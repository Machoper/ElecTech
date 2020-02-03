"""vote_tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from myapp import views as v
1
urlpatterns = [
    #admin page
    #path('admin/', admin.site.urls),

    #start of login session
    #path('index/', v.index),
    #path('login/', auth_views.login, name='login'),
    #path('login/success', v.success, name='success'), #create success in views
    #end of login session

    #start of voting session
    #path('<slug: election>/', v.election, name='Welcome-Voter'), #election in views?
    #path('<slug: election>/ballotlist/', v.ballotlist, name='ballotlist'),
    #path('<slug: election>/ballotlist/ballot/<int: ballotNum>/', v.ballot, name='ballot'),
    #path('<slug: election>/ballotlist/ballot/<int: ballotNum>/confirmation/', v.confirmation, name='confirmation'), #create confirmation in views
    #path('<slug: election>/ballotlist/ballot/<int: ballotNum>/completed/', v.completed, name='completed'), #create completed in views
    #end of voting session

    #worker page
    #path('worker/', v.worker, name='worker'),
    #path('help/', v.help, name='help'),

    #url(r'^test/(?P<key>[0-9]{4})/$', v.test),

   
    url(r'^admin/', admin.site.urls),
    url(r'^$', v.index),

    url(r'^(?P<activeElection>.+)/ballot/(?P<ballotNum>\d+)/verify/voted/$', v.voted, name='voted'),
    url(r'^(?P<activeElection>.+)/ballot/(?P<ballotNum>\d+)/verify/$', v.postVote, name='postVote'),
    url(r'^(?P<activeElection>.+)/ballot/(?P<ballotNum>\d+)/$', v.ballot, name='ballot'),
    url(r'^(?P<activeElection>.+)/ballot/$', v.ballotlist, name='ballotlist'),
    url(r'^docs/', v.docs, name='docs'),

 #    url(r'^test/$', v.test, name = 'test'),	
	# url(r'^test/(?P<e_id>(\d+-\d+))/$', v.testElectionID, name='testElectionID'),

    ############ API ###################
    url(r'^elections/$', v.getElections, name='getElections'),
    url(r'^ballots/$', v.getBallots, name='getBallots'),
    url(r'^(?P<e_id>.+)/results/', v.getResultsByElection, name='getResultsByElection'),
    url(r'^(?P<e_id>.+)/ballots/', v.getBallotsByElection, name='getBallotsByElection'),
    url(r'^elections/(?P<e_id>.+)/$', v.getElectionByID, name='getElectionByID'),
    url(r'^voters/$', v.getVoters, name='getVoters'),
    url(r'^pollingsite/(?P<p_id>(\w+))/$', v.getPollingSiteByPrecinctID, name='getPollingSiteByPrecinctID'),
    url(r'^votes/$', v.getTotalVotes, name='getTotalVotes'),
    url(r'^votes/party/(?P<party_id>.+)/$', v.getVotesByParty, name='getVotesByParty'),
    url(r'^votes/question/(?P<q_id>(\w+))/$', v.getVotesByQuestion, name='getVotesByQuestion'),
    url(r'^profile/', v.getProfile, name='getProfile'),

    ############### ADDED BY JOHN AND CONNOR ON 4-29-2018 ############################
    url(r'^results/(?P<p_id>(\w+))/$', v.getResultsByPrecinctID, name='getResultsByPrecinctID'),
    url(r'^results/(?P<p_id>(\w+))/(?P<q_id>(\w+))/$', v.getResultsByPrecinctAndQuestion, name='getResultsByPrecinctAndQuestion'),
    ##################################################################################
 
    ####################################
	
    url(r'^user/(\d+)/$', v.user, name='user'),
    url(r'^worker/', v.worker, name='worker'),
    url(r'^workerLogin/', v.workerLogin, name='workerLogin'),
    url(r'^export/$', v.export, name='export'),
    url(r'^checkin/$', v.checkin, name='checkin'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^printer/', v.printer, name='printer'),
]
