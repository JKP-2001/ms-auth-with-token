from django.urls import path

from . import views
from django.urls import path
# from .views import TaskListView,TaskDetailView,TaskCreateView,TaskUpdateView,TaskDeleteView
from . import views

urlpatterns = [

  path('', views.home, name='home'),

  path('signin', views.sign_in, name='signin'),
  path('signout', views.sign_out, name='signout'),
  path('calendar', views.calendar, name='calendar'),
  path('mail', views.mail, name='mail'),
  path('callback', views.callback, name='callback'),
  path('calendar/new', views.newevent, name='newevent'),
  path('mails',views.mailing, name='mailing'),

]



