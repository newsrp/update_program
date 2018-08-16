from plugin import Plugin
from utils import isAdmin

class ShowBalance(Plugin):

    def OnCommand(self, objects):

        if isAdmin(objects['from_id']) is False:
            return 'ok'

        message = objects['text'].split()

        if len(message) < 2:
            return 'ok'

        if not message[1].isdigit():
            return self.bot.api.messages.send(user_id=objects['from_id'], message='Необходимо ввести: балл ID-пользователя')
        if int(message[1]) <= 0:
            return self.bot.api.messages.send(user_id=objects['from_id'], message='ID не может быть отрицательным или равен нулю')

        user = self.bot.createUser(int(message[1]))
        self.bot.api.messages.send(user_id=objects['from_id'], message='Баланс id{}: {} ≜'.format(user.id, user.balance))
        user = None

    commands = ['бал ', 'балл ']
 