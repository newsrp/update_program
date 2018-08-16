from plugin import Plugin

class ShowDonate(Plugin):

    def OnCommand(self, objects):
        self.bot.api.messages.send(user_id=objects['from_id'], message='За него ху-воны дают! 😨<br>Подробнее: vk.cc/8dwMnZ')

    buttons = ['show_donate']
 