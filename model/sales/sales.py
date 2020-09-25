model.sales.sales import data_manager
from model.data_manager import read_table_from_file,write_table_to_file
from model.util import generate_id
from view import terminal as view
from csv import reader
import os

""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]
# DATAFILE = '../model/sales/sales.csv'


# Plikow tekstowych sie nie importuje!
def data(file_name):  # To nie jest wzór do nasladowania
    file = open(file_name, 'r')
    lines = reader(file)
    result = []
    for i in lines:
        result.append([i[0].split(";")])
    result = [i[0] for i in result]
    return result


print(os.getcwd())
# print(data('../model/sales/sales.csv'))


def list_transactions():
    transation = data(DATAFILE)
    for i in transation:
        print(''.join(i))

    # view.print_error_message("Not implemented yet.")
    return transation

# list_transactions()

def add_transaction():
    print("ADD TRANSACTION")
    item = [generate_id(), generate_id(), input("Name item: "),input("Revenue: "),input("Date in YYYY-MM-DD format: ")]
    content = read_table_from_file(DATAFILE) + [item]
    print(content)
    write_table_to_file(DATAFILE, content)
    view.print_error_message("Not implemented yet.")
    print(item)
# add_transaction()

def update_transaction():
    print("UPDATE TRANSACTION")
    update_id = input('Provide id of record to update: ')
    transactions = read_table_from_file(DATAFILE)
    result = []
    for i in transactions:
        print(i)
        if i[0] == update_id:
            result.append([i[0],input('Employee id: '), input("Name item: "), input("Revenue: "),
                    input("Date in YYYY-MM-DD format: ")])
        else:
            result.append(i)
    print(result)
    write_table_to_file(DATAFILE, result)
    view.print_error_message("Not implemented yet.")

update_transaction()