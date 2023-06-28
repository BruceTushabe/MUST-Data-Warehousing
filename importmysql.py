import mysql.connector
import pandas as pd

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    database='your_database'
)

# Create a cursor to execute SQL statements
cursor = connection.cursor()

# Employee Personal Information DataFrame
employee_personal_info = pd.DataFrame({
    'Last Name': ['Smith', 'Johnson', 'Williams'],
    'First Name': ['John', 'Emma', 'Michael'],
    'Sales': ['NR', 'ESP', 'NSP']
})

# Information on Organizations Part Timers DataFrame
organizations_part_timers = pd.DataFrame({
    'Last Name': ['Smith', 'Williams', 'Johnson'],
    'First Name': ['John', 'Michael', 'Emma'],
    'Employee Status': ['Newly joined the company', 'Has been in company for a long time', 'Newly joined the company'],
    'Academic Status': ['Good standing', 'Probation', 'Good standing']
})

# ... (Perform data transformations as shown in the previous code)

# Create tables in the MySQL database
cursor.execute('CREATE TABLE fact_table (Last_Name VARCHAR(40), First_Name VARCHAR(15), Sales INT)')
cursor.execute('CREATE TABLE employee_dim (Last_Name VARCHAR(40), First_Name VARCHAR(15), Employee_Status VARCHAR(10), Academic_Status VARCHAR(13))')
cursor.execute('CREATE TABLE sales_dim (Sales_ID INT, Sales_Type VARCHAR(3))')
cursor.execute('CREATE TABLE time_dim (Date DATE, Month VARCHAR(9), Year VARCHAR(4))')
cursor.execute('CREATE TABLE organization_dim (Last_Name VARCHAR(40), First_Name VARCHAR(15), Employee_Status VARCHAR(10), Academic_Status VARCHAR(13))')

# Insert data into the tables
fact_table_values = merged_data[['Last Name', 'First Name', 'Sales']].values.tolist()
cursor.executemany('INSERT INTO fact_table (Last_Name, First_Name, Sales) VALUES (%s, %s, %s)', fact_table_values)

employee_dim_values = employee_dim.values.tolist()
cursor.executemany('INSERT INTO employee_dim (Last_Name, First_Name, Employee_Status, Academic_Status) VALUES (%s, %s, %s, %s)', employee_dim_values)

sales_dim_values = sales_dim.values.tolist()
cursor.executemany('INSERT INTO sales_dim (Sales_ID, Sales_Type) VALUES (%s, %s)', sales_dim_values)

time_dim_values = time_dim.values.tolist()
cursor.executemany
