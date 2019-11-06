from django.contrib import admin
from .models import Bot, Weapon


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
	list_display = ('login', 'password', 'api_key', 'link')


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
	list_display = ('market_hash_name', 'exterior', 'type', 'bot')
