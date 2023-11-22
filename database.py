# try wrapping the code below that reads a persons.csv file in a class
# and make it more general such that it can read in any csv file
import copy
import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def csv_path(file_csv):
    file = []
    with open(os.path.join(__location__, f'{file_csv}.csv')) as f:
        rows = csv.DictReader(f)
        for i in rows:
            file.append(dict(i))
    return file


def update_csv(table, key_list):
    scv_file = open(f"{table.table_name}.csv", 'w')
    writer = csv.writer(scv_file)
    writer.writerow(key_list)
    for dictionary in table.table:
        writer.writerow(dictionary.values())
    scv_file.close()


# add in code for a Database class
class DB:
    def __init__(self):
        self.db = []

    def insert(self, table):
        self.db.append(table)

    def search(self, table_name):
        for table in self.db:
            if table.table_name == table_name:
                return table
        return None


# add in code for a Table class
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def join(self, other_table, common_key):
        joined_table = Table(
            self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            if item1[aggregation_key] == float:
                temps.append(float(item1[aggregation_key]))
            else:
                temps.append(item1[aggregation_key])
        return function(temps)

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def __str__(self):
        return self.table_name + ':' + str(self.table)

    def insert(self, dictionary):
        self.table.append(dictionary)

    def update(self, key_of_id, id_val, key_of_value, value):
        for i in self.table:
            if i[key_of_id] == id_val:
                i[key_of_value] = value

# modify the code in the Table class so that it supports the insert
# operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update
# operation where an entry's value associated with a key can be updated
