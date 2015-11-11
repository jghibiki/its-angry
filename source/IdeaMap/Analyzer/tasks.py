from __future__ import absolute_import
import sys
import os
import datetime
from dateutil import parser
import time, signal
from sklearn.externals import joblib
from celery import shared_task
from Core.models import Tweet, ProcessedTweet
from django.conf import settings
from django.contrib.gis.geos import Point

if __name__ != "__main__":

    cache_dir = settings.ANALYZER_CACHE_DIR
    
    vectorizer_cache = "vectorizer.pickle"
    vectorizer_cache = os.path.join(cache_dir, vectorizer_cache)
    
    classifier_cache = "classifier.pickle"
    classifier_cache = os.path.join(cache_dir, classifier_cache)

    vectorizer = joblib.load(vectorizer_cache)
    classifier_liblinear = joblib.load(classifier_cache)

@shared_task
def classify(tweet):

    test_vectors = vectorizer.transform([tweet["text"]])
    prediction_liblinear = classifier_liblinear.predict(test_vectors)
    confidence = classifier_liblinear.decision_function(test_vectors)[0]
    classification= prediction_liblinear[0]

    newTweet = ProcessedTweet(
        entities=tweet["entities"],
        processed_date=datetime.datetime.utcnow(),
        created_date= parser.parse(tweet["created_date"]),
        text=tweet["text"],
        original=tweet["original"],
        rating=confidence,
        classification=classification,
	point = Point(tweet["point"][0], tweet["point"][1]),
    )

    newTweet.save()

    return (newTweet.id, classification, confidence)
