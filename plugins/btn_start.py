from plugin import Plugin

class StartButtons(Plugin):

    def OnCommand(self, objects):
        user = self.bot.createUser(objects['from_id'])
        user = None
        self.bot.api.messages.send(user_id=objects['from_id'], message='YEP! Теперь Вам доступна бото-клавиатура ✨')

    buttons = ['start']
 