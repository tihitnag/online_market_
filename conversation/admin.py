from django.contrib import admin
from .models import Conversation,ConvesationMessage
# Register your models here.
admin.site.register(Conversation)
admin.site.register(ConvesationMessage)