from django.core import serializers
from core import models
import datetime
import json

def model_to_dict(obj):
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



def serialize(obj, indent=2):
    dictionary = model_to_dict(obj)
    return json.dumps(dictionary, indent=indent)

def serialize_many(obj_list, indent=2):
    dictionaries = [model_to_dict(obj) for obj in obj_list]
    return json.dumps(dictionaries, indent=indent)

'''
#runs test of an object
from core.models import Issue
i = Issue.objects.all()
print(serialize_many(i))
'''