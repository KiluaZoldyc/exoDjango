# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Categorie, Article
from django.contrib import admin

# Register your models here.

admin.site.register(Categorie)

admin.site.register(Article)
