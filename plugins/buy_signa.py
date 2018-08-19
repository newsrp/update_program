from plugin import Plugin
from random import choice

class BuySigna(Plugin):
    
    def OnCommand(self, objects):
        user = self.bot.createUser(objects['from_id'])
        if user.balance < 1000:
            self.bot.api.messages.send(user_id=objects['from_id'], message='У вас недостаточно средств')
            user = None
            return

        random_id = choice(self.bot.signs)
        result = self.bot.api.users.get(user_ids='{},{}'.format(random_id, objects['from_id']))
        text_format = "Поздравляем! ✨ <br>Сигну сделает @id{} ({} {}).<br>Ожидайте её на днях. ".format(result[0]['id'], result[0]['first_name'], result[0]['last_name'])
        self.bot.api.messages.send(user_id=objects['from_id'], message=text_format)
        
        text_format = "@id{} ({} {}) заказал(-а) сигну. <br>Сигну делает @id{} ({} {})".format(result[1]['id'], result[1]['first_name'], result[1]['last_name'], result[0]['id'], result[0]['first_name'], result[0]['last_name'])
        self.bot.api.messages.send(chat_id=29, message=text_format)
        self.bot.api.messages.send(chat_id=30, message=text_format)

        user.balance -= 1000
        user.save()
        user = None

    commands = ['купить сигну']