import mysql.connector
from time import time
import random


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="QueryOptimization"

)

mycursor = mydb.cursor()
#
# mycursor.execute("CREATE TABLE employees ( employee_no INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),birthdate DATE,gender VARCHAR(255))")
# mycursor.execute("CREATE TABLE salary(employee_no INT AUTO_INCREMENT,position VARCHAR (255),salary INT,foreign key (employee_no) references employees(employee_no))")
# mycursor.execute("CREATE TABLE department(dept_no INT AUTO_INCREMENT PRIMARY KEY,dept_name VARCHAR (255))")
# mycursor.execute("ALTER TABLE employees ( ADD COLUMN dept_no INT,foreign key (dept_no) references department(dept_no))")
"""
To generate 1000000 random records in employees table
"""
# name_lis=["Zeenat","Samra","Dua","Hanif","Fasih","Zarar"]
# gender_lis=["Male","Female"]
#
# employee_no=2634497
# while employee_no<=4000000:
#     sql = "INSERT INTO employees (name,gender,dept_no ) VALUES (%s,%s,%s)"
#     val = (random.choice(name_lis),random.choice(gender_lis) ,random.randint(1, 5))
#     mycursor.execute(sql, val)
#
#     mydb.commit()
#     employee_no += 1

# """
# To generate random records in salary table.
# """
# position_lis=["Senior","Associate"]
# employee_no=2634497
# while employee_no<=4000000:
#     sql = "INSERT INTO salary(position,salary) VALUES (%s,%s)"
#     val = (random.choice(position_lis),random.randint(60000,100000))
#     mycursor.execute(sql, val)
#
#     mydb.commit()
#     employee_no +=1


# """
#  to get count of records of employees table
# """
# sql="SELECT count(*) FROM employees"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)

"""
To check the count of the records in the table
"""
# sql="SELECT count(*) FROM salary"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)


"""
Creating Index on dept_no
"""
#
# sql_index=("DROP INDEX index_name ON table_name;")
# mycursor.execute("sql_index")
#
# sql_index=("DROP INDEX index_on_employee_name ON employees")
# mycursor.execute(sql_index)


"""
Creating Index on employee_name
"""
# sql_index=("create Index index_on_empname on employees(name)")
# mycursor.execute(sql_index)


"""
Checking Indexes
# """
# tic = time()
# mycursor.execute("Show Index from employees")
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)


"""
Query to search through indexes
# """
# sql="Select * from employees with  (INDEX(index_on_employee_name))"
# tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)

"""
check execution time first without indexes on employee_name

"""
# sql="Select * from employees where name=\"Zeenat\""
# tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)
#execution time is 10.139633178710938

"""
Now making index and running same query
"""


# sql="Select * from employees where name=\"Zeenat\""
# tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)
#query time 11.150353908538818


"""
Now getting the same query through subqueries
"""
# sql="Select * " \
#     "from (Select * from employees where name=\"Zeenat\")t"

# tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)
#querytime is 16.97790002822876


"""
Query to get dept name and dept no and employee by simple join without index on deptname and dept_no
"""
# sql="Select employees.employee_no,department.dept_name, department.dept_no from  employees inner join department on employees.dept_no=department.dept_no "
#
#
#
# tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)

#querytime=50.31611204147339


"""
Now quering same after making index on dept_no,dept_name and using subquery instead of join.
"""
# sql_index=("create Index dept_info on department(dept_no,dept_name)")
# mycursor.execute(sql_index)

sql="Select employees.employee_name,employees.dept_no,department.dept_name from employees where department.dept_name exists (Select dept_name as department.dept_name from departments)"

tic = time()
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(myresult)
toc = time()
print (toc - tic)
















































































































































































































































































































































