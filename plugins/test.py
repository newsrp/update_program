from plugin import Plugin

class PluginTest(Plugin):

    def OnCommand(self, objects):
        self.bot.api.messages.send(user_id=objects['from_id'], message='Yes')

    commands = ['frkwfjegjwrjgwgjtrgjtrjrtwgrtgrw']
    
    enabled = False
 
