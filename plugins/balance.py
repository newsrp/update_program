from plugin import Plugin
from utils import getEmoji

class Balance(Plugin):

    def OnCommand(self, objects):
        user = self.bot.createUser(objects['from_id'])
        self.bot.api.messages.send(user_id=objects['from_id'], message='На Вашем счету ≜{} {}'.format(user.balance, getEmoji()), keyboard=self.bot.keyboards)
        user = None

    buttons = [
        'show_balance'
    ]

    commands = [
    'баланс ху',
    'сколько баланс',
    'сколько у меня ху',
    'сколько ху',
    'какой счет ху',
    'какой счёт ху',
    'узнать баланс',
    "мой баланс",
    'какой баланс',
    'баланс?',
    'баланс.',
    'баланс!',
    'баланс',
    'скок на счету',
    'сколько на счету',
    'какой у меня баланс',
    ]
