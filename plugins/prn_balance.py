from plugin import Plugin
from utils import isAdmin

class PrnBalance(Plugin):

    def OnCommand(self, objects):
        if isAdmin(objects['from_id']) is False:
            return 'ok'

        message = objects['text'].split()
        if len(message) < 4:
            return self.bot.api.messages.send(user_id=objects['from_id'], message="Команда введена неправильно")

        if not message[1].isdigit() or not message[2].isdigit() or not message[3].isdigit():
            return self.bot.api.messages.send(user_id=objects['from_id'], message='Необходимо ввести: прн ID-пользователя ID-пользователя процент(1-100)')

        if int(message[3]) < 1 or int(message[3]) > 100:
            return self.bot.api.messages.send(user_id=objects['from_id'], message='Процент варьируется от 1 до 100')
            
        if int(message[2]) <= 0 or int(message[2]) < 0:
            return self.bot.api.messages.send(user_id=objects['from_id'], message='ID не может быть отрицательным')

        user1 = self.bot.createUser(message[1])
        user2 = self.bot.createUser(message[2])
        result_minus = int(abs(user1.balance*int(message[3])/100))
        text_format = "#log<br>Перенос ху-вон vk.com/id{} -> vk.com/id{}<br>Перенесено {}% от суммы {} = {} ху-вон".format(user1.id, user2.id, message[3], user1.balance, result_minus)
        user1.balance -= result_minus
        user2.balance += result_minus
        user1.save()
        user2.save()
        user1 = None
        user2 = None
        self.bot.api.messages.send(user_id=objects['from_id'], message=text_format)

    commands = ['прн']