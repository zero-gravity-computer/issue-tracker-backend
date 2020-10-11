
from django.urls import re_path
from core import views

# Create a urlpattern element that allows CRUD
# operations for a given model
def resource(name, model, suffix = '.json'):
    return re_path(
        rf"{name}/(?P<id>\d+){suffix}|{name}{suffix}",
        views.resource(model)
    )


