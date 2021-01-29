from core.models import *
from core.middleware import *
from django_instant_rest import patterns
from django.urls import path
from .views import authenticate, get_contributor_by_token


urlpatterns = [
    patterns.resource('issues', Issue, middleware = issue_resource_policies),
    patterns.resource('organizations', Organization),
    patterns.resource('contributors', Contributor),
    patterns.resource('teams', Team),
    patterns.resource('team_memberships', TeamMembership),
    patterns.resource('comments', Comment),
    path('contributors/authenticate', authenticate),
    path('contributors/by_token', get_contributor_by_token)
]