from django.http import JsonResponse, HttpResponse
import core
from core import models, serializers
import json
from django.views.decorators.csrf import csrf_exempt
import dateutil.parser
from django.db.models.fields import DateTimeField
from django.utils.timezone import make_aware


id_not_exists_err = {"message": "Requested id does not exist" }
empty_body_err = {"message" : "Request body is empty"}
no_body_err = {"message" : "Request body does not exist"}
invalid_json_err = {"message" : "Request body is not valid json"}
missing_id_err = {"message" : "required id not provided"}
invalid_data_err = {"message" : "invalid data type received"}
unsupported_method_err = {"message" : "request method not supported by url"}



def date_fields(model):
    '''
    Return a list of strings that correspond to a model's
    fields that are instances of DateTimeField
    '''
    def is_date_field(name):
        return type(getattr(model, name).field) == DateTimeField
    
    field_names = [f.name for f in model._meta.fields]
    return list(filter(is_date_field, field_names))



def read_many(model):
    def request_handler(request):
        params = { key: request.GET.get(key) for key in request.GET }
        filter_set=None

        # Parsing incoming date fields
        for key in params:
            for field in date_fields(model):
                if key.startswith(field):
                    try:
                        naive_date = dateutil.parser.parse(params[key])
                        params[key] = make_aware(naive_date)
                    except:
                        message = f"Invalid date string provided for field {key}"
                        invalid_date_err = { "message": message }
                        return JsonResponse({"errors": [invalid_date_err]})

        #applies smart filters from django
        for key in params:
            try:
                filter_set = model.objects.filter(**{key : params[key]})
            except:
                pass
        
        #gets all results if no filter is provided
        if filter_set is None:
            filter_set = model.objects.all()

        #retrieves results
        data = list(map(serializers.model_to_dict, filter_set))
        return JsonResponse({"data": data})
    return request_handler


def read_one(model):
    def request_handler(request, id):
        try:
            obj = model.objects.get(id=id)
        except:
            return JsonResponse({"errors": [id_not_exists_err]})
        data = serializers.model_to_dict(obj)
        return JsonResponse({"data": data})        
    return request_handler
  

def create_one(model):
    @csrf_exempt
    def request_handler(request):
        try:
            data = json.loads(request.body.decode("utf-8"))
        except:
            return JsonResponse({"errors": [invalid_json_err]})
        try:
            for key in data:
                field = getattr(model, key)
                if field.field.is_relation is True:
                    related_model = field.field.related_model
                    data[key] = related_model.objects.get(id = data[key])

            m = model.objects.create(**data)
            data = serializers.model_to_dict(m)
            return JsonResponse({"data" : data})
        except:
            return JsonResponse({"errors": [invalid_data_err]})
    return request_handler


def update_one(model):
    @csrf_exempt
    def request_handler(request, id): 
        try:
            change_data = json.loads(request.body.decode("utf-8"))
        except:
            return JsonResponse({"errors": [invalid_json_err]})
        try:
            obj = model.objects.get(id=id)
                
            for field_name in change_data:
                field = getattr(model, field_name)
                if field.field.is_relation is True:
                    related_model = field.field.related_model
                    change_data[field_name] = related_model.objects.get(id = change_data[field_name])
                setattr(obj, field_name, change_data[field_name])

            obj.save()
            data = serializers.model_to_dict(obj)
            return JsonResponse({"data" : data})
        except:
            return JsonResponse({"errors": [id_not_exists_err]})
    return request_handler


def delete_one(model):
    @csrf_exempt
    def request_handler(request, id):
        try:
            obj = model.objects.get(id=id)
            obj.delete()
            data = serializers.model_to_dict(obj)
            return JsonResponse({"data" : data})
        except:
            return JsonResponse({"errors": [id_not_exists_err]})
    return request_handler


def resource(model):
    @csrf_exempt
    def request_handler(request, id=None):
        if request.method =='POST':
            return create_one(model)(request)
        elif request.method =='GET':
            if id:
                return read_one(model)(request, id)
            else:
                return read_many(model)(request)
        elif request.method == 'PUT':
            if id:
                return update_one(model)(request, id)
            else:
                return JsonResponse({"errors": [missing_id_err]})
        elif request.method =='DELETE':
            if id:
                return delete_one(model)(request, id)
            else:
                return JsonResponse({"errors": [missing_id_err]})
        else:
            return JsonResponse({"errors" : [unsupported_method_err]})
    return request_handler

def error_response(error):
    return JsonResponse({"errors" : [error]})
