from django.http import JsonResponse
from core import models, serializers

def read_issues(request):
    data = serializers.json(models.Issue)
    return JsonResponse(data, safe=False)
