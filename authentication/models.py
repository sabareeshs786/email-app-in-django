import imp


import uuid
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class LoginDetails(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    emailid = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)

class SignUpDetails(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=254, null=False)
    last_name = models.CharField(max_length=254, null=False)
    username = models.CharField(max_length=254, null=False)
    phone_regex = RegexValidator(regex=r'^91\d{10}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    password = models.CharField(max_length=50, null=False)
    
    
