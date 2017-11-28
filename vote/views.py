from django.shortcuts import render
from django.contrib.auth import logout, get_user

def index(request):
    # print(get_user(request))
    rend = render(request, 'vote/vote.html', {logout: logout, request: request})
    logout(request)
    return rend

