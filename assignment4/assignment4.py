import pandas as pd
import json

# 1.1 Create a DataFrame from a dictionary
task1_data_frame = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# 1.2 Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

# 1.3 Modify an existing column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1

# 1.4 Save the DataFrame as a CSV file
filename = 'employees.csv'
task1_older.to_csv(filename, index=False)

# ---

# 2.1 Read data from a CSV file
task2_employees = pd.read_csv(filename)

# 2.2 Read data from a JSON file
filename = 'additional_employees.json'
with open(filename, 'w') as file:
    data = json.dumps({
        'Name': ['Eve', 'Frank'],
        'Age': [28, 40],
        'City': ['Miami', 'Seattle'],
        'Salary': [60000, 95000]
    })
    file.write(data)
json_employees = pd.read_json(filename)

# 2.3 Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)

# ---

# 3.1 Use the head() method
first_three = more_employees.head(3)

# 3.2 Use the tail() method
last_two = more_employees.tail(2)

# 3.3 Get the shape of a DataFrame
employee_shape = more_employees.shape

# 3.4 Use the info() method
print(more_employees.info(False))

# ---

# 4.1 Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data
dirty_data = pd.read_csv('dirty_data.csv')
clean_data = dirty_data.copy()

# 4.2 Remove any duplicate rows from the DataFrame
clean_data.drop_duplicates(subset=['Name'], inplace=True)

# 4.3 Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
# 4.5 Fill missing numeric values (use fillna).  Fill Age with the mean
average_age = clean_data['Age'].mean()
clean_data.fillna({'Age': average_age}, inplace=True)

# 4.4 Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data.replace({'Salary': ['unknown', 'n/a']}, pd.NA, inplace=True)
# 4.5 Fill missing numeric values (use fillna).  Fill Salary with the median
median_salary = clean_data['Salary'].median()
clean_data.fillna({'Salary': median_salary}, inplace=True)

# 4.6 Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format='mixed')

# 4.7 Strip extra whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].apply(str.strip)
clean_data['Department'] = clean_data['Department'].apply(lambda d : str.strip(d).upper())
