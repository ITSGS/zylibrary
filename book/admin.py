# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from book.models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(CheckOut)
admin.site.register(Shelf)
admin.site.register(Comment)
admin.site.register(Rent)
admin.site.register(Note)
admin.site.register(FeedBack)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    site_order = 1
    list_display = ('name', 'desc', 'order_number', 'status')
    fields = ('name', 'desc', 'order_number', 'status')
