from django.db import models
from django.contrib.auth.models import User

class Geo_scope(models.Model):
    scope = models.CharField(max_length=255)

class Sector(models.Model):
    sector = models.CharField(max_length=255)

class Organization(models.Model):
    name = models.CharField(max_length=255)
    geo_scope = models.ForeignKey(Geo_scope,null=True)
    sectors = models.ManyToManyField(Sector)

class Organization_location(models.Model):
    organization = models.ForeignKey(Organization)
    primary = models.BooleanField(default=False) # record is org's main location
    country = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    county = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    street = models.CharField(max_length=255,null=True)
    postalcode = models.CharField(max_length=255,null=True)

class Organization_contact(models.Model):
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True)
    primary_phone = models.CharField(max_length=255,null=True)
    secondary_phone = models.CharField(max_length=255,null=True)

class Organization_comment(models.Model):
    organization = models.ForeignKey(Organization)
    user = models.ForeignKey(User)
    subject = models.CharField(max_length=255,null=True)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


