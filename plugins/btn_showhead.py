from plugin import Plugin

def findHead(manga):
    for i in manga:
        if i['text'].find('Обсудить главу') != -1:
            return i
    return manga[0]

class ShowHead(Plugin):

    def OnCommand(self, objects):
        result = self.bot.service_api.wall.search(owner_id=-131916561, query="#manhwa@hvdra", count=10)['items']
        result = findHead(result)
        self.bot.api.messages.send(user_id=objects['from_id'], attachment="wall{}_{}".format(result['owner_id'], result['id']))

    buttons = ['show_head']
 