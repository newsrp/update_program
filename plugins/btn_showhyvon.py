from plugin import Plugin

class ShowHyvon(Plugin):

    def OnCommand(self, objects):
        self.bot.api.messages.send(user_id=objects['from_id'], message='Основная информация о ху-вонах: vk.cc/89FAok<br>Более подробно в "справке" (она там же ↑). ')

    buttons = ['show_hy']
 