from plugin import Plugin

class ShowAdmin(Plugin):

    def OnCommand(self, objects):
        self.bot.api.messages.send(user_id=objects['from_id'], message='Сурьозный вопрос админу или просто скучно?<br>Пиши! Ответим в течение n-ного времени 😌')

    buttons = ['show_admin']
 