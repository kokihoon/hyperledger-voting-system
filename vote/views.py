from django.shortcuts import render, HttpResponse
from django.contrib.auth import logout, get_user
from django.contrib.auth.models import User

import hashlib
import json
from datetime import datetime

from VotingSystem.settings import MEMBER_URL, VEHICLE_LISTING_RUL

import requests


def index(request):
    user_id = get_id(get_user(request))
    request_json = get_number_json(user_id)
    r = requests.post(
        MEMBER_URL,
        json=request_json
    )
    print(r.text)
    if r.status_code == 200:
        rend = render(request, 'vote/vote.html', {'user_id': user_id})
       # logout(request)
        return rend
    else:
        return HttpResponse('로그인 실패. 다시 시도 해보세요.')


def participation_rate(request):
    voted_count = 0

    r = requests.get(VEHICLE_LISTING_RUL)
    r_json = r.json()
    if r.status_code == 200:
        for listing in r_json:
            if not('votes' in listing):
                continue
            voted_count += len(listing['votes'])

        all_user_cnt = 1
        all_user_cnt = len(User.objects.filter(is_superuser=False))

        rate = voted_count / all_user_cnt * 100
        print('rate', rate)
        return HttpResponse(json.dumps({'rate': rate}))
    else:
        return HttpResponse(status=500)

def get_id(user) -> str:
    seed_data = str(user) + str(datetime.now().time())
    return hashlib.sha3_256(seed_data.encode()).hexdigest()


def get_number_json(user_id):
    return {
        "$class": "org.ioks.vote.Voter",
        "ballot": 1,
        "id": user_id
    }
