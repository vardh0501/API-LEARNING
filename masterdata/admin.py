# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from masterdata.models import SD_Creation, MD_Creation

# Register your models here.
class SD_CreationAdmin(admin.ModelAdmin):
	list_display = ('name','creation_name')


admin.site.register(SD_Creation,SD_CreationAdmin)
admin.site.register(MD_Creation)