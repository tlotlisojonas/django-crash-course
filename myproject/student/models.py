from django.db import models

# Create your models here.
class Learner(models.Model):
    name = models.CharField(max_length=200)
    age = models.DecimalField(max_digits=2,decimal_places=0)

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    subjects = [
        ('Eng','English'),
        ('Maths','Mathematics'),
        ('Physics','Physical Sciences'),
        ('LS','Life Sciences'),
        ('LO','Life Orientation')
    ]
    subject = models.CharField(max_length=200, choices=subjects, default='English')
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject    