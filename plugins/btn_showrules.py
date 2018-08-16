from plugin import Plugin

class ShowRules(Plugin):

    def OnCommand(self, objects):
        self.bot.api.messages.send(user_id=objects['from_id'], message='Сложным языком (коротко): vk.cc/88tY4v<br>Простым языком (подробно): vk.cc/8dwLUs')

    buttons = ['show_rules']
 