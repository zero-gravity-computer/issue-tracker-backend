from django.core import serializers
from core import models

def json_many(model):
    '''
    Given a model class, retrieve a list of its objects,
    and represent them as a JSON string.
    '''
    data = serializers.serialize("json", model.objects.all())
    return data


def json_one(model, id):
    '''
    Retrieve an object by its id and return it as a JSON string.
    '''
    data = serializers.serialize("json", [model.objects.get(id=id)])
    return data