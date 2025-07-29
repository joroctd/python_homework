import csv

def list_comp():
    with open('../csv/employees.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        data = list(csv_reader)[1:]
        # could grab indices based off header strings rather than using indices directly
        employee_names = [f'{e[1]} {e[2]}' for e in data]
        print(employee_names)
        e_names = [e for e in employee_names if 'e' in e]
        print(e_names)

list_comp()
