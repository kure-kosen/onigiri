from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import requests
import os

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def index(request):
    return HttpResponse("Hello World")

@csrf_exempt
def callback(request):
    try:
        action = json.loads(request.body.decode('utf-8'))['action']
        from pprint import pprint
        pprint(action)
        entities = action['display']['entities']
        if action['type'] == 'action_create_card':
            list_name = entities['list']['text']
            card_name = entities['card']['text']
            member_name = entities['memberCreator']['text']
            body = f'リスト名:{list_name} カード名:{card_name} メンバー名:{member_name}'
            print(body)
        elif action['type'] == 'action_move_card_from_list_to_list':
            pass               
    except Exception as e:
        pass
    return HttpResponse("callback")

