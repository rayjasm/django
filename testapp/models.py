from django.db import models
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json

class testdb(models.Model):
    id = models.IntegerField(primary_key=True)
    image_path = models.CharField(max_length=255)
    success = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    returnclass = models.IntegerField()
    confidence = models.DecimalField(max_digits=5, decimal_places=4)
    request_timestamp = models.IntegerField()
    response_timestamp = models.IntegerField()

class exam(models.Model):
    APIKEY = "**********"
    url = "http://example.com/"
    image_path = "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"
    
    headers = { 'token': APIKEY }
    data = { 'image_path': image_path }
    res = requests.post(url, headers=headers, data=data).json()

    success = res['success']
    message = res['message']
    returnclass = res['estimated_data'][0]['class']
    confidence = res['estimated_data'][0]['confidence']

    testdb = testdb(image_path=image_path, success=success, message=message,
                    returnclass=returnclass, confidence=confidence)
    testdb.save()