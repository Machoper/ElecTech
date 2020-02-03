from django import forms
from .models import *

class DriversLicenseForm(forms.Form):
	id_number = forms.CharField(label="DriversLicenseID", max_length=100)

class PassportForm(forms.Form):
	id_number = forms.CharField(label="PassportID", max_length=100)

class VoterIDForm(forms.Form):
	id_number = forms.CharField(label="VoterID", max_length=100)

class BallotForm(forms.Form):
	picked = forms.ModelMultipleChoiceField(queryset=Option.objects.all(), to_field_name="title")

class MyModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class QuestionForm(forms.Form):
	picked = MyModelMultipleChoiceField(queryset=None, widget=forms.RadioSelect)