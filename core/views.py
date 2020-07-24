from django.http import JsonResponse, HttpResponse
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

@csrf_exempt
def test(request):
    if request.method =='POST':
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        data["contributor"] = models.Contributor.objects.get(id = data["contributor"])
        data["team"] = models.Team.objects.get(id = data["team"])
        print(data)
        models.TeamMembership.objects.create(**data)

        return HttpResponse(str(data))
    else:
        return HttpResponse('use POST')

