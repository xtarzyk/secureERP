# Do not modify this file!


def read_table_from_file(file_name, separator=';'):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "").split(separator) for element in lines]
    except IOError:
        return []


def write_table_to_file(file_name, table, separator=';'):
    with open(file_name, "a") as file:
        file.write("\n")
        for record in table:
            row = separator.join(record)
            file.write(record + ";")
