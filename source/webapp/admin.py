from django.contrib import admin
from webapp.models import Poll, Choice

class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    exclude = []

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'variation', 'poll']
    exclude = []

admin.site.register(Poll)
admin.site.register(Choice)
