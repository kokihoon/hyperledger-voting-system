from django.shortcuts import render, HttpResponse
from django.contrib.auth import logout, get_user

import hashlib
from datetime import datetime

from VotingSystem.settings import MEMBER_URL

import requests


def index(request):
    user_id = get_id(get_user(request))
    request_json = get_number_json(user_id)
    r = requests.post(
        MEMBER_URL,
        json=request_json
    )

    if r.status_code == 200:
        rend = render(request, 'vote/vote.html', {'user_id': user_id})
        logout(request)
        return rend
    else:
        return HttpResponse('로그인 실패. 다시 시도 해보세요.')


def get_id(user) -> str:
    seed_data = str(user) + str(datetime.now().time())
    return hashlib.sha3_256(seed_data.encode()).hexdigest()


def get_number_json(user_id):
    return {
        "$class": "org.acme.vehicle.auction.Member",
        "balance": 1,
        "email": user_id,
        "firstName": user_id,
        "lastName": user_id
    }
