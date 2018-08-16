from plugin import Plugin
from utils import isAdmin

class AddBalance(Plugin):

    def OnCommand(self, objects):
        if isAdmin(objects['from_id']) is False:
            return 'ok'

        message = objects['text'].split()
        if len(message) < 3:
            return self.bot.api.messages.send(user_id=objects['from_id'], message="Команда введена неправильно", keyboard=self.bot.keyboards)

        if not message[1].isdigit():
            return self.bot.api.messages.send(user_id=objects['from_id'], message='Необходимо ввести: плю ID-пользователя ху-вон', keyboard=self.bot.keyboards)
            
        if not message[2].isdigit():
            return self.bot.api.messages.send(user_id=objects['from_id'], message='Необходимо ввести: плю ID-пользователя ху-вон', keyboard=self.bot.keyboards)
            
        if int(message[1]) <= 0 or int(message[2]) < 0:
            return self.bot.api.messages.send(user_id=objects['from_id'], message='Число не может быть отрицательным', keyboard=self.bot.keyboards)

        user = self.bot.createUser(int(message[1]))
        self.bot.api.messages.send(user_id=objects['from_id'], message='#log<br>Баланс vk.com/id{} изменен с {} на {}'.format(message[1], user.balance, user.balance + int(message[2])), keyboard=self.bot.keyboards)
        user.balance += int(message[2])
        user.save()
        user = None

    commands = ['плю']