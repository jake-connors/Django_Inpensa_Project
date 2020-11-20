from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from django.contrib.auth.models import User


class dataset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    #docfile = models.FileField(default=None)
    budget = models.FloatField(null = True)
    size = models.IntegerField(null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class data(models.Model):
    dsid = models.ForeignKey(dataset, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    TCO =models.FloatField(null = True)
    TVO =models.FloatField(null = True)
    NET =models.FloatField(null = True)
    PP =models.FloatField(null = True)
    ROI =models.FloatField(null = True)
    CapEx =models.FloatField(null = True)
    OneTime =models.FloatField(null = True)
    OnGoing =models.FloatField(null = True)
    Revenue =models.FloatField(null = True)
    Saving =models.FloatField(null = True)
    Avoid =models.FloatField(null = True)
    CostGrade =models.FloatField(null = True)
    ValueScore =models.FloatField(null = True)
    RiskScore =models.FloatField(null = True)
    BlendedScore =models.FloatField(null = True)
    CalcPriority =models.FloatField(null = True)
    OverridedPriority =models.IntegerField()
    accepted = models.IntegerField(1)

    def __dataset__(self):
        return self.dsid


class model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name =  models.CharField(max_length=50)
    kfile = models.FileField()
    numOfFeatures = models.IntegerField(2)
    TCO = models.IntegerField(1)
    TVO = models.IntegerField(1)
    NET =models.IntegerField(1)
    PP =models.IntegerField(1)
    ROI =models.IntegerField(1)
    CapEx =models.IntegerField(1)
    OneTime =models.IntegerField(1)
    OnGoing =models.IntegerField(1)
    Revenue =models.IntegerField(1)
    Saving =models.IntegerField(1)
    Avoid =models.IntegerField(1)
    CostGrade =models.IntegerField(1)
    ValueScore =models.IntegerField(1)
    RiskScore =models.IntegerField(1)
    BlendedScore =models.IntegerField(1)
    CalcPriority =models.IntegerField(1)
    OverridedPriority =models.IntegerField(1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class prediction(models.Model):
    did = models.ForeignKey(data, on_delete=models.CASCADE)
    mid = models.ForeignKey(model, on_delete=models.CASCADE)
    dsid = models.ForeignKey(dataset, on_delete=models.CASCADE)
    score = models.FloatField()
    def __float__(self):
        return self.score
