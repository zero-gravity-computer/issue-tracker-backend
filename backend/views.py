from core.models import Contributor
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import jwt
from .settings import SECRET_KEY


@csrf_exempt
def authenticate(request):
    '''allowing requests to provide username/password
    combinations in exchange for json web token'''
    try:
        credentials = json.loads(request.body.decode("utf-8"))
    except:
        message = "expected POST request with json body"
        return JsonResponse({'error':message}, status=400)
    try:
        c = Contributor.objects.get(username=credentials["username"])
        c.verify_password(credentials["password"])
        payload = {"contributor_id": c.id}
        encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return JsonResponse({"data": {"token":encoded_jwt}})
    except:
        message = "incorrect username/password combination"
        return JsonResponse({'error':message}, status=400)
    

