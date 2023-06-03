from django.db import models


class Form(models.Model):
    name = models.TextField()
    question = models.TextField()
