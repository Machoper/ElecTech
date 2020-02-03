# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

# Create your models here.
class Election(models.Model):
    # look into making custom primary keys
    election_id = models.CharField(max_length=30, null=False, primary_key=True)
    title = models.CharField(max_length=30, null=False)
    election_type = models.CharField(max_length=30, null=False)
    active = models.BooleanField(default=False)

    class Meta:
        db_table = 'election'

    def toJson(self):
        return dict(election_id = self.election_id,
                    title = self.title,
                    election_type = self.election_type)

class Ballot(models.Model):
    title = models.CharField(max_length=30, null=False)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, null=False)
    class Meta:
        db_table = 'ballot'

    def toJson(self):
        return dict(ballot_id = self.id,
                    title = self.title,
                    election = Election.toJson(self.election))

class Question(models.Model):
    question_type = models.CharField(max_length=30, null=False)
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000, null=False)
    votes = models.IntegerField(null=True, default=0)
    class Meta:
        db_table = 'question'

    def toJson(self):
        return dict(question_id = self.id,
                    question_type = self.question_type,
                    question_text = self.question_text,
                    votes = self.votes,
                    ballot = Ballot.toJson(self.ballot))

class Option(models.Model):
    title = models.CharField(max_length=30, null=False)
    party = models.CharField(max_length=30, null=True)
    running_mate = models.CharField(max_length=30, null=True)
    votes = models.IntegerField(null=True, default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    class Meta:
        db_table = 'option'

    def toJson(self):
        return dict(option_id = self.id,
                    title = self.title,
                    party = self.party,
                    running_mate = self.running_mate,
                    votes = self.votes,
                    question = Question.toJson(self.question))

class Profile(models.Model):
    voter_number = models.CharField(max_length=30, null=False, default="0")
    voter_status = models.CharField(max_length=30, null=False, default="inactive")
    date_registered = models.DateField(default=now)
    address = models.CharField(max_length=50, null=True)
    county = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    zip_code = models.CharField(max_length=30, null=True)
    locality = models.CharField(max_length=30, null=True)
    precinct = models.CharField(max_length=30, null=True)
    precinct_id = models.CharField(max_length=4, null=True)

    signed_in = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    class Meta:
        db_table = 'voter'

    def toJson(self):
        return dict(voter_id = self.user.username,
                    voter_number = self.voter_number,
                    voter_status = self.voter_status,
                    date_registered = self.date_registered,
                    last_name = self.user.last_name,
                    first_name = self.user.first_name,
                    address = self.address,
                    county = self.county,
                    state = self.state,
                    zip_code = self.zip_code,
                    locality = self.locality,
                    precinct = self.precinct,
                    precinct_id = self.precinct_id)


class Vote(models.Model):
    voter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE)

    @classmethod
    def create(cls, voterId, ballotId):
        newVoter = Profile.objects.get(id=voterId)
        newBallot = Ballot.objects.get(id=ballotId)

        vote = cls(voter=newVoter, ballot=newBallot)

        return vote

    # validate uniquess of voter and ballot (voter can only vote for Ballot once)
    class Meta:
        unique_together = ('voter', 'ballot',)
        db_table = 'vote'

    def toJson(self):
        return dict(vote_id = self.id,
                    voter = Profile.toJson(self.voter),
                    ballot = Ballot.toJson(self.ballot))

############### ADDED BY JOHN AND CONNOR ON 4-29-2018 ############################
class Measure(models.Model):
    precinct_id = models.CharField(max_length=4, null=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(null=True, default=0)
    
    class Meta:
        db_table = 'measure'

    def toJson(self):
        return dict(precinct_id = self.precinct_id,
                    option = self.option,
                    votes = self.votes,
                    question = self.question)
##################################################################################
    
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Queue(models.Model):
    title = models.CharField(max_length=30, null=False)
    party = models.CharField(max_length=30, null=True)
    running_mate = models.CharField(max_length=30, null=True)
    question_text = models.CharField(max_length=1000, null=False, default="No question")
    class Meta:
        db_table = 'queue'

    def toJson(self):
        return dict(queue_id = self.id,
                    title = self.title,
                    party = self.party,
                    running_mate = self.running_mate,
                    question_text = self.question_text)
      
# class Measure(models.Model):
#     precinct_id = models.CharField(max_length=4, null=True)
#     option = models.ForeignKey(Option, on_delete=models.CASCADE)
#     votes = models.IntegerField(null=True, default=0)
    
#     class Meta:
#         db_table = 'measure'
