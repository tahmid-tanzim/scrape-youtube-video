from django.contrib import admin
from django.http import JsonResponse


# Register your models here.
def get(request):
    response_data = {}
    if request.method == 'GET':
        response_data['result'] = 'error'
        response_data['message'] = 'Some error message'
    return JsonResponse(response_data)
