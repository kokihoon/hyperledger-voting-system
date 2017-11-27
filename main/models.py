from django.db import models

class UserCheck(models.Model):
    user = models.ForeignKey('auth.User')
