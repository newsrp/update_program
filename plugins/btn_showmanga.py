from plugin import Plugin

class ShowManga(Plugin):

    def OnCommand(self, objects):
        self.bot.api.messages.send(user_id=objects['from_id'], message='Подробнее о комиксах, что мы переводим: vk.cc/7yMym5')

    buttons = ['show_manga']
 