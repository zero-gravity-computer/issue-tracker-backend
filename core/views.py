from django.http import JsonResponse, HttpResponse
import core
from core import models, serializers
import json

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


#test view is below

from django.views.decorators.csrf import csrf_exempt

def field_is_relational(field, model):
    return "fields.related" in str(getattr(model , field))
    


@csrf_exempt
def test(request):
    if request.method =='POST':
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        for key in data:
            field = getattr(core.models.Team, key)
            #if the key corresponds to a relational field,
            #replaces data[key] with object key id references
            if field.field.is_relation is True:
                related_model = field.field.related_model
                data[key] = related_model.objects.get(id = data[key])
        print(data)
        models.Team.objects.create(**data)
        return HttpResponse(str(data))
    else:
        return HttpResponse('use POST')
            

'''data["contributor"] = models.Contributor.objects.get(id = data["contributor"])
        data["team"] = models.Team.objects.get(id = data["team"])'''


'''from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def create_object(request):
    data = {"" : ""}
    if request.method =='POST':
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return HttpResponse(str(data))
        for field in data._meta.fields:
            value = getattr(data, field.name)
            if type(data) == datetime.datetime:
                data[field.name] = data.isoformat()
            if hasattr(data, "id"):
                data = data.id
            result[field.name] = data
            data[field.name] = data[POST.field.name]
        return HttpResponse(str(result))
    else:
        return HttpResponse('use POST')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def create_one(model):
    data = {"" : ""}
    def test(request):
        if request.method =='POST':
            data = json.loads(request.body.decode("utf-8"))
            for key in post.body():
                value = getattr(model, field.name)
                if type(data) == datetime.datetime:
                    data[field.name] = data.isoformat()
                if hasattr(data, "id"):
                    data = data.id
                result[field.name] = data
                data[field.name] = dat[POST.field.name]
            return HttpResponse(str(result))
        else:
            return HttpResponse('use POST')
    return HttpResponse(str(data))

@csrf_exempt
def test2(obj):
    data = {}
    def request_handler(request):
        data = json.loads(request.body.decode("utf-8"))
        if request.method == 'POST':
            for key in request.POST(json):
                data[key] = request.POST[key]
            for value in request.POST:
                data[value] = request.POST[key]
        else:
            print('use POST method to access this function')
    return HttpResponse(str(data))'''