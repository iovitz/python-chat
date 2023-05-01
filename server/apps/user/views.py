from django.http import HttpResponse
from django.shortcuts import render

from apps.common.const.error_code import ErrorCode


# Create your views here.
def getHello(request):
    name = request.GET.get('name', '张三')
    age = request.GET.get('age', '20')
    raise {
        'code': ErrorCode.ServerError,
        'name': '123'
    }
    return HttpResponse('Hello, i\'m, {0}, age is {1}'.format(name, age))
