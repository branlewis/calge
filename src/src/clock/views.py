from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, get_list_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
# from clock.models import shiftTime
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests
#from .forms import timeInForm, timeOutForm
import datetime


class showTimeCard(LoginRequiredMixin, generic.TemplateView):
    template_name = "clock/showTimeCard.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        timeCard = get_list_or_404(models.shiftTime)
        todayShift, userShifts = self.getUserTimeShift(user, timeCard)

        kwargs["show_timeCard"] = timeCard
        kwargs["show_user"] = user
        kwargs["show_todayShift"] = todayShift
        kwargs["show_userShifts"] = userShifts
        return super().get(request, *args, **kwargs)

    def post(self, request):
        user = self.request.user
        today = datetime.datetime.today()
        timeNow = datetime.datetime.now()
        if 'timeInbtn' in request.POST:
            shiftTime = models.shiftTime()
            shiftTime.user = user
            shiftTime.date = today
            shiftTime.timeIn = timeNow
            shiftTime.timeOut = timeNow
            shiftTime.save()
            # return render(request, "/home.html")
            return redirect("/")
        if 'timeOutbtn' in request.POST:
            timeCard = get_list_or_404(models.shiftTime)
            todayShift, userShifts = self.getUserTimeShift(user, timeCard)
            todayShift.timeOut = timeNow
            todayShift.save()
            # return render(request, "/home.html")
            return redirect("/")

    def getUserTimeShift(self, user, timeCard):
        print("\n\n")
        today = datetime.datetime.today()
        print("today=", today)
        print("today.date()=", today.date())
        todayShift = False
        userShifts = []
        for shift in timeCard:
            if shift.user != user:
                continue
            print("user shift.date=", shift.date)
            print("user shift.timeIn=", shift.timeIn)
            print("user shift.timeOut=", shift.timeOut)
            if str(shift.timeIn) != str(shift.timeOut):
                userShifts.append(shift)
            if shift.date != today.date():
                continue
            print("user shift.timeOut=", shift.timeOut)
            if str(shift.timeIn) != str(shift.timeOut):
                continue
            todayShift = shift
            print("today shift.date=", shift.date)
            print("today shift.timeIn=", shift.timeIn)
            print("today shift.timeOut=", shift.timeOut)
        return todayShift, userShifts

    '''def get_time_In(request):
        if request.method("POST"):
            form = timeInForm(request.POST)
            if form.is_valid():
                shiftTime.user = self.user
                shiftTime.date = dateField.now()
                shiftTime.timeIn = TimeField.now()
                shiftTime.save()
                redirect("Home")
        else:
            form = timeInForm()
        return render(request, "showTimeCard.html", {'form':form})'''

    '''def post(self, request):
        shiftTime.self.user = self.user
        shiftTime.self.date = dateField.now()
        shiftTime.self.timeIn = TimeField.now()
        shiftTime.self.save()
        return True'''

'''def request_page(request):
    if(request.GET.get('timeInbtn')):
        shiftTime.addTimeIn()
    return redirect("Home")
'''

def newTimeIn(self):
    '''models.shiftTime.addTimeIn(self)'''
    return redirect("Home")


'''def filterTop(timeCard):
    currentEntries = timeCard.filter(user = request.user)
    current = currentEntries.pop()
    if current.timeOut == null:
        return False
    else:
        return True

def filterTop(timeCard):
    current = timeCard.pop()
    if current.timeOut == null:
        return False
    else:
        return True
'''
def dump(obj):
   for attr in dir(obj):
       if hasattr( obj, attr ):
           print( "obj.%s = %s" % (attr, getattr(obj, attr)))


'''
def index(request):
    return render_to_response('index.html', {
        'clockIn': clockIn.objects.all(),
        'clockOut': clockOut.objects.all()
    })

def viewClock(request, slug):
    return render_to_response('index.html', {
        'clockIn': get_object_or_404(clockIn, slug=slug),
        'clockOut': get_object_or_404(clockOut, slug=slug)
    })

@register.filter(name='zip')
def zip_lists(clockIn, clockOut):
  return zip(clockIn, clockOut)
'''
