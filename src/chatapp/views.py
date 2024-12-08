from django.shortcuts import render,redirect
from .models import Room ,Message
# Create your views here.

def CreateRoom(request):
    if request.method == "POST":
        username = request.POST['username']
        room = request.POST['room']
        try:
            get_room = Room.objects.get(room_name=room)
            return redirect("room", room=room,username=username)
        except Room.DoesNotExist:
            #return f"The Tour Guide Didn't initiate This Room Yet!!"
            new_room = Room(room_name=room)
            new_room.save()
            return redirect("room", room=room,username=username)
    return render(request,'index.html')


def MessageView(request,room,username):
    room_name =Room.objects.get(room_name=room)
    try:
        room_messages =Message.objects.filter(room=room_name)
        # if not isinstance(room_messages,(list,tuple,dict)):
        #     room_messages = [].append(room_messages)
    except Message.DoesNotExist:
        room_messages = []
    context ={
        "messages":room_messages,
        "user":username,
        "room_name":room,
    }

    return render(request,'_message.html',context=context)