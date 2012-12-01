from django.db import models

class Geo_scope(models.Model):
    scope = models.CharField(max_length=255)

class Sector(models.Model):
    sector = models.CharField(max_length=255)

class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Organization(models.Model):
    name = models.CharField(max_length=255)
    geo_scope = models.ForeignKey(Geo_scope)

class Organization_sector(models.Model):
    organization = models.ForeignKey(Organization)
    sector = models.ForeignKey(Sector)

class Organization_location(models.Model):
    organization = models.ForeignKey(Organization)
    primary = models.BooleanField() # record is org's main location
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=255)

class Organization_contact(models.Model):
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    primary_phone = models.CharField(max_length=255)
    secondary_phone = models.CharField(max_length=255)

class Organization_comment(models.Model):
    organization = models.ForeignKey(Organization)
    user = models.ForeignKey(User)
    subject = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


