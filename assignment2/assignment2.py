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


