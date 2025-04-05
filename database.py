import psycopg2 
from loader import config
from receipt import Receipt

class DataBase:
    def __init__(self):
        self.conn = psycopg2.connect(user=config['db']['user'],
                                     password=config['db']['password'],
                                     host=config['db']['host'],
                                     port=config['db']['port'],
                                     database=config['db']['database'])
        self.create_tables()
        
    def create_tables(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''CREATE table IF NOT EXISTS receipt
                            (doc_id TEXT NOT NULL,
                            item TEXT,
                            category TEXT NOT NULL,
                            amount INT,
                            price INT,
                            discount INT)''')
        except Exception as err: 
            print(repr(err))
        else:
            self.conn.commit()
        
    def insert_data(self, receipt: Receipt):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                            INSERT INTO receipt 
                            VALUES (%s, %s, %s, %s, %s, %s)
                            ''', (receipt.doc_id,
                            receipt.item,
                            receipt.category,
                            receipt.amount,
                            receipt.price,
                            receipt.discount))
        except Exception as err:
            print(repr(err))
        else:
            self.conn.commit()