#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#########################################################################
# BotTelegram Zabbix
# Filename: botTelegram-zabbix.py
##########################################################################

from telegram.ext import Updater, CommandHandler
import logging
import sys
import subprocess
import urllib
import requests

##########################################
# Python install module
# git clone https://github.com/possess1on/botTelegram-zabbix.git
# cd botTelegram-zabbix
# pip install python-telegram-bot
# sudo apt-get install python-pip
# pip install -r requirements.txt
# Test
# python botTelegram-zabbix.py
#
# BG
# python botTelegram-zabbix.py&
#
##########################################

##########################################
# Install python & pip
# pip install pip python-telegram-bot --upgrade
# apt-get install python-urllib3
##########################################


varZabbixmapa1 = "url"
varZabbixmapa2 = "url"
varZabbixmapa3 = "url"
varZabbixmapa4 = "url"
varZabbixmapa5 = "url"
varZabbixmapa6 = "url"
varZabbixmapa7 = "url"
varZabbixmapa8 = "url"
varZabbixmapa9 = "url"
varZabbixmapa10 = "url"
varZabbixmapa11 = "url"
varZabbixmapa12 = "url"
varZabbixmapa13 = "url"
varZabbixmapa14 = "url"
varZabbixmapa15 = "url"


users_liberados = [id]


varBotToken = 'token'


varUsername = "log"
varPassword = "pass"
varZabbixServer = "url"


varZabbixLanguage = "US"



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO,
                    filename='botTelegram_zabbix.log')
logging.info('Started')

logger = logging.getLogger(__name__)
job_queue = None

# Zabbix cookie
varcookie = None





def start(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    bot.sendMessage(update.message.chat_id, text='Добро пожаловать!!')

def mapa1(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa1
        file_img = "botTelegram_mapa1.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
		return


def mapa2(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa2
        file_img = "botTelegram_mapa2.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa3(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa3
        file_img = "botTelegram_mapa3.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa4(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa4
        file_img = "botTelegram_mapa4.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa5(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa5
        file_img = "botTelegram_mapa5.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa6(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa6
        file_img = "botTelegram_mapa6.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa7(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa7
        file_img = "botTelegram_mapa7.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa8(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa8
        file_img = "botTelegram_mapa8.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa9(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa9
        file_img = "botTelegram_mapa9.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa10(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa10
        file_img = "botTelegram_mapa10.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa11(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa11
        file_img = "botTelegram_mapa11.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa12(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa12
        file_img = "botTelegram_mapa12.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa13(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:

        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa13
        file_img = "botTelegram_mapa13.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return


def mapa14(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa14
        file_img = "botTelegram_mapa14.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return

def mapa15(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    try:


        # urllib.urlretrieve(varZabbixmapa5, "botTelegram_mapa5.jpg")
        login()
        zbx_img_url = varZabbixmapa15
        file_img = "botTelegram_mapa15.jpg"
        res = requests.get(zbx_img_url, cookies=varcookie)
        res_code = res.status_code
        if res_code == 404:
            logger.warn("Код 404 проверьте адрес: {}".format(zbx_img_url))
            return False
        res_img = res.content
        with open(file_img, 'wb') as fp:
            fp.write(res_img)
        fp.close
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

    except IndexError:
        return
    except ValueError:
        return
        
        
def help(bot, update):
    chat_id = update.message.chat_id
    if not chat_id in users_liberados:
        logging.info("Не найден - ID {}".format(chat_id))
        return
    bot.sendMessage(update.message.chat_id, text="Help:\n"
                                                 "/atm - Банкоматы\n"
                                                 "/postamat - Почтаматы\n"
                                                 "/140100 - Аксу\n"
                                                 "/140200 - Актогай\n"
                                                 "/140300 - Баянаул\n"
                                                 "/140400 - Железинка\n"
                                                 "/140500 - Иртышск\n"
                                                 "/140600 - Качиры\n"
                                                 "/140700 - Лебяжий\n"
                                                 "/140800 - Майск\n"
                                                 "/140900 - ПРУПС\n"
                                                 "/141000 - Успенка\n"
                                                 "/141100 - Щербакты\n"
                                                 "/141200 - Экибастуз\n"
                                                 "/140000 - ОПСы\n")


def error(bot, update, error):
    logger.warn('Update "%s" error "%s"' % (update, error))


def login():
    global varcookie
    requests.packages.urllib3.disable_warnings()

    if varZabbixLanguage == "PT":
        data_api = {"name": varUsername, "password": varPassword, "enter": "Connect-SE"}
    else:
        data_api = {"name": varUsername, "password": varPassword, "enter": "Sign in"}

    req_cookie = requests.post(varZabbixServer + "/", data=data_api, verify=True)
    varcookie = req_cookie.cookies
 

    if len(req_cookie.history) > 1 and req_cookie.history[0].status_code == 302:
        logger.warn("Проверьте адрес сервера")

    if not varcookie:
        logger.warn("Проверьте имя пользователя и пароль")
        varcookie = None

def grafico(bot, update, args):
        chat_id = update.message.chat_id
        if not chat_id in users_liberados:
            logging.info("Не найден - ID {}".format(chat_id))
            return
        try:
            #print len(args)
            if len(args) < 2:
                bot.sendMessage(chat_id, text='Корректность')
                return False
            grafico_id = args[0]
            grafico_seg = args[1]
            login()     
            zbx_img_url = ("{}/chart.php?itemids={}&period={}&width=600".format(varZabbixServer, grafico_id, grafico_seg))
            file_img = "botTelegram_grafico_{}.jpg".format(grafico_id)
            res = requests.get(zbx_img_url, cookies=varcookie)
            res_code = res.status_code
            if res_code == 404:
                logger.warn("Проверьте адрес Zabbix Grafico: {}".format(zbx_img_url))
                return False
            res_img = res.content
            with open(file_img, 'wb') as fp:
                fp.write(res_img)
            fp.close()
            bot.sendPhoto(chat_id=update.message.chat_id, photo=open(file_img, 'rb'))

        except (IndexError, ValueError):
            update.message.reply_text('Проверьте ID grafico')
            return

def main():
    global job_queue

    updater = Updater(varBotToken)
    job_queue = updater.job_queue

    dp = updater.dispatcher



    dp.add_handler(CommandHandler("atm", mapa1))
    dp.add_handler(CommandHandler("postamat", mapa2))
    dp.add_handler(CommandHandler("140100", mapa3))
    dp.add_handler(CommandHandler("140200", mapa4))
    dp.add_handler(CommandHandler("140300", mapa5))
    dp.add_handler(CommandHandler("140400", mapa6))
    dp.add_handler(CommandHandler("140500", mapa7))
    dp.add_handler(CommandHandler("140600", mapa8))
    dp.add_handler(CommandHandler("140700", mapa9))
    dp.add_handler(CommandHandler("140800", mapa10))
    dp.add_handler(CommandHandler("140900", mapa11))
    dp.add_handler(CommandHandler("141000", mapa12))
    dp.add_handler(CommandHandler("141100", mapa13))
    dp.add_handler(CommandHandler("141200", mapa14))
    dp.add_handler(CommandHandler("140000", mapa15))
    dp.add_handler(CommandHandler("grafico", grafico, pass_args=True))
    dp.add_handler(CommandHandler("help", help))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()


    updater.idle()
    logging.info('Finished')
    logging.shutdown()

if __name__ == '__main__':
    main()
