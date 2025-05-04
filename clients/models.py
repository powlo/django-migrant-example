from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.ForeignKey("clients.Company", on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=100)
