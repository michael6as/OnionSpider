from tinydb import TinyDB, Query
from dal.db_provider import DbProvider


class TinyDbProvider(DbProvider):
    def __init__(self):
        self.db = TinyDB('db.json')

    def insert_paste(self, paste):
        query = Query()
        query_result = self.db.search(query.id == paste['id'])
        if len(query_result) == 0:
            self.db.insert(paste)
            print('inserted '+paste['id'])
        else:
            print('Old Paste ' + paste['id'])

    def search_paste(self, paste):
        return paste in self.db
