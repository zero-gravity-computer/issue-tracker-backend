
from core.models import *
from core.middleware import *
from django_instant_rest import patterns


urlpatterns = [
    patterns.resource('issues', Issue, middleware = issue_resource_policies),
    patterns.resource('contributors', Issue),
    patterns.resource('organizations', Organization),
    patterns.resource('contributors', Contributor),
    patterns.resource('teams', Team),
    patterns.resource('team_memberships', TeamMembership),
    patterns.resource('comments', Comment),
]

