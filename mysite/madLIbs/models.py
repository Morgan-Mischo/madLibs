from django.db import models

# Create your models here.


class Profile(models.Model):
    noun_plural = models.CharField(max_length=200)
    noun = models.CharField(max_length=200)
    animal = models.CharField(max_length=200)
    verb_base_form = models.CharField(max_length=200)
    noun_2 = models.CharField(max_length=200)
    verb_base_form_2 = models.CharField(max_length=200)
    noun_3 = models.CharField(max_length=200)
    noun_4 = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)
    story_type = models.CharField(max_length=200, default='story1')
