from core.models import Contributor
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import jwt
from .settings import SECRET_KEY


@csrf_exempt
def authenticate(request):
    try:
        credentials = json.loads(request.body.decode("utf-8"))
        c = Contributor.objects.get(username=credentials["username"])
        if c.verify_password(credentials["password"]):
            payload = {"contributor_id": c.id}
            encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            return HttpResponse(encoded_jwt)
    except:
        return HttpResponse("authentication failed")
