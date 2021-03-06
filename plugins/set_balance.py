from plugin import Plugin
from utils import isAdmin

class SetBalance(Plugin):

    def OnCommand(self, objects):
        if isAdmin(objects['from_id']) is False:
            return 'ok'

        message = objects['text'].split()
        if len(message) < 3:
            return self.bot.api.messages.send(user_id=objects['from_id'], message="Команда введена неправильно")

        if not message[1].isdigit():
            return self.bot.api.messages.send(user_id=objects['from_id'], message='Необходимо ввести: сет ID-пользователя ху-вон')
            
        if not message[2].isdigit():
            return self.bot.api.messages.send(user_id=objects['from_id'], message='Необходимо ввести: сет ID-пользователя ху-вон')
            
        if int(message[1]) <= 0:
            return self.bot.api.messages.send(user_id=objects['from_id'], message='ID не может быть отрицательным')

        user = self.bot.createUser(int(message[1]))
        self.bot.api.messages.send(user_id=objects['from_id'], message='#log<br>Баланс vk.com/id{} изменен с {} на {}'.format(message[1], user.balance, message[2]))
        user.balance = int(message[2])
        user.save()
        user = None

    commands = ['сет']