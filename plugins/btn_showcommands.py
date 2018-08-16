from plugin import Plugin

class ShowCommands(Plugin):

    def OnCommand(self, objects):
        self.bot.api.messages.send(user_id=objects['from_id'], message='Временно не работает')

    buttons = ['show_commands']
 