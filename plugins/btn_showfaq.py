from plugin import Plugin

class ShowFAQ(Plugin):

    def OnCommand(self, objects):
        self.bot.api.messages.send(user_id=objects['from_id'], message='Ответы на самые часто задаваемые вопросы: vk.cc/891EFZ')

    buttons = ['show_faq']
 