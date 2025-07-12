def read_employees():
    info = {}
    rows = []
    try:
        with open('../csv/employees.csv') as file:
            for i, line in enumerate(file):
                data = line.split(',')
                if i == 0:
                    info['fields'] = data
                else:
                    rows.append(data)
        info['rows'] = rows
    except:
        print('Error')
    
    return info

employees = read_employees()


def column_index(header):
    return employees['fields'].index(header)

employee_id_column = column_index('employee_id')


def first_name(row_num):
    col_num = column_index('first_name')
    return employees['rows'][row_num][col_num]


def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    return list(filter(employee_match, employees['rows']))


def employee_find_2(employee_id):
    return list(filter(
        lambda row : int(row[employee_id_column]) == employee_id , 
        employees["rows"]
    ))


def sort_by_last_name():
    employees['rows'].sort(key=lambda row : row[column_index('last_name')])
    return employees['rows']

sort_by_last_name()


def employee_dict(row):
    employee = dict(zip(employees['fields'], row))
    employee.pop('employee_id')
    return employee


def all_employees_dict():
    eid_col_ind = column_index('employee_id')
    employees_dict = {}
    for row in employees['rows']:
        employees_dict[row[eid_col_ind]] = employee_dict(row)
    return employees_dict


import os
ENV_THIS_VALUE = 'THISVALUE'

def set_this_value(string):
    os.environ[ENV_THIS_VALUE] = string

set_this_value('ABC')

def get_this_value():
    return os.getenv(ENV_THIS_VALUE)


import custom_module

def set_that_secret(secret):
    custom_module.set_secret(secret)


import csv

def read_minutes():
    def read_single(file_name):
        info = {}
        rows = []
        try:
            with open(f'../csv/{file_name}.csv') as file:
                csv_reader = csv.reader(file, delimiter=',', quotechar='"')
                info['fields'] = next(csv_reader)
                for line in csv_reader:
                    rows.append(tuple(line))
            info['rows'] = rows
        except:
            print('Error')
        
        return info
    
    return read_single('minutes1'), read_single('minutes2')

minutes1, minutes2 = read_minutes()


def create_minutes_set():
    sm1 = set(minutes1['rows'])
    sm2 = set(minutes2['rows'])
    return set.union(sm1, sm2)

minutes_set = create_minutes_set()


from datetime import datetime

def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))

minutes_list = create_minutes_list()


def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    mapped_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_list))
    try:
        with open('./minutes.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(minutes1['fields'])
            csv_writer.writerows(mapped_list)
    except:
        print('Error')
    return mapped_list

write_sorted_list()
