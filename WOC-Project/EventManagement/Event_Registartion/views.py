from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from datetime import date
# Create your views here.
from .models import Event


def Reg(request):
    return render(request, 'Registration.html', {'name': "Parth"})


def EventReg(request):
    if request.method == "POST":
        event_name = request.POST['Eventname']
        description = request.POST['Description']
        location = request.POST['Location']
        link_of_poster = request.POST['LOP']
        from_date = request.POST['sdate']
        to_date = request.POST['edate']
        dead_date = request.POST['deadline']
        from_time = request.POST['stime']
        to_time = request.POST['ttime']
        dead_time = request.POST['dtime']
        host_name = request.POST['Hname']
        host_email = request.POST['Hemail']
        password = request.POST['password']

        date_o = date.today()
        date_o = str(date_o)

        date_o = int(date_o.replace('-', ''))
        print(from_date, date_o)
        if int(from_date.replace("-", "")) < date_o:
            status = "Coming Soon"
        elif date_o > int(to_date.replace("-", "")):
            status = "Finished"
        else:
            status = "Active Now"

        x = 1
        for temp2 in Event.objects.all():
            if temp2.EventName == event_name:
                x = 2
        print(x)
        if x == 2:
            messages.error(request, 'Event is already exist with this event name. please change eventname.')
            #            return render(request, 'temp.html', {'error':'Event is already exist with this event name. Please, go to Event-Registration change EventName.'})
            return redirect('Event-Registration')
        else:
            event = Event.objects.create(EventName=event_name, Description=description, Location=location,
                                         Link_of_Poster=link_of_poster, From_Date=from_date, From_Time=from_time,
                                         To_Date=to_date, To_Time=to_time, Dead_Date=dead_date, Dead_Time=dead_time,
                                         Host_Name=host_name, Host_Email=host_email, Password=password, Status=status)

          #  send_mail('Event-Registration', 'Thank you for using my Event management app.\n Your Event is successfully '
           #                                 'registered \n \nYour Event-ID : ' + str(event.id) + '\nEventName :' + str(
         #       event.EventName) + '\nYour Password:' + str(
          #      event.Password) + '\n\nYou can check Participants details on Event Dashboard By entering Event Id and Your Password',
           #           'parthdilipbharati@gmail.com',
           #           [event.Host_Email], fail_silently=False)
            event.save()
            print('Event Registered Successfully')

            return redirect('HomePage')
    else:
        return render(request, 'Registration.html', {messages: False})
