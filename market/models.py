from django.db import models

# Модель оружия, в полях модели всякие параметры из стима


class Weapon(models.Model):

	bot = models.ForeignKey('Bot', on_delete=models.CASCADE, null=True)
	steam_id = models.IntegerField()
	classid = models.IntegerField()
	instanceid = models.IntegerField()
	appid = models.IntegerField()
	tradable_after = models.TextField()
	exterior = models.CharField(max_length=200)
	icon_url = models.TextField()
	market_hash_name = models.CharField(max_length=200)
	market_name = models.CharField(max_length=200)
	marketable = models.IntegerField()
	name = models.CharField(max_length=200)
	tradable = models.IntegerField()
	type = models.CharField(max_length=200)

	def __str__(self):
		return self.name

# Модель бота маркета, содержащая данные логина, пароля, данных steam guard и апи ключ от стим


class Bot(models.Model):
	login = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	steam_guard_name = models.CharField(max_length=200)
	api_key = models.CharField(max_length=100)
	link = models.CharField(max_length=200, null='steam url')

	def __str__(self):
		return self.login
