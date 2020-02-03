# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.core import serializers
#from escpos.printer import Usb
from myapp.models import *
from .forms import *
from .models import *

##########################################################################
################################API WORK##################################
##########################################################################
def getElections(request):
    x = request.GET.get('key', '0')
    if (x == "electech"):
        data = "{ \"status\" : \"200\", " + serializers.serialize("json", Election.objects.all())

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"
    return HttpResponse(data)
### 

def getBallots(request):
    x = request.GET.get('key', '0')
    if (x == "electech"):
        data = "{ \"status\" : \"200\", " + serializers.serialize("json", Ballot.objects.all())

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"
    return HttpResponse(data)

def getResultsByElection(request, e_id):
  ballots = Ballot.objects.filter(election_id=e_id)
  votingOptions = []
  for ballot in ballots:
    questions = Question.objects.filter(ballot_id=ballot.id)
    for question in questions:
      options = Option.objects.filter(question_id=question.id)
      for option in options:
        votingOptions.append(option)

  x = request.GET.get('key', '0')
  if (x == "electech"):

    if (len(votingOptions) == 0):
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid Election ID Provided\" }"
    else:
        data = "{ \"status\" : \"200\", " + serializers.serialize("json", votingOptions)

  else:
      data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"
  return HttpResponse(data)


def getBallotsByElection(request, e_id):
    x = request.GET.get('key', '0')
    if (x == "electech"):

        ballots = Ballot.objects.filter(election_id=e_id)
        if (len(ballots) == 0):
            data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid Election ID Provided\" }"
        else:
            data = "{ \"status\" : \"200\", " + serializers.serialize("json", ballots)

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"
    return HttpResponse(data)


def getElectionByID(request, e_id):
    x = request.GET.get('key', '0')
    if (x == "electech"):

        oneElection = Election.objects.filter(election_id=e_id)
        if (len(oneElection) == 0):
            data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid Election ID Provided\" }"
        else:
            data = "{ \"status\" : \"200\", " + serializers.serialize("json", oneElection)

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"
    return HttpResponse(data)
###

def getVoters(request):
    voters = Profile.objects.all()

    x = request.GET.get('key', '0')
    if (x == "electech"):
        data = "{ \"status\" : \"200\", " + serializers.serialize("json", voters)

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"
    return HttpResponse(data)
###

def getPollingSiteByPrecinctID(request, p_id):
    votersByPrecinctID = Profile.objects.filter(precinct_id=p_id)

    x = request.GET.get('key', '0')
    if (x == "electech"):

        if (len(votersByPrecinctID) == 0):
            data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid Precinct ID Provided\" }"
        else:
            data = "{ \"status\" : \"200\", " + serializers.serialize("json", votersByPrecinctID)

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"

    return HttpResponse(data)
###


def getTotalVotes(request):
    numvotes = Option.objects.all()

    x = request.GET.get('key', '0')
    if (x == "electech"):
        data = "{ \"status\" : \"200\", " + serializers.serialize("json", numvotes)

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"
    return HttpResponse(data)
###

def getVotesByQuestion(request, q_id):
    numvotes = Option.objects.filter(question = q_id)

    x = request.GET.get('key', '0')
    if (x == "electech"):

        if (len(numvotes) == 0):
            data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid Question ID Provided\" }"
        else:
            data = "{ \"status\" : \"200\", " + serializers.serialize("json", numvotes)

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"

    return HttpResponse(data)
###

def getVotesByParty(request, party_id):
    numvotes = Option.objects.filter(party = party_id)

    x = request.GET.get('key', '0')
    if (x == "electech"):

        if (len(numvotes) == 0):
            data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid Party ID Provided\" }"
        else:
            data = "{ \"status\" : \"200\", " + serializers.serialize("json", numvotes)

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"

    return HttpResponse(data)
###

def getProfile(request):
    temp = Profile.objects.all()

    x = request.GET.get('key', '0')
    if (x == "electech"):
        data = "{ \"status\" : \"200\", " + serializers.serialize("json", temp)

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"
    return HttpResponse(data)
###

