from django.contrib import admin
from .models import Board,Thread,Message

# @admin.register(Board)
# class BoardAdmin(admin.ModelAdmin):
# 	exclude=['TreadCount','MessageCount']


admin.site.register(Board)
admin.site.register(Thread)
admin.site.register(Message)

# @admin.register(Thread)
# class BoardAdmin(admin.ModelAdmin):
# 	exclude=['TreadCount','MessageCount']

# @admin.register(Message)
# class BoardAdmin(admin.ModelAdmin):
# 	exclude=['TreadCount','MessageCount']

