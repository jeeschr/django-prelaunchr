from django.conf.urls import patterns, url, include
from . import views
from .views import *

urlpatterns = patterns('',

	# social contest prelaunch page
	url(r'^$', views.contest_landing_page),
	url(r'^submit/$', createUser.as_view()),
	url(r'^share/$', views.thanks_share_us, name='thanks-share-us'),
	url(r'^(?P<ref>[0-9a-zA-Z]+)/$', views.contest_landing_page),

)



