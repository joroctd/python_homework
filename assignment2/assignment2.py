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


def first_name(row):
    col = column_index('first_name')
    return employees['rows'][row][col]


def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    return list(filter(employee_match, employees['rows']))
