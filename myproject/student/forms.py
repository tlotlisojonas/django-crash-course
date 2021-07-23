from django.forms import ModelForm
from .models import Subject, Learner

class SubjectRegistrationForm(ModelForm):
   class Meta:
       model = Subject
       fields = ['subject']

class LearnerRegistrationForm(ModelForm):
   class Meta:
       model = Learner
       fields = ['name','age']       