############### ADDED BY JOHN AND CONNOR ON 4-29-2018 ############################
def getResultsByPrecinctID(request, p_id):
    measuresByPrecinctID = Measure.objects.filter(precinct_id=p_id)

    x = request.GET.get('key', '0')
    if (x == "electech"):

        if (len(measuresByPrecinctID) == 0):
            data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid Precinct ID Provided\" }"
        else:
            data = "{ \"status\" : \"200\", " + serializers.serialize("json", measuresByPrecinctID)

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"

    return HttpResponse(data)
###

def getResultsByPrecinctAndQuestion(request, p_id, q_id):
    measuresByQuestion = Measure.objects.filter(question=q_id)
    measuresByBoth = measuresByQuestion.filter(precinct_id=p_id)

    x = request.GET.get('key', '0')
    if (x == "electech"):
        data = "{ \"status\" : \"200\", " + serializers.serialize("json", measuresByBoth)

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"

    return HttpResponse(data)
###
##############################################################################



def printer(request):

    x = request.GET.get('key', '0')
    if (x == "electech"):
        data = serializers.serialize("json", Queue.objects.all())
        Queue.objects.all().delete()

    else:
        data = "{ \"status\" : \"404\", \"status_message\" : \"Invalid API Key Provided\" }"
    return HttpResponse(data)

###

##########################################################################
##########################################################################
##########################################################################

# Create your views here.
def index(request):
    activeElection = Election.objects.get(active = True)

    return render(request, "index.html", {'activeElection': activeElection})

def user(request, userId):
    template = loader.get_template("user.html")
    return HttpResponse(template.render())
#   return HttpResponse("Displaying user %s"%userId) #would use userId to display said users page

def ballot(request, activeElection, ballotNum):
    # check user is authenticated
    if request.user.is_authenticated:
        # check that selected election is active
        selectedElection = Election.objects.get(election_id = activeElection)
        if (selectedElection.active):
            # check that selected ballot is associated with active election
            selectedBallot = Ballot.objects.get(id = ballotNum)
            if selectedBallot.election_id == activeElection:
                if request.method == 'POST':
                    form = BallotForm(request.POST)
                    questionList = [q.toJson() for q in Question.objects.filter(ballot=ballotNum)]
                    for question in questionList:
                        question["options"] = [option.toJson() for option in Option.objects.filter(question=question["question_id"])]
                else:
                    form = BallotForm()
                    questionList = [q.toJson() for q in Question.objects.filter(ballot=ballotNum)]
                    for question in questionList:
                        question["options"] = [option.toJson() for option in Option.objects.filter(question=question["question_id"])]
                return render(request, "ballot.html", {"questionList": questionList, "form": form})

            else:
                return render(request, "404.html")
        else:
            return render(request, "404.html")
    else:
        return redirect('/login/')
    # template = loader.get_template("ballot.html")
    # return HttpResponse(template.render())

def ballotlist(request, activeElection):
    if request.user.is_authenticated:
        if Profile.objects.get(user=request.user).signed_in == False:
            messages.error(request, 'Please check in first!')
            logout(request)
            return redirect('/login/')
            #message = "Please check in first!"
            #return render(request, "./registration/login.html", {'message': message, 'form': AuthenticationForm()})
        selectedElection = Election.objects.get(election_id = activeElection)
        if (selectedElection.active):
            ballotList = Ballot.objects.filter(election_id = activeElection)
            return render(request, "ballotlist.html", {'ballotList': ballotList})
        else:
            return render(request, "404.html")
    else:
        return redirect('/login/')

def postVote(request, activeElection, ballotNum):
    if request.user.is_authenticated:
        selectedElection = Election.objects.get(election_id = activeElection)
        if (selectedElection.active):
            votedOptions = []
            # check that selected ballot is associated with active election
            selectedBallot = Ballot.objects.get(id = ballotNum)
            if selectedBallot.election_id == activeElection:
                if request.method == "POST":
                    for key, value in request.POST.items():
                        try:
                            question_id = int(key)
                            option_id = int(value)
                            voted = {}
                            voted["option"] = Option.objects.get(id = option_id)
                            voted["question"] = Question.objects.get(id = question_id)
                            votedOptions.append(voted)
                        except ValueError:
                            continue
                return render(request, "verifyvote.html", {'votedOptions': votedOptions})
            else:
               return render(request, "404.html") 
        else:
            return render(request, "404.html")
    else:
        return redirect('/login/')

