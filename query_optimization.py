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
# employee_no=4000001
# while employee_no<=10000000:
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


"""
 to get count of records of employees table
"""
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
Now Dropping Indexes to check performance without Indexes.
"""

# sql_index=("DROP INDEX index_name ON table_name;")
# mycursor.execute("sql_index")
#
# sql_index=("DROP INDEX index_on_employee_name ON employees")
# mycursor.execute(sql_index)


"""
Creating Index on employee_name
"""
# sql_index=("create Index emp_inf_name on employees(name)")
# mycursor.execute(sql_index)


"""
Creating Index on dept_name in department table
"""
# sql_index=("create Index dept_inf_name on department(dept_name)")
# mycursor.execute(sql_index)

"""
Checking Indexes on employee table
# """
# tic = time()
# mycursor.execute("Show Index from employees")
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)

"""
Checking Indexes on department table
# """
# tic = time()
# mycursor.execute("Show Index from department")
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



"""
  Different Methods to optimize queries 
"""

"""
Creating a view table on employee_no and dept_no and joining it with the department table vs simiply selecting employee_no
dept_no and department name by inner joining the employees table with the department table
"""
#
# sql= "CREATE VIEW employee_info AS " \
#      "Select employee_no,dept_no " \
#      "from employees go"
# tic = time()
# mycursor.execute(sql)
# # myresult = mycursor.fetchall()
# # print(myresult)
# toc = time()
# print (toc - tic)


"""
Now joining the view with the department table
"""
# sql="Select employee_info.employee_no,employee_info.dept_no, department.dept_name " \
#     "from employee_info inner join department on employee_info.dept_no=department.dept_no "
# tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)



"""

Now simply applying join without using views

"""
#
# sql="Select employees.employee_no,employees.dept_no, department.dept_name " \
#     "from employees inner join department on employees.dept_no=department.dept_no "
# tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)


"""
retrieving data from two tables without join,  rather than join using AND
"""
# sql="Select employees.employee_no,employees.dept_no,department.dept_name from employees,department where employees.dept_no=department.dept_no"
# # tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)
"""
I pasting the queries I ran through phpmyadmin because pycharm stopped responding when 100000000 records were added
"""
#
# (to check effect of group by on query performance )
# select count(*) from employees group by dept_no

# (performing the same through union)



"""
GROUP BY VS DISTINCT
"""
# sql=("Select gender from employees group by gender")
# tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)




# sql=("Select distinct gender from employees ")
# tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)


"""
now for more distinct values which exists in employee_id table we will check performance of group by and distinct
"""


sql=("Select employee_no from employees group by employee_no")
tic = time()
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(myresult)
toc = time()
print (toc - tic)




# sql=("Select distinct gender from employees ")
# tic = time()
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)
# toc = time()
# print (toc - tic)



















































































































































































































































































































