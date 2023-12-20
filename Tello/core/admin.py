from django.contrib import admin
from core.models import *

admin.site.register([Product, Category, Comment, Image, ProductVersion, FAQ,])
