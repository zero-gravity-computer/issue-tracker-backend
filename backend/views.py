from core.models import Contributor
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def authenticate(request):
    try:
        credentials = json.loads(request.body.decode("utf-8"))
        c = Contributor.objects.get(username=credentials["username"])
        result = c.verify_password(credentials["password"])
        return HttpResponse(result)
    except:
        return HttpResponse("authentication failed")
