import csv

def list_comp():
    with open('../csv/employees.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        data = list(csv_reader)[1:]
        # could grab indices based off header strings rather than using indices directly
        employee_names = [f'{emp[1]} {emp[2]}' for emp in data]
        print(employee_names)
        e_names = [name for name in employee_names if 'e' in name]
        print(e_names)

list_comp()
