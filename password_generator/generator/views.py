from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    #return HttpResponse('Hello there friend!')
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    thepassword = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')

    #this checks the selected option on the URL
    if request.GET.get('uppercase'):
        chars.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))
    if request.GET.get('special'):
        chars.extend(list('!@#$%~&^*()'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    for x in range(length):
        thepassword += random.choice(chars)
    # the third argument injects stuff to our template file
    # and to display it we use {{}} in the template
    return render(request, 'generator/password.html', {'password': thepassword})

