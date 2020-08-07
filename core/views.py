from django.http import JsonResponse, HttpResponse
import core
from core import models, serializers
import json
from django.views.decorators.csrf import csrf_exempt

def read_many(model):
    def request_handler(request):
        obj_list = model.objects.all()
        data = serializers.serialize_many(obj_list)
        return HttpResponse(data, content_type="application/json")
    return request_handler


def read_one(model):
    def request_handler(request, id):
        obj = model.objects.get(id=id)
        data = serializers.serialize(obj)
        return HttpResponse(data, content_type="application/json")
    return request_handler
  

def create_one(model):
    @csrf_exempt
    def request_handler(request):
        if request.method =='POST':
            data = json.loads(request.body.decode("utf-8"))

            for key in data:
                field = getattr(model, key)
                #if the key corresponds to a relational field,
                #replaces data[key] with object key id references
                if field.field.is_relation is True:
                    related_model = field.field.related_model
                    data[key] = related_model.objects.get(id = data[key])

            model.objects.create(**data)
            return HttpResponse(str(data))
        else:
            return HttpResponse('use POST')
    return request_handler


def resource(model):
    @csrf_exempt
    def request_handler(request, id=None):
        if request.method =='POST':
            return create_one(model)(request)
        elif request.method =='GET':
            if id:
                return read_one(model)(request, id)
            else:
                return read_many(model)(request)
    return request_handler