# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#Model for Questions
class Question(models.Model):
    title = models.CharField(max_length=30)
    subject = models.ForeignKey(
        'Subject',
        models.SET_NULL,
        blank=True,
        null=True,
    )
    subcategory = models.ForeignKey(
        'SubCategory',
        models.SET_NULL,
        blank=True,
        null=True,
    )
    question = models.CharField(max_length=40)
    option1 = models.CharField(max_length=40, blank=True)
    option2 = models.CharField(max_length=40, blank=True)
    option3 = models.CharField(max_length=40, blank=True)
    option4 = models.CharField(max_length=40, blank=True)
    correctanswer = models.CharField(max_length=60)
    help1 = models.CharField(max_length=300)
    help2 = models.CharField(max_length=300)
    help3 = models.CharField(max_length=300)
    figure1 = models.CharField(max_length=30, blank=True)
    figure2 = models.CharField(max_length=30, blank=True)
    def __unicode__(self):
        return self.title

class Subject(models.Model):
    title = models.CharField(max_length=30)
    def __unicode__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=30)
    subject = models.ForeignKey(
        'Subject',
        models.SET_NULL,
        blank=True,
        null=True,
    )
    def __unicode__(self):
        return self.title
