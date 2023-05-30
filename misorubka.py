import telebot
import configparser
import os.path
import hashlib
import requests
from telebot import types  # для указание типов
проверка='бот'
token = '6124334077:AAFYIRDGvAYKZmbZzuCmTVgG7Z0xkUeI__s'
bot = telebot.TeleBot(token)
######кнопки#####
####меню
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Меню")
markup.add(btn1)
###меню1
meny = types.ReplyKeyboardMarkup(resize_keyboard=True)
men1 = types.KeyboardButton("Шаурма")
men2 = types.KeyboardButton("Шашлык")
men3 = types.KeyboardButton("Лапша")
men4 = types.KeyboardButton("Корзина")
men5 = types.KeyboardButton("Оплатить")
men6 = types.KeyboardButton("Назад")
meny.add(men1,men2,men3,men4,men5,men6)
######шаурма
шаурма = types.ReplyKeyboardMarkup(resize_keyboard=True)
шаурма1 = types.KeyboardButton("Классическая")
шаурма2 = types.KeyboardButton("Фирменная")
шаурма3 = types.KeyboardButton("Назад")
шаурма.add(шаурма1,шаурма2,шаурма3)
######шаурма классическая
класик = types.ReplyKeyboardMarkup(resize_keyboard=True)
курL = types.KeyboardButton("КуринаяL")
курXL = types.KeyboardButton("КуринаяXL")
курXXL = types.KeyboardButton("КуринаяXXL")
свинL = types.KeyboardButton("СвинаяL")
свинXL = types.KeyboardButton("СвинаяXL")
свинXXL = types.KeyboardButton("СвинаяXXL")
назкл = types.KeyboardButton("Назад")
класик.add(курL,курXL,курXXL,свинL,свинXL,свинXXL,назкл)
#####фирменная
фирменная=types.ReplyKeyboardMarkup(resize_keyboard=True)
Losначос=types.KeyboardButton("Losначос")
сырная=types.KeyboardButton("Сырная")
острая=types.KeyboardButton("Острая")
барбекю=types.KeyboardButton("Барбекю")
индия=types.KeyboardButton("Индия")
назкл1=types.KeyboardButton("Назад")
фирменная.add(Losначос,сырная,острая,барбекю,индия,назкл1)
###лапша
лапша=types.ReplyKeyboardMarkup(resize_keyboard=True)
курлапша=types.KeyboardButton("Куриная")
свинлапша=types.KeyboardButton("Свиная")
назкл2=types.KeyboardButton("Назад")
лапша.add(курлапша,свинлапша,назкл2)
#####шашлык
шашлык=types.ReplyKeyboardMarkup(resize_keyboard=True)
куршашлык=types.KeyboardButton("Куриный")
свиншашлык=types.KeyboardButton("Свиной")
назкл3=types.KeyboardButton("Назад")
шашлык.add(куршашлык,свиншашлык,назкл3)
######добавить
вкорзину=types.ReplyKeyboardMarkup(resize_keyboard=True)
корзина1=types.KeyboardButton("Корзина")
вкорзину1=types.KeyboardButton("В корзину")
назкл4=types.KeyboardButton("Назад")
вкорзину.add(корзина1,вкорзину1,назкл4)

