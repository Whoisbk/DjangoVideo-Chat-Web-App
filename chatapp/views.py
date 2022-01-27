from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from agora_token_builder import RtcTokenBuilder
import random
from time import time
import json
from .models import roomMember

# Create your views here.

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member,created = roomMember.objects.get_or_created(
        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name']
    )

    return JsonResponse({'name':data['name']},safe=false)

def getToken(request):
    app_Id = '985039d605dc45ae81936c57bf1cfd90'
    app_Certificate = 'e6914ab69c20484db97717e86160576b'
    channel_name = request.GET.get('channel')
    uid = random.randint(1,230)
    experation_time_sec = 3600 * 24
    current_timeStamp = time()
    privilage_Expired_Timestamp = current_timeStamp + experation_time_sec
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(app_Id,app_Certificate,channel_name,uid,role,privilage_Expired_Timestamp)

    return JsonResponse({'token':token,'uid':uid},safe = False)

def lobby(request):
    return render(request,'chatapp/lobby.html')


def room(request):
    return render(request,'chatapp/room.html')




