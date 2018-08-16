from plugin import Plugin, LoadPlugins

class UpdatePlugins(Plugin):

    def OnCommand(self, objects):
        self.bot.plugins = LoadPlugins(self.bot)
        self.bot.api.messages.send(user_id=objects['from_id'], message='Все плагины обновлены. Загружено {} штук'.format(len(self.bot.plugins)))

    commands = ['обновить плагины']