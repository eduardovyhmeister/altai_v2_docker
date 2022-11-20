""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # this add the urls specificioant fro events urls
    path('register',views.UserRegisterView,name='register'),
    path('login',views.UserLoginView,name='login'),
    path('logout',views.UserLogout,name='logout'),
    path('howToAltai',views.HowToAltai,name='howToAltai'),
    path('fundamentalRights',views.FundamentalRights,name='fundamentalRights'),
    path('howToTAIRMP',views.HowToTAIRMP,name='howToTAIRMP'),
    path('about',views.About,name='about'),

    path('myAltais',views.MyAltais,name='myAltais'),
    path('myAltaisCreate',views.MyAltaisCreate,name='myAltaisCreate'),
    path('myAltaisDelete/<pk>',views.MyAltaisDelete,name='myAltaisDelete'),
    path('myAltaisHome/<pk>',views.MyAltaisHome,name='myAltaisHome'),
    path('myAltaiReq1/<int:pk>', views.MyAltaiReq1, name='myAltaiReq1'),
    path('myAltaiReq2/<int:pk>', views.MyAltaiReq2, name='myAltaiReq2'),
    path('myAltaiReq3/<int:pk>', views.MyAltaiReq3, name='myAltaiReq3'),
    path('myAltaiReq4/<int:pk>', views.MyAltaiReq4, name='myAltaiReq4'),
    path('myAltaiReq5/<int:pk>', views.MyAltaiReq5, name='myAltaiReq5'),
    path('myAltaiReq6/<int:pk>', views.MyAltaiReq6, name='myAltaiReq6'),
    path('myAltaiReq7/<int:pk>', views.MyAltaiReq7, name='myAltaiReq7'),
    path('myAltaiResult/<int:pk>',views.ResultsPageAltai,name='myAltaiResult'),

    path('myTaiprm',views.MyTaiprm,name='myTaiprm'),
    path('myTaiprmCreate',views.MyTaiprmCreate,name='myTaiprmCreate'),
    path('myTaiprmDelete/<pk>',views.MyTaiprmDelete,name='myTaiprmDelete'),
    path('myTaiprmHome/<pk>',views.MyTaiprmHome,name='myTaiprmHome'),
    path('myTaiprmStep1/<int:pk>', views.MyTaiprmStep1, name='myTaiprmStep1'),
    path('myTaiprmStep2/<int:pk>', views.MyTaiprmStep2, name='myTaiprmStep2'),
    path('myTaiprmStep3/<int:pk>', views.MyTaiprmStep3, name='myTaiprmStep3'),
    path('myTaiprmStep4/<int:pk>', views.MyTaiprmStep4, name='myTaiprmStep4'),
    path('myTaiprmStep5/<int:pk>', views.MyTaiprmStep5, name='myTaiprmStep5'),
    path('myTaiprmStep6/<int:pk>', views.MyTaiprmStep6, name='myTaiprmStep6'),
    path('myTaiprmStep7/<int:pk>', views.MyTaiprmStep7, name='myTaiprmStep7'),
    path('myTaiprmStep8/<int:pk>', views.MyTaiprmStep8, name='myTaiprmStep8'),
    path('myTaiprmStep9/<int:pk>', views.MyTaiprmStep9, name='myTaiprmStep9'),
    path('myTaiprmStep10/<int:pk>', views.MyTaiprmStep10, name='myTaiprmStep10'),
    path('myTaiprmStep11/<int:pk>', views.MyTaiprmStep11, name='myTaiprmStep11'),
    path('myTaiprmResult/<int:pk>',views.MyTaiprmResults,name='myTaiprmResult'),
    path('myTaiprmPdf/<int:pk>',views.MyTaiprmPdf, name='myTaiprmPdf'),
    path('newFailureMode/<int:pk>',views.NewFailureMode,name='newFailureMode'),
    
    
    #path('<int:year>/<str:month>/',views.home), # this shows hot to use path converters. they are colled by <> and they are int: numbers, str:strings, path: whole urls, slug:hyphen-and-underscores stuff, UUID: universally unique identifier
    #path('events',views.all_events,name='events'),
    #path('add_venue',views.add_venue,name='add_venue'),
    #path('list_venues',views.list_venues,name='list_venues'),
    #path('show_venue/<venue_id>',views.show_venue, name='show_venue'),
    #path('search_venues',views.search_venue,name='search_venues'),
    #path('update_venue/<venue_id>',views.update_venue, name='update_venue'),
    #path('update_event/<event_id>',views.update_event, name='update_event'),
    #path('add_event',views.add_event,name='add_event'),
    #path('delete_event/<event_id>',views.delete_event,name='delete_event'),
    #path('delete_venue/<venue_id>',views.delete_venue,name='delete_venue'),
    #path('venue_text',views.venue_text,name='venue_text')


]


