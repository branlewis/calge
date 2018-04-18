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

        #kwargs["show_timeCard"] = timeCard
        #kwargs["show_user"] = user
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
        # print("today=", today)
        # print("today.date()=", today.date())
        todayShift = False
        userShifts = []
        for shift in timeCard:
            if shift.user != user:
                continue
            # print("user shift.date=", shift.date)
            # print("user shift.timeIn=", shift.timeIn)
            # print("user shift.timeOut=", shift.timeOut)
            if str(shift.timeIn) != str(shift.timeOut):
                userShifts.append(shift)
            if shift.date != today.date():
                continue
            # print("user shift.timeOut=", shift.timeOut)
            if str(shift.timeIn) != str(shift.timeOut):
                continue
            todayShift = shift
            # print("today shift.date=", shift.date)
            # print("today shift.timeIn=", shift.timeIn)
            # print("today shift.timeOut=", shift.timeOut)
        return todayShift, userShifts


# Debug purposes only
def dump(obj):
   for attr in dir(obj):
       if hasattr( obj, attr ):
           print( "obj.%s = %s" % (attr, getattr(obj, attr)))
