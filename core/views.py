from django.http import JsonResponse
from core import models, serializers


def read_issue(request, id):
    '''
    Given an http request and an id, return an http response
    with a JSON serialized list, including the issue with the
    given id.
    '''
    data = serializers.json_one(models.Issue, id=id)
    return JsonResponse(data, safe=False)


def read_issues(request):
    '''
    Given an http request and model class, 
    returns an http response with a JSON serialized 
    list of all the class' objects.
    '''
    data = serializers.json_many(models.Issue)
    return JsonResponse(data, safe=False)


'''
def read_many(model):
    def request_handler(request):
        data = serializers.json_one(model, id=id)
        return JsonResponse(data, safe=False)
    return request_handler
'''
