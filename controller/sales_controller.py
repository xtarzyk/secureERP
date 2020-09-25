model.sales.sales import data_manager
from model.data_manager import read_table_from_file,write_table_to_file
from model.util import generate_id
from view import terminal as view
from csv import reader
import os

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

FILE_NAME = '../model/sales/sales.csv'
def list_transactions():
    transation = data(FILE_NAME)
    for i in transation:
        print(''.join(i))

    # view.print_error_message("Not implemented yet.")
    return transation

# list_transactions()

def add_transaction():
    print("ADD TRANSACTION")
    item = [generate_id(), generate_id(), input("Name item: "),input("Revenue: "),input("Date in YYYY-MM-DD format: ")]
    content = read_table_from_file(FILE_NAME) +[item]
    print(content)
    write_table_to_file(FILE_NAME,content)
    view.print_error_message("Not implemented yet.")
    print(item)
# add_transaction()

def update_transaction():
    print("UPDATE TRANSACTION")
    update_id = input('Provide id of record to update: ')
    transactions = read_table_from_file(FILE_NAME)
    result = []
    for i in transactions:
        print(i)
        if i[0] == update_id:
            result.append([i[0],input('Employee id: '), input("Name item: "), input("Revenue: "),
                    input("Date in YYYY-MM-DD format: ")])
        else:
            result.append(i)
    print(result)
    write_table_to_file(FILE_NAME,result)
    view.print_error_message("Not implemented yet.")

update_transaction()


def delete_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
