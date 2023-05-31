from django.db import models

# Create your models here.

class WorkImage(models.Model):

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    source = models.URLField(max_length=250) 

    # Following code is to avoid the UnorderedObjectListWarning
    class Meta:
        ordering = ['id']

    # to show the name (string format) of Work Image in admin
    def __str__(self):
        return self.name

class ServiceImage(models.Model):

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    source = models.URLField(max_length=250) 

    # Following code is to avoid the UnorderedObjectListWarning
    class Meta:
        ordering = ['id']

    # to show the name (string format) of Service Image in admin
    def __str__(self):
        return self.name

class OtherImage(models.Model):

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    source = models.URLField(max_length=250) 

    # Following code is to avoid the UnorderedObjectListWarning
    class Meta:
        ordering = ['id']

    # to show the name (string format) of Service Image in admin
    def __str__(self):
        return self.name

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)
    
    # Following code is to avoid the UnorderedObjectListWarning
    class Meta:
        ordering = ['id']

    # to show the name (string format) of Enquiry (user who made enquiry)
    # in admin        
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    work_desc = models.CharField(max_length=100)
    
    # Following code is to avoid the UnorderedObjectListWarning
    class Meta:
        ordering = ['id']

    # to show the name (string format) of Client in admin        
    def __str__(self):
        return self.name

