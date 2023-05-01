from django.http import HttpResponse
from django.shortcuts import render
from apps.xtest.models import Message


# Create your views here.
def getForm(request):
    messages = Message.objects.all()
    return render(request, 'form_test.html', {
        'messages': messages
    })


def postForm(request):
    message = Message()
    print(request.POST.get('name', 'unknown name'))
    print(request.POST.get('email', 'unknown email'))
    print(request.POST.get('address', 'unknown address'))
    print(request.POST.get('message', 'unknown message'))
    message.name = request.POST.get('name', 'unknown name')
    message.email = request.POST.get('email', 'unknown email')
    message.address = request.POST.get('address', 'unknown address')
    message.message = request.POST.get('message', 'unknown message')
    message.save()
    return HttpResponse('OK')
