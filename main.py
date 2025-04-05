from csv_parser import CsvParser
from database import DataBase
import os 

if __name__ == "__main__":
    path = os.path.join(os.getcwd(), '..', 'household_goods_store', 'data')
    abs_path = os.path.abspath(path)
    
    database = DataBase()
    parser = CsvParser(abs_path)
    receipts = parser.parse_csv_dir()
    for receipt in receipts:
        database.insert_data(receipt)