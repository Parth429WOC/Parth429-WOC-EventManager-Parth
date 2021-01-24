from django.shortcuts import render, redirect
from Event_Registartion.models import Event
from Participant_Registration.models import Participant
from django.contrib import messages


# Create your views here.

def Dashboard(request):
    if request.method == "POST":

        event_id = request.POST['Id']
        h_password = request.POST['password']
        x = 1
        temp = Event()
        for temp in Event.objects.all():
            if temp.id == int(event_id) and str(temp.Password) == h_password:
                x = 2
                break
        print(x)
        if x == 2:
            temp3 = []
            for temp2 in Participant.objects.all():
                if temp2.Event_Name == temp.EventName:
                    temp3.append(temp2)

            return render(request, 'EventDashboard.html', {'part': temp3, 'event': temp, 'is_participant': True
                                                           })
        else:
            messages.error(request,  'User is not exist. Please check your Event-Id or Password.' )
            #         return render(request, 'temp.html', {'error': 'User is not exist. Please check your Event-Id or '
            #                                                   'Password.'})
            return redirect('Event-Dashboard')
    else:
        return render(request, 'EventDashboard.html', {'is_participant': False})
