from plugin import Plugin

class ShowHash(Plugin):

    def OnCommand(self, objects):
        self.bot.api.messages.send(user_id=objects['from_id'], message='Все хэштеги сообщества: vk.cc/86asHo')

    buttons = ['show_hash']
 