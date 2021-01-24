from django.contrib import messages
from django.shortcuts import render, redirect
import twilio
from twilio.rest import Client
# Create your views here.
from Event_Registartion.models import Event
from datetime import date
from datetime import datetime
from Participant_Registration.models import Participant


def ParticipantReg(request):
    if request.method == "GET":
        events = Event.objects.all()
        temp = []
        today = datetime.now()
        today_date = date.today()
        now_h = int(today.hour)
        now_m = int(today.minute)
        for event in events:
            dead_time = str(event.Dead_Time)
            dead_time = dead_time.split(':')
            if event.Dead_Date > today_date:
                temp.append(event)
            elif event.Dead_Date == today_date and int(dead_time[0]) > now_h:
                temp.append(event)
            elif event.Dead_Date == today_date and int(dead_time[0]) == now_h and int(dead_time[1]) >= now_m:
                temp.append(event)
        return render(request, 'ParticipantRegistration.html', {'Event_Available': temp})
    else:
        name = request.POST['Name']
        contact = request.POST['Contact']
        email = request.POST['email']
        event = request.POST['reg']
        type_reg = request.POST['typeOreg']
        if type_reg == "Individual":
            nop = 1
        else:
            nop = request.POST['NoParticipant']

        for temp in Event.objects.all():
            if temp.EventName == event:
                break

        x = 1
        for participant in Participant.objects.all():
            if (participant.Name == name and str(participant.Contact_No) == contact) or str(participant.Email) == email:
                x = 2
                break

        if x == 2:
            messages.error(request, 'Participant is already exist. You can take part in event only once.')
            #       return render(request, 'temp.html', {
            #          'error': 'Participant is already exist. You can take part in event only once.'})
            return redirect('Participant-Registration')
        else:
            temp = Participant.objects.create(Name=name, Contact_No=contact, Email=email, Event_Name=event,
                                              Type_Of_Registration=type_reg, No_Of_Participant=nop)
            event2 = Event()
            for event2 in Event.objects.all():
                if event2.EventName == event:
                    break


            print('participant created')

            return redirect('HomePage')