###########корзина
корзина=types.ReplyKeyboardMarkup(resize_keyboard=True)
очистить=types.KeyboardButton("Очистить")
назкл5=types.KeyboardButton("Назад")
корзина.add(очистить,назкл5)
@bot.message_handler(content_types=['text'])
def func(message):
  global проверка
  global meny
  #########проверка пользователя
  users = f"{message.chat.id}.ini"
  копейки=0
  if not os.path.exists(users):
    def createConfig(users):
      config = configparser.ConfigParser()
      config.add_section("us")
      config.set("us", "scope", "0")
      config.set("us", "scopekop", "0")
      config.set("us", "proverka", "бот")
      config.set("us", "КуринаяL", "0")
      config.set("us", "КуринаяXL", "0")
      config.set("us", "КуринаяXXL", "0")
      config.set("us", "СвиннаяL", "0")
      config.set("us", "СвиннаяXL", "0")
      config.set("us", "СвиннаяXXL", "0")
      config.set("us", "Losначос", "0")
      config.set("us", "сырная", "0")
      config.set("us", "острая", "0")
      config.set("us", "индия", "0")
      config.set("us", "барбекю", "0")
      config.set("us", "шашлык.куриный", "0")
      config.set("us", "шашлык.свинной", "0")
      config.set("us", "лапша.куриная", "0")
      config.set("us", "лапша.свинная", "0")
      config.set("us", "Заказ", "Новый заказ,")
      with open(users, "w") as config_file:
        config.write(config_file)
      config = configparser.ConfigParser()
      config.read('online.ini')
      onlines=int(config.get("onlin", "users"))
      onlines1=onlines+1
      config.set("onlin", "users",f'{onlines1}')
      with open('online.ini', "w") as config_file:
        config.write(config_file)
    createConfig(users)
  config = configparser.ConfigParser()
  config.read(users)
  баланс = config.get("us", "scope")
  проверка = config.get("us", "proverka")
            ##############################
  if message.text=='Меню':
    bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=meny)
  elif message.text=='users':
    config = configparser.ConfigParser()
    config.read('online.ini')
    onlines=int(config.get("onlin", "users"))
    bot.send_message(message.chat.id,f'Количество пользователей бота:{onlines}')
  elif message.text=='Корзина':
    users = f"{message.chat.id}.ini"
    config = configparser.ConfigParser()
    config.read(users)
    баланс=int(config.get("us", "scope"))
    config.set("us", "заказ", f"Сумма вашего заказа:{баланс}₽\nВаш заказ:")
    with open(users, "w") as config_file:
      config.write(config_file)
    
    def my_function1():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "куринаяl"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "куринаяl"))
        tg=tg+f'\nКуриная L:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function2():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "куринаяxl"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "куринаяxl"))
        tg=tg+f'\nКуриная XL:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function3():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "куринаяxxl"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "куринаяxxl"))
        tg=tg+f'\nКуриная XXL:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function4():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "свиннаяl"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "свиннаяl"))
        tg=tg+f'\nСвиная L:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function5():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "свиннаяxl"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "свиннаяxl"))
        tg=tg+f'\nСвиная XL:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function6():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "свиннаяxxl"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "свиннаяxxl"))
        tg=tg+f'\nСвиная XXL:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function7():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "losначос"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "losначос"))
        tg=tg+f'\nLosначос:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function8():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "сырная"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "сырная"))
        tg=tg+f'\nСырная:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function9():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "острая"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "острая"))
        tg=tg+f'\nОстрая:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function10():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "индия"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "индия"))
        tg=tg+f'\nИндия:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function11():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "барбекю"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "барбекю"))
        tg=tg+f'\nБарбекю:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function12():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "лапша.куриная"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "лапша.куриная"))
        tg=tg+f'\nЛапша куриная:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function13():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "лапша.свинная"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "лапша.свинная"))
        tg=tg+f'\nЛапша свиная:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function14():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "шашлык.куриный"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "шашлык.куриный"))
        tg=tg+f'\nШашлык куриный:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    def my_function15():
      global users
      users = f"{message.chat.id}.ini"
      config = configparser.ConfigParser()
      config.read(users)
      tg=int(config.get("us", "шашлык.свинной"))
      if tg>0:
        config = configparser.ConfigParser()
        config.read(users)
        tg=str(config.get("us", "заказ"))
        ts=str(config.get("us", "шашлык.свинной"))
        tg=tg+f'\nШашлык свиной:{ts}шт'
        config.set("us", "заказ", f"{tg}")
        with open(users, "w") as config_file:
          config.write(config_file)
    my_function1()
    my_function2()
    my_function3()
    my_function4()
    my_function5()
    my_function6()
    my_function7()
    my_function8()
    my_function9()
    my_function10()
    my_function11()
    my_function12()
    my_function13()
    my_function14()
    my_function15()
    config = configparser.ConfigParser()
    config.read(users)
    tg=config.get("us", "заказ")
    bot.send_message(message.chat.id, text=f'{tg}'.format(message.from_user), reply_markup=корзина)
    config.set("us", "proverka", "корзина")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
  elif message.text=='Оплатить':
    config = configparser.ConfigParser()
    config.read(users)
    ss=int(config.get("us", "scopekop"))
    url=requests.post('https://securepay.tinkoff.ru/v2/Init',json={"TerminalKey": "TinkoffBankTest",
    "Amount": ss,
    "OrderId": "21050"})
    bot.send_message(message.chat.id,text=url)
  elif message.text=='Барбекю':
    config.set("us", "proverka", "барбекю")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/vwuGT64RTeqMsw')
    bot.send_message(message.chat.id, text="Армянский лаваш\nШашлык из свенины\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nСушеный жареный лук\nСоус барбекю\nЦена:250₽".format(message.from_user), reply_markup=вкорзину)
  elif проверка=='шашлык':
    if message.text=='Куриный':
      config.set("us", "proverka", "шашлыккур")
      with open(users, "w") as config_file:
        config.write(config_file)
      config = configparser.ConfigParser()
      config.read(users)
      проверка = config.get("us", "proverka")
      bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/w9n4ZWOELecaDQ')
      bot.send_message(message.chat.id, text="Шашлык из куриного филе\nАрмянский лаваш\nФирменный соус\nТоматный соус\n150₽ Цена за 100г".format(message.from_user), reply_markup=вкорзину)
    elif message.text=='Назад':
      config.set("us", "proverka", "бот")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=meny)
    elif message.text=='Свиной':
      config.set("us", "proverka", "шашлыксвин")
      with open(users, "w") as config_file:
        config.write(config_file)
      config = configparser.ConfigParser()
      config.read(users)
      проверка = config.get("us", "proverka")
      bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/UA-6pnmcGbDDfQ')
      bot.send_message(message.chat.id, text="Шашлык из свиной шеи\nАрмянский лаваш\nФирменный соус\nТоматный соус\n170₽ Цена за 100г".format(message.from_user), reply_markup=вкорзину)
  elif проверка=='лапша':
    if message.text=='Куриная':
      config.set("us", "proverka", "лапшакур")
      with open(users, "w") as config_file:
        config.write(config_file)
      config = configparser.ConfigParser()
      config.read(users)
      проверка = config.get("us", "proverka")
      bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/UAykvwoCrxjThA')
      bot.send_message(message.chat.id, text="Лапша домашняя\nШашлык из куриного филе\nФирменный соус\nТоматный соус\nЦена:160₽".format(message.from_user), reply_markup=вкорзину)
    elif message.text=='Назад':
      config.set("us", "proverka", "бот")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=meny)
    elif message.text=='Свиная':
      config.set("us", "proverka", "лапшасвин")
      with open(users, "w") as config_file:
        config.write(config_file)
      config = configparser.ConfigParser()
      config.read(users)
      проверка = config.get("us", "proverka")
      bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/MT3JGzclMR57Rg')
      bot.send_message(message.chat.id, text="Лапша домашняя\nШашлык из свиной шеи\nФирменный соус\nТоматный соус\nЦена:180₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='Индия':
    config.set("us", "proverka", "индия")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/XqQ7lyR_jvzFNA')
    bot.send_message(message.chat.id, text="Армянский лаваш\nШашлык из куриного филе\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nСладко-пряный соус\nЦена:220₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='Острая':
    config.set("us", "proverka", "острая")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/DqGZJVg8RLVmvA')
    bot.send_message(message.chat.id, text="Шашлык из куриного филе\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nПерец халапеньо\nФирменный соус\nОстрый соус\nЦена:230₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='Сырная':
    config.set("us", "proverka", "сырная")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/iSsnT6Fz-qJx8Q')
    bot.send_message(message.chat.id, text="Армянский лаваш\nШашлык из куриного филе\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nЖареная ветчина\nСыр красный Чеддер\nФирменный соус\nСырный соус\nЦена:240₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='Losначос':
    config.set("us", "proverka", "Losначос")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/HIUQ5YnIKVFxBw')
    bot.send_message(message.chat.id, text="Армянский лаваш\nШашлык из куриного филе\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nЖаренная ветчина\nСушеный жареный лук\nЧипсы начос\nФирменный соус\nБургерный соус\nЦена:260₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='КуринаяL':
    config.set("us", "proverka", "КуринаяL")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/vwuGT64RTeqMsw')
    bot.send_message(message.chat.id, text="Армянский лаваш\nШашлык из куриного филе\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nФирменный соус\nТоматный соус\nЦена:170₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='КуринаяXL':
    config.set("us", "proverka", "КуринаяXL")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/vwuGT64RTeqMsw')
    bot.send_message(message.chat.id, text="Армянский лаваш\nШашлык из куриного филе\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nФирменный соус\nТоматный соус\nЦена:200₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='КуринаяXXL':
    config.set("us", "proverka", "КуринаяXXL")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/vwuGT64RTeqMsw')
    bot.send_message(message.chat.id, text="Армянский лаваш\nШашлык из куриного филе\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nФирменный соус\nТоматный соус\nЦена:230₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='СвинаяL':
    config.set("us", "proverka", "СвиннаяL")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/vwuGT64RTeqMsw')
    bot.send_message(message.chat.id, text="Армянский лаваш\nШашлык из свинины\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nФирменный соус\nТоматный соус\nЦена:200₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='СвинаяXL':
    config.set("us", "proverka", "СвиннаяXL")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/vwuGT64RTeqMsw')
    bot.send_message(message.chat.id, text="Армянский лаваш\nШашлык из свенины\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nФирменный соус\nТоматный соус\nЦена:230₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='СвинаяXXL':
    config.set("us", "proverka", "СвиннаяXXL")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_photo(message.chat.id,'https://disk.yandex.ru/i/vwuGT64RTeqMsw')
    bot.send_message(message.chat.id, text="Армянский лаваш\nШашлык из свенины\nПекинская капуста\nСвежие помидоры\nСвежие огурцы\nФирменный соус\nТоматный соус\nЦена:260₽".format(message.from_user), reply_markup=вкорзину)
  elif message.text=='Шашлык':
    config.set("us", "proverka", "шашлык")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=шашлык)
  elif message.text=='Лапша':
    config.set("us", "proverka", "лапша")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_message(message.chat.id, text=f"Выберите!".format(message.from_user), reply_markup=лапша)
  elif message.text=='Фирменная':
    config.set("us", "proverka", "фирменная")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
    bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=фирменная)
  elif message.text=='Классическая':
    bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=класик)
    config.set("us", "proverka", "классическая")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
  elif message.text=='Шаурма':
    bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=шаурма)
    config.set("us", "proverka", "шаурма")
    with open(users, "w") as config_file:
      config.write(config_file)
    config = configparser.ConfigParser()
    config.read(users)
    проверка = config.get("us", "proverka")
  ####################кнопки#####################
  elif проверка=='Losначос':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "losначос"))
      tp = int(config.get("us", "scope"))
      ss = int(config.get("us", "scopekop"))
      ss = ss+260
      tp=tp+260
      ts=ts+1
      config.set("us", "scopekop", f"{ss}")
      config.set("us", "scope", f"{tp}")
      config.set("us", "losначос", f"{ts}")
      config.set("us", "proverka", "фирменная")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅Losначос удачно добавлена в корзину".format(message.from_user), reply_markup=фирменная)
    if message.text=='Назад':
      config.set("us", "proverka", "фирменная")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=фирменная)
  elif проверка=='лапшасвин':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "лапша.свинная"))
      tp = int(config.get("us", "scope"))
      ss = int(config.get("us", "scopekop"))
      ss = ss+18000
      tp=tp+180
      ts=ts+1
      config.set("us", "scopekop", f"{ss}")
      config.set("us", "scope", f"{tp}")
      config.set("us", "лапша.свинная", f"{ts}")
      config.set("us", "proverka", "лапша")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅Лапша свиная удачно добавлена в корзину".format(message.from_user), reply_markup=лапша)
    if message.text=='Назад':
      config.set("us", "proverka", "лапша")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=лапша)
  elif проверка=='лапшакур':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "лапша.куриная"))
      tp = int(config.get("us", "scope"))
      tp=tp+16000
      ts=ts+1
      config.set("us", "scope", f"{tp}")
      config.set("us", "лапша.куриная", f"{ts}")
      config.set("us", "proverka", "лапша")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅Лапша куриная удачно добавлена в корзину".format(message.from_user), reply_markup=лапша)
    if message.text=='Назад':
      config.set("us", "proverka", "лапша")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=лапша)
  elif проверка=='корзина':
    if message.text=='Назад':
      config.set("us", "proverka", "бот")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=meny)
    elif message.text=='Очистить':
      config.set("us", "scopekop", "0")
      config.set("us", "proverka", "бот")
      config.set("us", "куринаяl", "0")
      config.set("us", "куринаяxl", "0")
      config.set("us", "куринаяxxl", "0")
      config.set("us", "свиннаяl", "0")
      config.set("us", "свиннаяxl", "0")
      config.set("us", "свиннаяxxl", "0")
      config.set("us", "losначос", "0")
      config.set("us", "острая", "0")
      config.set("us", "сырная", "0")
      config.set("us", "индия", "0")
      config.set("us", "барбекю", "0")
      config.set("us", "шашлык.куриный", "0")
      config.set("us", "шашлык.свинной", "0")
      config.set("us", "лапша.куриная", "0")
      config.set("us", "лапша.свинная", "0")
      config.set("us", "scope", "0")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅Корзина успешно очищена!".format(message.from_user), reply_markup=meny)
  elif проверка=='шашлыксвин':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "шашлык.свинной"))
      tp = int(config.get("us", "scope"))
      tp=tp+170
      ts=ts+1
      config.set("us", "scope", f"{tp}")
      config.set("us", "шашлык.свинной", f"{ts}")
      config.set("us", "proverka", "шашлык")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅шашлык свиной удачно добавлена в корзину".format(message.from_user), reply_markup=шашлык)
    if message.text=='Назад':
      config.set("us", "proverka", "шашлык")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=шашлык)
  elif проверка=='шашлыккур':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "шашлык.куриный"))
      tp = int(config.get("us", "scope"))
      tp=tp+150
      ts=ts+1
      config.set("us", "scope", f"{tp}")
      config.set("us", "шашлык.куриный", f"{ts}")
      config.set("us", "proverka", "шашлык")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅Шашлык куриный удачно добавлена в корзину".format(message.from_user), reply_markup=шашлык)
    if message.text=='Назад':
      config.set("us", "proverka", "шашлык")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=шашлык)
  elif проверка=='сырная':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "сырная"))
      tp = int(config.get("us", "scope"))
      tp=tp+240
      ts=ts+1
      config.set("us", "scope", f"{tp}")
      config.set("us", "сырная", f"{ts}")
      config.set("us", "proverka", "фирменная")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅Сырная удачно добавлена в корзину".format(message.from_user), reply_markup=фирменная)
    if message.text=='Назад':
      config.set("us", "proverka", "фирменная")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=фирменная)
  elif проверка=='барбекю':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "барбекю"))
      tp = int(config.get("us", "scope"))
      tp=tp+250
      ts=ts+1
      config.set("us", "scope", f"{tp}")
      config.set("us", "барбекю", f"{ts}")
      config.set("us", "proverka", "фирменная")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅Барбекю удачно добавлена в корзину".format(message.from_user), reply_markup=фирменная)
    if message.text=='Назад':
      config.set("us", "proverka", "фирменная")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=фирменная)
  elif проверка=='индия':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      tp=int(config.get("us", "scope"))
      ts = int(config.get("us", "индия"))
      ts=ts+1
      tp=tp+220
      config.set("us", "scope", f"{tp}")
      config.set("us", "индия", f"{ts}")
      config.set("us", "proverka", "фирменная")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅Индия удачно добавлена в корзину".format(message.from_user), reply_markup=фирменная)
    if message.text=='Назад':
      config.set("us", "proverka", "фирменная")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=фирменная)
  elif проверка=='острая':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "острая"))
      tp = int(config.get("us", "scope"))
      ts=ts+1
      tp=tp+230
      config.set("us", "scope", f"{tp}")
      config.set("us", "острая", f"{ts}")
      config.set("us", "proverka", "фирменная")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅Острая удачно добавлена в корзину".format(message.from_user), reply_markup=фирменная)
    if message.text=='Назад':
      config.set("us", "proverka", "фирменная")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=фирменная)
  elif проверка=='КуринаяL':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "куринаяl"))
      tp= int(config.get("us", "scope"))
      ts=ts+1
      tp=tp+170
      config.set("us", "scope", f"{tp}")
      config.set("us", "куринаяl", f"{ts}")
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅КуринаяL удачно добавлена в корзину".format(message.from_user), reply_markup=класик)
    if message.text=='Назад':
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=класик)
  elif проверка=='КуринаяXL':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "куринаяxl"))
      tp = int(config.get("us", "scope"))
      tp=tp+200
      ts=ts+1
      config.set("us", "scope", f"{tp}")
      config.set("us", "куринаяxl", f"{ts}")
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅КуринаяXL удачно добавлена в корзину".format(message.from_user), reply_markup=класик)
    if message.text=='Назад':
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=класик)
  elif проверка=='КуринаяXXL':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "куринаяxxl"))
      tp = int(config.get("us", "scope"))
      tp=tp+230
      ts=ts+1
      config.set("us", "scope", f"{tp}")
      config.set("us", "куринаяxxl", f"{ts}")
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅КуринаяXXL удачно добавлена в корзину".format(message.from_user), reply_markup=класик)
    if message.text=='Назад':
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=класик)
  elif проверка=='СвиннаяL':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "свиннаяl"))
      tp = int(config.get("us", "scope"))
      ts=ts+1
      tp=tp+200
      config.set("us", "scope", f"{tp}")
      config.set("us", "свиннаяl", f"{ts}")
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅СвинаяL удачно добавлена в корзину".format(message.from_user), reply_markup=класик)
    if message.text=='Назад':
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=класик)
  elif проверка=='СвиннаяXL':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "свиннаяxl"))
      tp = int(config.get("us", "scope"))
      tp=tp+230
      ts=ts+1
      config.set("us", "scope", f"{tp}")
      config.set("us", "свиннаяxl", f"{ts}")
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅СвинаяXL удачно добавлена в корзину".format(message.from_user), reply_markup=класик)
    if message.text=='Назад':
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=класик)
  elif проверка=='СвиннаяXXL':
    if message.text=='В корзину':
      config = configparser.ConfigParser()
      config.read(users)
      ts = int(config.get("us", "свиннаяxxl"))
      tp = int(config.get("us", "scope"))
      tp=tp+260
      ts=ts+1
      config.set("us", "scope", f"{tp}")
      config.set("us", "свиннаяxxl", f"{ts}")
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="✅СвинаяXXL удачно добавлена в корзину".format(message.from_user), reply_markup=класик)
    if message.text=='Назад':
      config.set("us", "proverka", "классическая")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=класик)
  elif проверка=='шаурма':
    if message.text=='Назад':
      config.set("us", "proverka", "бот")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=meny)
  elif проверка=='фирменная':
    if message.text=='Назад':
      config.set("us", "proverka", "шаурма")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=шаурма)
  elif проверка=='классическая':
    if message.text=='Назад':
      config.set("us", "proverka", "шаурма")
      with open(users, "w") as config_file:
        config.write(config_file)
      bot.send_message(message.chat.id, text="Выберите!".format(message.from_user), reply_markup=шаурма)
  else:
    bot.send_message(message.chat.id, text="Здравствуйте вы попали в телеграмм бота онлайн заказов мясорубка".format(message.from_user), reply_markup=markup)
bot.polling(none_stop=True)
