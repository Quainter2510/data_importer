import csv 
import re 
import os
import shutil
from datetime import datetime
from receipt import Receipt

class CsvParser:
    def __init__(self, dir):
        self.dir = dir 
        
    def check_correct_filename(self, filename):
        return re.match(r'\d+_\d+\.csv', filename)
    
    def parse_csv_dir(self):
        receipts = []
        files = os.listdir(self.dir)
        for file in files:
            if self.check_correct_filename(file):
                receipts += self.upload_receipt(file)
        return receipts
    
    def upload_receipt(self, file):
        file_receipts = []
        with open(os.path.join(self.dir, file)) as receipt:
            reader = csv.DictReader(receipt, delimiter=";")
            for row in reader:
                file_receipts.append(Receipt(doc_id=row['doc_id'],
                                             item=row['item'],
                                             category=row['category'],
                                             amount=row['amount'],
                                             price=row['price'],
                                             discount=row['discount']))
        self.move_file_to_archive(file)
        return file_receipts
    
    def move_file_to_archive(self, file):
        shutil.move(os.path.join(self.dir, file),
                    os.path.join(os.getcwd(), 'archive', f'{datetime.now().date()}_{file}'))