import sqlite3

class SQLitePipeline(object):
    def open_spider(self, spider):
        self.connection = sqlite3.connect('cotacao.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cotacao(
                dolar NUMBER,
                euro NUMBER,
                libra NUMBER,
                iene NUMBER
            )
        ''')

        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT OR IGNORE INTO cotacao(dolar, euro, libra, iene) VALUES(?, ?, ?, ?)
        ''',(
           item.get('dolar'),
           item.get('euro'),
           item.get('libra'),
           item.get('iene')
        ))
        self.connection.commit()
        return item
        