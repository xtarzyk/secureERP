""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def list_customers_model():
    data = data_manager.read_table_from_file(DATAFILE, separator=';')
    print (HEADERS[1])
    for name in range(len(data)):
     print (data[name][1])


def add_customer_model():
    table = []
    file_name = "model/crm/crm.csv"
    separator = ";"
    ide = util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    table.append(str(ide))
    name =(input ("Give me your name:"))
    table.append(str(name))
    email = (input("Give me your email:"))
    table.append(str(email))
    with open(file_name, "a") as file:
        file.write("\n")
        for record in table:
            row = separator.join(record)
            file.write(record + ";")
    
