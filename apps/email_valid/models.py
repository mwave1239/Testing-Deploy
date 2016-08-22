from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class EmailManager(models.Manager):
    def register(self, email):
        errors = []
        if len(email) == 0:
            errors.append("Email cannot be blank")
        elif not EMAIL_REGEX.match(email):
            errors.append("Email not valid")
        if len(errors) is not 0:
            return (False, errors)
        else:
            e = Email.email_mgr.create(email=email)
            e.save()
            return (True, e)

    def destroy(self, id):
        e = Email.email_mgr.get(id=id)
        if not e:
            return (False, "Email doesn't exist")
        else:
            e.delete()
            return (True, "Email removed")

class Email(models.Model):
    email = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    email_mgr = EmailManager()
