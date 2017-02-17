from rest_framework import viewsets
import models
import serializers


class Units(viewsets.ViewSet):
    morchas = models.Morcha.objects.all()
    print morchas.units