def voted(request, activeElection, ballotNum):
    if request.user.is_authenticated:
        selectedElection = Election.objects.get(election_id = activeElection)
        if (selectedElection.active):
            # check that selected ballot is associated with active election
            selectedBallot = Ballot.objects.get(id = ballotNum)
            if selectedBallot.election_id == activeElection:
                if request.method == "POST":
                    try:
                        # create vote instance to eliminate voting twice
                        vote = Vote.create(request.user.profile.id, ballotNum)
                        vote.save()
                        for key, value in request.POST.items():
                            try:
                                option_id = int(value)
                                votedOption = Option.objects.get(id=option_id)     
                                # update measure
                                measure = Measure.objects.filter(option_id=option_id).get(precinct_id=request.user.profile.precinct_id)
                                measure.votes += 1
                                measure.save()
                                # update voted option
                                votedOption.votes += 1
                                votedOption.save()
                                # update total vote of question
                                votedQuestion = Question.objects.get(id=votedOption.question_id)
                                votedQuestion.votes += 1
                                votedQuestion.save()
                                printed = Queue(title=votedOption.title, party=votedOption.party, running_mate=votedOption.running_mate, question_text=votedOption.question.question_text)
                                printed.save()
                            except ValueError:
                                continue
                    except Exception as e:
                        instance = Profile.objects.get(user=request.user)
                        instance.signed_in = False
                        instance.save()
                        logout(request)
                        return render(request, "400.html")
                    instance = Profile.objects.get(user=request.user)
                    instance.signed_in = False
                    instance.save()
                    logout(request)
                    return redirect('/login/')
            else:
                return render(request, "404.html")
        else:
            return render(request, "404.html")
    else:
        return redirect('/login/')

def changeVote(element):
    print(element)

def checkin(request):
    if request.method == 'POST':
        form = VoterIDForm(request.POST)
        activeElection = Election.objects.get(active = True)
        if form.is_valid():
            voter_number = form.cleaned_data['id_number']
            try:
                instance = Profile.objects.get(voter_number=voter_number)
            except Profile.DoesNotExist:
                # return HttpResponse("lll")
                message = "Invalid voter ID provided"
                return render(request, "checkin.html", {'form': VoterIDForm(), 'activeElection': activeElection, 'message': message})
            if instance.precinct_id != "0201":
                message = "You are at the wrong voting site!"
                return render(request, "checkin.html", {'form': VoterIDForm(), 'activeElection': activeElection, 'message': message})
            # return HttpResponse(instance)
            instance.signed_in = True
            instance.save()
            message = "You have successfully checked in! Please proceed to the voting booth."
            return render(request, "checkin.html", {'form': VoterIDForm(), 'activeElection': activeElection, 'message': message})
    else:
        form = VoterIDForm()
        activeElection = Election.objects.get(active = True)
        return render(request, "checkin.html", {'form': form, 'activeElection': activeElection})


def worker(request):
    template = loader.get_template("worker.html")
    return HttpResponse(template.render())

def workerLogin(request):
    activeElection = Election.objects.get(active = True)

    return render(request, "workerLogin.html", {'activeElection': activeElection})
    
def export(request):        
    template = loader.get_template("export.html")       
    return HttpResponse(template.render())

def confirmation(request):      
    template = loader.get_template("confirmation.html")     
    return HttpResponse(template.render())      
    
def completed(request):     
    template = loader.get_template("completed.html")        
    return HttpResponse(template.render())      
        
def success(request):       
    template = loader.get_template("success.html")      
    return HttpResponse(template.render())      
        
def election(request):      
    template = loader.get_template("election.html")     
    return HttpResponse(template.render())
        
 #def printer(request):     
 #    p = Usb(0x0416, 0x5011, 0, 0x81, 0x01)        
 #    p.text('Hello World\n')       
 #      
 #    return HttpResponse("Success")        
        
def docs(request):
    template = loader.get_template("api_docs.html")
    return HttpResponse(template.render()) 
