from django.http import JsonResponse, HttpResponse
import core
from core import models, serializers
import json
from django.views.decorators.csrf import csrf_exempt

errors = [
    { "message": "Requested id does not exist" }
]
id_not_exists_err = { "message": "Requested id does not exist" }

def read_many(model):
    def request_handler(request):
        obj_list = model.objects.all()
        data = serializers.serialize_many(obj_list)
        return HttpResponse(data, content_type="application/json")
    return request_handler


def read_one(model):
    def request_handler(request, id):
        try:
            obj = model.objects.get(id=id)
            data = serializers.serialize(obj)
            return HttpResponse(data, content_type="application/json")
        except:
            return HttpResponse(str(id_not_exists_err))
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

            m = model.objects.create(**data)
            return HttpResponse(serializers.serialize(m))
        else:
            return HttpResponse('use POST')
    return request_handler


def update_one(model):
    @csrf_exempt
    def request_handler(request, id): 
        change_data = json.loads(request.body.decode("utf-8")) 
        try:
            obj = model.objects.get(id=id)
                
            for field_name in change_data:
                field = getattr(model, field_name)
                if field.field.is_relation is True:
                    related_model = field.field.related_model
                    change_data[field_name] = related_model.objects.get(id = change_data[field_name])
                setattr(obj, field_name, change_data[field_name])

            obj.save()
            data = serializers.serialize(obj)
            return HttpResponse(data, content_type="application/json")
        except:
            return HttpResponse(str(id_not_exists_err))
    return request_handler


def delete_one(model):
    @csrf_exempt
    def request_handler(request, id):
        try:
            obj = model.objects.get(id=id)
            obj.delete()
            return HttpResponse("object deleted")
        except:
            return HttpResponse(str(id_not_exists_err))
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
        elif request.method == 'PUT':
            if id:
                return update_one(model)(request, id)
        elif request.method =='DELETE':
            if id:
                return delete_one(model)(request, id)
    return request_handler