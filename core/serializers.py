from django.core import serializers
from core import models

def json(model):
    data = serializers.serialize("json", model.objects.all())
    return data


