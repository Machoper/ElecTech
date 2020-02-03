# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from django.core import serializers
from myapp.models import *
from .forms import *
from .models import *

# Test for JSON serializer
def getElections(request):
    data = serializers.serialize("json", Election.objects.all())
    #template = loader.get_template("test.html")
    #return HttpResponse(template.render())
    return HttpResponse(data)

def getElectionByID(request, e_id):
    allElections = Election.objects.all()
    print(type(allElections))
    oneElection = Election.objects.filter(id_label=e_id)
    # oneElection = Election.objects.filter(id_label="2019-11")
    print(type(e_id))
    # print("self: " + str(self))
    print("request: " + str(request))
    print("e_id: " + e_id)
    # oneElection = Election.objects.filter(pk=e_id)
    # oneElection = Election.objects.filter(id_label=e_id)
    print(type(oneElection))
    data = serializers.serialize("json", oneElection)
    # dataAllElections = serializers.serialize("json", allElections);
    # return HttpResponse(data)
    return HttpResponse(data)

# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def user(request, userId):
    template = loader.get_template("user.html")
    return HttpResponse(template.render())
#   return HttpResponse("Displaying user %s"%userId) #would use userId to display said users page

def ballot(request, userId, ballotNum):
    # if request.method == 'POST':
    #     form = BallotForm(request.POST)
    #     questionList = [q.toJson() for q in Question.objects.filter(ballot=ballotNum)]
    #     for question in questionList:
    #         question["options"] = [option.toJson() for option in Option.objects.filter(question=question["question_id"])]
    # else:
    #     form = BallotForm()
    #     questionList = [q.toJson() for q in Question.objects.filter(ballot=ballotNum)]
    #     for question in questionList:
    #         question["options"] = [option.toJson() for option in Option.objects.filter(question=question["question_id"])]

    formset = []
    questionList = [q.toJson() for q in Question.objects.filter(ballot=ballotNum)]
    for question in questionList:
        form = QuestionForm()
        form.fields["picked"].queryset = Option.objects.filter(question=question["question_id"])
        form.fields["picked"].label = question["question_text"]
        formset.append(form)
        question["options"] = [option.toJson() for option in Option.objects.filter(question=question["question_id"])]
    return render(request, "ballot.html", {"questionList": questionList, "form": formset})

def ballotlist(request, activeElection):
    ballotList = Ballot.objects.filter(election_id = activeElection)
    return render(request, "ballotlist.html", {'ballotList': ballotList})

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())

def worker(request):
    template = loader.get_template("worker.html")
    return HttpResponse(template.render())

def help(request):
    template = loader.get_template("help.html")
    return HttpResponse(template.render())

def export(request):
    template = loader.get_template("export.html")
    return HttpResponse(template.render())

def help(request):
    template = loader.get_template("help.html")
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
