from django.http import JsonResponse, HttpResponse
from core import models, serializers

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
        return HttpResponse('WOO')
    else:
        return HttpResponse('use POST')

