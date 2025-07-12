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
print(employees)


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
print(employees)


def employee_dict(row):
    employee = dict(zip(employees['fields'], row))
    employee.pop('employee_id')
    return employee
