# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class SD_Creation(models.Model):
	name = models.CharField(max_length=100,blank=True,null=True)
	creation_name = models.CharField(max_length=100,blank=True,null=True)


class MD_Creation(models.Model):
	name = models.CharField(max_length=100,blank=True,null=True)
	creation_date = models.CharField(max_length=100,blank=True,null=True)
