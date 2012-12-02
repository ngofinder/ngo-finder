from django.db import models
from django.contrib.auth.models import User

class Geo_scope(models.Model):
    scope = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.scope

class Sector(models.Model):
    sector = models.CharField(max_length=255)

    def __unicode__(self):
        return self.sector

class Organization(models.Model):
    name = models.CharField(max_length=255)
    geo_scope = models.ForeignKey(Geo_scope,null=True)
    sectors = models.ManyToManyField(Sector)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Location(models.Model):
    organization = models.ForeignKey(Organization)
    primary = models.BooleanField(default=False) # record is org's main location
    url = models.CharField(max_length=255)
    country = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    county = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    street = models.CharField(max_length=255,null=True)
    postalcode = models.CharField(max_length=255,null=True)

    def __unicode__(self):
        if self.city:
            return ','.join(self.country,self.state,self.county,self.city)
        else:
            return ','.join(self.country,self.state,self.county)

class Operation(models.Model):
    organization = models.ForeignKey(Organization)
    countries = models.TextField(null=True)
    states = models.TextField(null=True)
    counties = models.TextField(null=True)
    cities = models.TextField(null=True)

    def __unicode__(self):
        return 'Op #'+self.pk

class Contact(models.Model):
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True)
    primary_phone = models.CharField(max_length=255,null=True)
    secondary_phone = models.CharField(max_length=255,null=True)
    
    def __unicode__(self):
        return self.name

class Comment(models.Model):
    organization = models.ForeignKey(Organization)
    user = models.ForeignKey(User)
    subject = models.CharField(max_length=255,null=True)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


