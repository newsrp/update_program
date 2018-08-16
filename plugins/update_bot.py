from plugin import Plugin
from utils import isAdmin
from settings import vk_app, vk_login, vk_password, vk_scope, version_bot
import vk
import requests
import os

class UpdateBot(Plugin):

    def OnCommand(self, objects):
        if isAdmin(objects['from_id']) == False:
            return True

        self.bot.api.messages.send(user_id=objects['from_id'], message='Ищу обновления...')

        session = vk.AuthSession(vk_app, vk_login, vk_password, scope=vk_scope)
        api = vk.API(session, v=5.80)
        result = api.execute.getUpdateUrl()
        
        if result['v'] > version_bot:
            r = requests.get(result['program_url'])

            with open('download_update.exe', 'wb') as f:  
                f.write(r.content)

            self.bot.api.messages.send(user_id=objects['from_id'], message='Обновление бота...')

            os.system('start download_update.exe')

            os._exit(1)
        else:
            self.bot.api.messages.send(user_id=objects['from_id'], message='Обновлений для бота нет.')

    commands = ['обновить бота']

 