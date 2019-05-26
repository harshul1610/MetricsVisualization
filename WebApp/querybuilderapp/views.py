from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from django.apps import apps
import json
import sqlite3
import re

myapp = apps.get_app_config('querybuilderapp')
models_dict = myapp.models


def get_model_fields(model):
    field_objs = model._meta.fields
    fields = list(map(lambda x: (x.name, x.get_internal_type()), field_objs))
    print(fields)
    return fields

# Create your views here.
def home(request):
    return render(request, 'querybuilderapp/index.html', context={'tables': models_dict})

def get_schema_details(request):
    model_str = request.POST.get('table_name', None)
    model_class = models_dict[model_str]
    model_attr = get_model_fields(model_class)
    return JsonResponse(model_attr, safe=False)