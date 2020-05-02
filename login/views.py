from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from login.models import MyUser
from rest_framework import generics
from .serializers import UserProfileSerializer
from login.forms import UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def homepage(request):
    return render(request, 'login/base.html')

"""
    user = request.POST['username']
    pswd = request.POST['password']
    user = authenticate(request, username=user, password=pswd)

    if user is not None:

"""

def index(request):
    return render(request, 'login/index.html')


def register(request):
    return render(request,'login/registration.html')

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(phone_no__contains=query)

            results = MyUser.objects.filter(lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'login/search.html', context)

        else:
            return render(request, 'login/search.html')

    else:
        return render(request, 'login/search.html')



class APIObjects(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserProfileSerializer


class APIObjectsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserProfileSerializer
