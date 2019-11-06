from authentication.models import SteamUser
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from steampy.client import SteamClient, InvalidCredentials
from steampy.utils import GameOptions
from .models import Bot, Weapon
import os


def bot_inventory():
	bot = Bot.objects.all()[0]
	API_KEY = bot.api_key
	LOGIN = bot.login
	PASSWORD = bot.password
	steam_guard_name = bot.steam_guard_name
	steam_guard_path = r'C:\Users\timag\Desktop\marketproj\csgotrademarket\market\steam_guard.txt'
	steam_client = SteamClient(API_KEY)
	try:
		steam_client.login(LOGIN, PASSWORD, steam_guard_path)
	except (ValueError, InvalidCredentials):
		print('Your login credentials are invalid')
		#exit(1)
	#print("Logged into steam")
	game = GameOptions.CS
	inv = steam_client.get_my_inventory(game)
	return inv


def user_inventory(request):
	bot = Bot.objects.all()[0]
	API_KEY = bot.api_key
	LOGIN = bot.login
	PASSWORD = bot.password
	steam_guard_name = bot.steam_guard_name
	steam_guard_path = r'C:\Users\timag\Desktop\marketproj\csgotrademarket\market\steam_guard.txt'
	steam_client = SteamClient(API_KEY)
	try:
		steam_client.login(LOGIN, PASSWORD, steam_guard_path)
	except (ValueError, InvalidCredentials):
		print('Your login credentials are invalid')
		#exit(1)
	#print("Logged into steam")
	game = GameOptions.CS
	inv = steam_client.get_partner_inventory(str(request.user.steamid), game)
	return inv


def get_bot_inventory():
	inv = bot_inventory()
	list_keys = list(inv.keys())
	for i in range(len(list_keys)):
		inv1 = inv[list_keys[i]]
		classid = inv1['classid']
		instanceid = inv1['instanceid']
		appid = inv1['appid']
		descriptions1 = inv1['descriptions']
		# descriptions = inv['descriptions'][2]

		exterior = descriptions1[0]['value'].split(' ')[1]
		icon_url = 'https://steamcommunity-a.akamaihd.net/economy/image/'+inv1['icon_url']
		market_hash_name = inv1['market_hash_name']
		market_name = inv1['market_name']
		marketable = inv1['marketable']
		name = inv1['name']
		type = inv1['type']
		tradable = inv1['tradable']
		tags = inv1['tags']
		steam_id = inv1['id']
		if int(tradable) == 0:
			try:
				tradable_after = inv1['owner_descriptions'][1]['value']
			except KeyError:
				tradable_after = 'null'
		else:
			tradable_after = '0'
		if Weapon.objects.filter(bot=Bot.objects.all()[0], classid=classid, appid=appid, instanceid=instanceid,
							  exterior=exterior, icon_url=icon_url, market_hash_name=market_hash_name, market_name=market_name,
							  name=name, type=type, marketable=marketable, steam_id=steam_id, tradable_after=tradable_after, tradable=tradable).exists():
			pass
		else:
			Weapon.objects.create(bot=Bot.objects.all()[0], classid=classid, appid=appid, instanceid=instanceid,
							  exterior=exterior, icon_url=icon_url, market_hash_name=market_hash_name, market_name=market_name,
							  name=name, type=type, marketable=marketable, steam_id=steam_id, tradable_after=tradable_after, tradable=tradable)
	return 0


def update_inventory(request):
	get_bot_inventory()
	return redirect('market:market_main')


@login_required
def get_user_inventory(request):
	ui = user_inventory(request)
	#ui = request.user.steamid
	return render(request, 'market/my_inv.html', {'bot': ui})


def market_main_view(request):
	weapons = Weapon.objects.all()
	item_list = []
	for weapon in weapons:
		item_list.append({'name': weapon.market_name, 'exterior': weapon.exterior, 'tradable': weapon.tradable_after, 'icon': weapon.icon_url})

	return render(request, 'market/main.html', {'bot': item_list})

