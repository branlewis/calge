from django.urls import path
from . import views

app_name = "clock"
urlpatterns = [
    path("clock/me/", views.showTimeCard.as_view(), name='timeCard'),
    #path("clock/timeIn", views.newTimeIn, name='newTimeIn'),
    path('<slug:slug>/', views.showTimeCard.as_view(),
         name='showTimeCard'),

]
