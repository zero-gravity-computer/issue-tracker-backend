
from core.models import *
from core.middleware import *
from django_instant_rest import patterns
from django.urls import path

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def authenticate(request):
    credentials = json.loads(request.body.decode("utf-8"))
    c = Contributor.objects.get(username=credentials["username"])
    result = c.verify_password(credentials["password"])
    print(result)
    return HttpResponse(result)

urlpatterns = [
    patterns.resource('issues', Issue, middleware = issue_resource_policies),
    patterns.resource('organizations', Organization),
    patterns.resource('contributors', Contributor),
    patterns.resource('teams', Team),
    patterns.resource('team_memberships', TeamMembership),
    patterns.resource('comments', Comment),
    path('contributors/authenticate', authenticate)
]