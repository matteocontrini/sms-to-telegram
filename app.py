import datetime
import html
import logging
import os

import gammu
import telebot

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHANNEL_ID = os.environ['TELEGRAM_CHANNEL_ID']

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s[%(asctime)s] %(message)s', datefmt='%Y-%m-%dT%H:%M:%S%z')

bot = telebot.TeleBot(TOKEN)

sm = gammu.StateMachine()


# Windows
# sm.SetConfig(0, {
#     'Connection': 'at',
#     'Device': 'COM3'
# })


def maybe_reset():
    if datetime.datetime.now().minute == 0:
        # logging.warning('Requesting soft reset')
        # try:
        #     sm.Reset(False)
        # except gammu.ERR_NOTCONNECTED:
        #     logging.exception('Soft reset failed')
        logging.warning('Power-cycling USB port')
        os.system('sudo uhubctl -a cycle -l 1-1 -p 5')


def serialize(sms):
    text = '<strong>{}</strong>'.format(html.escape(sms['Number']))
    text += '\n\n'
    text += html.escape(sms['Text'])
    text += '\n\n'
    text += '({})'.format(sms['DateTime'].isoformat())
    return text


def get_next_sms():
    try:
        return sm.GetNextSMS(Start=True, Folder=0)[0]
    except gammu.ERR_EMPTY:
        return None


def main():
    sm.SetConfig(0, {
        'Connection': 'at',
        'Device': '/dev/ttyUSB0'
    })

    # Connect to phone
    try:
        sm.Init()
    except (gammu.ERR_DEVICENOTEXIST, gammu.ERR_NOSIM):
        logging.exception('Init error')
        maybe_reset()
        return

    logging.info('Checking for new SMS')
    while True:
        sms = get_next_sms()
        if not sms:
            break
        logging.info(sms)
        text = serialize(sms)
        bot.send_message(
            chat_id=CHANNEL_ID,
            text=text,
            parse_mode='HTML'
        )
        sm.DeleteSMS(Folder=0, Location=sms['Location'])
    maybe_reset()
    logging.info('Done')


if __name__ == '__main__':
    main()
