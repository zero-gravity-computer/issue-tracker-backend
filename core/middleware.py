
from django.http import JsonResponse

'''
Middleware to can be used to modify the way
that requests are handled. This is how we'll
add access control policies, validation, etc..
'''


def issue_resource_policies(get_response):
    # One-time configuration and initialization.

    def middleware(request, id = None):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request, id)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

def allow_cors(get_response):
    # One-time configuration and initialization.

    def middleware(request, id = None):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)
        response['Access-Control-Allow-Origin'] = "*"

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware


