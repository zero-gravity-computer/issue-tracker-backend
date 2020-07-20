from django.core import serializers
from core import models
import datetime

''' original serializers:


def json_many(model):
    data = serializers.serialize("json", model.objects.all())
    return data


def json_one(model, id):
    data = serializers.serialize("json", [model.objects.get(id=id)])
    return data

'''
def ModelToDict(obj):
    result = {}
    for field in obj._meta.fields:
        value = getattr(obj, field.name)

        #handles datetime fields
        if type(value) == datetime.datetime:
            value = value.isoformat()
        #handles relational fields 
        if hasattr(value, "id"):
            value = value.id
        
        result[field.name] = value
    return result

#runs test of an object
'''from core.models import Team
i = Team.objects.get(id=1)
print(ModelToDict(i))'''

