
import pandas as pd

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

# Merge the two data sources based on a common unique identifier
merged_data = pd.merge(employee_personal_info, organizations_part_timers, on=['Last Name', 'First Name'], how='inner')

# Trim whitespace from Last Name and First Name fields
merged_data['Last Name'] = merged_data['Last Name'].str.strip()
merged_data['First Name'] = merged_data['First Name'].str.strip()

# Convert Sales field to numerical values
sales_mapping = {'NR': 1, 'ESP': 2, 'NSP': 3}
merged_data['Sales'] = merged_data['Sales'].map(sales_mapping)

# Convert Employee Status field to numerical values
employee_status_mapping = {'Newly joined the company': 1, 'Has been in company for a long time': 2}
merged_data['Employee Status'] = merged_data['Employee Status'].map(employee_status_mapping)

# Convert Academic Status field to numerical values
academic_status_mapping = {'Good standing': 1, 'Probation': 2}
merged_data['Academic Status'] = merged_data['Academic Status'].map(academic_status_mapping)

# Handle missing or null values (if needed)
merged_data.fillna(value={'Sales': 0, 'Employee Status': 0, 'Academic Status': 0}, inplace=True)

# Create the fact table
fact_table = merged_data[['Last Name', 'First Name', 'Sales']]

# Create the employee dimension table
employee_dim = merged_data[['Last Name', 'First Name', 'Employee Status', 'Academic Status']]
employee_dim.drop_duplicates(inplace=True)
employee_dim.reset_index(drop=True, inplace=True)

# Create the sales dimension table
sales_dim = pd.DataFrame({
    'SalesID': range(1, len(sales_mapping) + 1),
    'SalesType': list(sales_mapping.keys())
})

# Create the time dimension table
time_dim = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=365),
    'Month': pd.date_range(start='2023-01-01', periods=365).strftime('%B'),
    'Year': pd.date_range(start='2023-01-01', periods=365).strftime('%Y')
})

# Create the organization dimension table
organization_dim = merged_data[['Last Name', 'First Name', 'Employee Status', 'Academic Status']]
organization_dim.drop_duplicates(inplace=True)
organization_dim.reset_index(drop=True, inplace=True)

# Print the resulting tables
print("Fact Table:")
print(fact_table)

print("\nEmployee Dimension Table:")
print(employee_dim)

print("\nSales Dimension Table:")
print(sales_dim)

print("\nTime Dimension Table:")
print(time_dim)

print("\nOrganization Dimension Table:")
print(organization_dim)
