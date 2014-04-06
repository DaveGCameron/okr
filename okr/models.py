from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    #logo = TODO: we need an image field here

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    #profile = TODO: we need an image field here
    company = models.ForeignKey('Company')

    def __unicode__(self):
        return self.name


class Period(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    start_date = models.DateField()
    end_date = models.DateField()


#class Objective(models.Model):
#    pass


#class KeyResult(models.Model):
#    pass
