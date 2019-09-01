from __future__ import unicode_literals
from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def basic_validator(self, postData):
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PW_REGEX = re.compile(
            r'^(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$')
        
        errors = {}

        if len(postData['FirstName'].strip()) < 1 or not postData['FirstName'].isalpha():
            errors['FirstName'] = "Required & letters only"

        if len(postData['LastName'].strip()) < 1 or not postData['LastName'].isalpha():
            errors['LastName'] = "Required & letters only"
        
        if len(postData['DisplayName'].strip()) < 1:
            errors['DisplayName'] = "Required"

        if len(postData['DisplayName'].strip()) > 15:
            errors['DisplayName'] = "Please keep your Display Name under 15 characters"

        if not EMAIL_REGEX.match(postData['Email']):
            errors['Email'] = "You must provide a valid email"

        if User.objects.filter(email=postData['Email']):
            errors['Email'] = "This email is already registered"

        if not PW_REGEX.match(postData['Password']):
            errors['Password'] = "Password must be at least 8 characters in length and contain at least 1 uppercase letter, 1 lower case letter & at least 1 number or special character"

        if not postData['Password'] == postData['Confirm']:
            errors['Confirm'] = "Passwords do not match"

        # print(f"***************************** {errors} from model.py")
        return errors

    def validate_login(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['LoginEmail'].lower())
        print('%' * 30)

        if not (user and bcrypt.checkpw(postData['LoginPassword'].encode(), user[0].password.encode())):
            errors['Login'] = "Invalid email or password"

        return errors

    def validate_firstName(self, postData):
        errors = {}
        if len(postData['FirstName'].strip()) < 1 or not postData['FirstName'].isalpha():
            errors['FirstName'] = "Required & letters only"
        return errors
    
    def validate_lastName(self, postData):
        errors = {}
        if len(postData['LastName'].strip()) < 1 or not postData['LastName'].isalpha():
            errors['LastName'] = "Required & letters only"
        return errors

    def validate_email(self, postData):
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        errors = {}

        if not EMAIL_REGEX.match(postData['Email']):
            errors['Email'] = "You must provide a valid email"

        if User.objects.filter(email=postData['Email']):
            errors['Email'] = "This email is already registered"
        
        return errors

    def validate_displayChange(self, postData):
        errors = {}
        print(len(postData['DisplayName'].replace(" ", "")))
        if len(postData['DisplayName'].replace(" ", "")) > 15:
            errors['DisplayName'] = "Please keep your Display Name under 15 characters"

        if len(postData['DisplayName'].replace(" ", "")) <= 0:
            errors['DisplayName'] = "Required"

        
        return errors

    def validate_pwChange(self, postData):
        PW_REGEX = re.compile(
            r'^(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$')

        errors = {}
        
        if not PW_REGEX.match(postData['Password']):
            errors['Password'] = "Password must be at least 8 characters in length and contain at least 1 uppercase letter, 1 lower case letter & at least 1 number or special character"

        if not postData['Password'] == postData['Confirm']:
            errors['Confirm'] = "Passwords do not match"

        return errors

    

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    displayname = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
