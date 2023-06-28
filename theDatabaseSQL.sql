-- Create the fact table
CREATE TABLE fact_table (
  Last_Name VARCHAR(40),
  First_Name VARCHAR(15),
  Sales INT
);

-- Create the employee dimension table
CREATE TABLE employee_dim (
  Last_Name VARCHAR(40),
  First_Name VARCHAR(15),
  Employee_Status VARCHAR(10),
  Academic_Status VARCHAR(13)
);

-- Create the sales dimension table
CREATE TABLE sales_dim (
  Sales_ID INT,
  Sales_Type VARCHAR(3)
);

-- Create the time dimension table
CREATE TABLE time_dim (
  Date DATE,
  Month VARCHAR(9),
  Year VARCHAR(4)
);

-- Create the organization dimension table
CREATE TABLE organization_dim (
  Last_Name VARCHAR(40),
  First_Name VARCHAR(15),
  Employee_Status VARCHAR(10),
  Academic_Status VARCHAR(13)
);
