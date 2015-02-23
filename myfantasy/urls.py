from django.conf.urls import patterns, include, url
from myfantasy import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fantasy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name = 'index'),
    url(r'^test/$', views.test, name = 'test'),
    url(r'^player/(?P<player_id>\d+)/$', views.player_details, name = 'player_details'),
    url(r'^team/(?P<team_id>\d+)/$', views.team_details, name = 'team_details'),
    
)
