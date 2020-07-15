from django.http import JsonResponse
from core import models, serializers



'''
def read_many(model):
    def request_handler(request):
        data = serializers.json_one(model, id=id) pk instead of id?
        return JsonResponse(data, safe=False)
    return request_handler
'''
def read_many(model):
    def request_handler(request):
        data = serializers.json_many(model)
        return JsonResponse(data, safe=False)
    return request_handler

def read_one(model):
    def request_handler(request, id):
        data = serializers.json_one(model, id=id)
        return JsonResponse(data, safe=False)
    return request_handler