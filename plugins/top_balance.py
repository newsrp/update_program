from plugin import Plugin
from utils import isAdmin

class RemoveBalance(Plugin):

    def OnCommand(self, objects):
        if isAdmin(objects['from_id']) is False:
            return 'ok'

        message = objects['text'].split()
        if(len(message) != 2):
            self.bot.api.messages.send(user_id=objects['from_id'], message='Необходимо ввести: топ число')
            return 'ok'
        if not message[1].isdigit():
            self.bot.api.messages.send(user_id=objects['from_id'], message='Необходимо ввести: топ число')
            return 'ok'
        if int(message[1]) < 1 or int(message[1]) > 50:
            self.bot.api.messages.send(user_id=objects['from_id'], message='Предел варьируется от 1 до 50')
            return 'ok'
        s = 'Топ {} богачей<br><br>'.format(message[1])
        cursor = self.bot.db.query('SELECT `vk_id`, `balance` FROM `accounts` ORDER BY `balance` DESC LIMIT {}'.format(message[1]))
        dataq = cursor.fetchall()
        index = 1
        for i in dataq:
            s += '{}. vk.com/id{} — {} ху-вон<br>'.format(index, i[0], i[1])
            index += 1
        self.bot.api.messages.send(user_id=objects['from_id'], message=s)

    commands = ['топ']

