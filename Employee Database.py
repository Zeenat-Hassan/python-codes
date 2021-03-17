import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="Employee"

)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE employees ( employee_no INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),birthdate DATE,gender VARCHAR(255))")
# mycursor.execute("CREATE TABLE salary(employee_no INT AUTO_INCREMENT,position VARCHAR (255),salary INT,foreign key (employee_no) references employees(employee_no))")
# mycursor.execute("CREATE TABLE department(dept_no INT AUTO_INCREMENT PRIMARY KEY,dept_name VARCHAR (255))")
#mycursor.execute("ALTER TABLE salary ADD COLUMN position VARCHAR(255)")


"""
To generate 1000000 random records in employees table
"""
# name_lis=["Zeenat","Samra","Dua","Hanif","Fasih","Zarar"]
# gender_lis=["Male","Female"]
#
# employee_no=1
# while employee_no<=1000000:
#     sql = "INSERT INTO employees (name,gender,dept_no ) VALUES (%s,%s,%s)"
#     val = (random.choice(name_lis),random.choice(gender_lis) ,random.randint(1, 5))
#     mycursor.execute(sql, val)
#
#     mydb.commit()
#     employee_no += 1

"""
To generate random records in salary table.
"""
# position_lis=["Senior","Associate"]
# employee_no=5
# while employee_no<=1000000:
#     sql = "INSERT INTO salary(position,salary) VALUES (%s,%s)"
#     val = (random.choice(position_lis),random.randint(60000,100000))
#     mycursor.execute(sql, val)
#
#     mydb.commit()
#     employee_no +=1

"""
To check the count of the records in the table
"""

# mycursor.execute("SELECT count(*) FROM salary")
# myresult = mycursor.fetchall()
# print(myresult)


"""
 to get count of records of employees table
"""
# mycursor.execute("SELECT count(*) FROM employees")
# myresult = mycursor.fetchall()
# print(myresult)

"""
 to get unique names of employees
"""
# sql = "SELECT DISTINCT(name) FROM employees"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)

"""
 to get unique genders of employees
"""
# sql = "SELECT DISTINCT(gender) FROM employees"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)

"""
to get count of employeesin dept no 1
"""

# sql = "SELECT count(*) FROM employees where dept_no={}".format(1)
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)

"""
 to get employees whose gender is male
"""
# sql= "Select count(*) from employees where gender=\"Male\""
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""
to get records where gender is male
"""
# sql= "Select * from employees where gender=\"Male\""
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""
Query to get id's of employees whose name is zeenat
"""
# sql= "Select employee_no from employees where name=\"Zeenat\""
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)


"""
Practicing Subqueries
to get records of employees whose name and zeenat and gender male
"""
# sql="Select * from (Select * from employees where gender=\"Male\")t where name=\"Zeenat\""
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)


"""
to practice joins by joining department table and employees table
"""
# sql="Select * from employees inner join department on employees.dept_no=department.dept_no "
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""
JOINS
to joining multiple tables

"""
# sql="Select employees.employee_no,employees.name,employees.dept_no,employees.gender,department.dept_name,salary.position,salary.salary from salary inner join employees on employees.employee_no=salary.employee_no inner join department on employees.dept_no=department.dept_no "
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""
JOINS AND SUBQUERIES
 detail of the employee who has the maximum salary
"""
# sql="Select employees.employee_no,employees.name,employees.dept_no,employees.gender,department.dept_name,salary.position,salary.salary from salary inner join employees on employees.employee_no=salary.employee_no inner join department on employees.dept_no=department.dept_no where salary in (select max(salary) from salary)"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""
GROUP BY,SUBQUERY
12  to get employees with third max salary
"""
# sql="Select salary from (Select distinct(salary) from salary order by salary desc limit 3) t order by salary asc limit 1"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)


"""
GET top 3 salaries

"""
# sql="Select distinct(salary) from salary order by salary desc limit 3"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""
GROUP BY,SUBQUERY
Query to get employees with second max salary
"""
# sql="Select salary from (Select distinct(salary) from salary order by salary desc limit 2) t order by salary asc limit 1"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""

Query to get max salaries department wise
"""
# sql= "Select max(salary) as maxsal, dept_name as department from salary inner join employees on employees.employee_no=salary.employee_no inner join department on employees.dept_no=department.dept_no group by dept_name"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""

CONCAT built in function
"""
# sql="Select CONCAT(\"dept_no is \", dept_no ,\"and dept name is  \", dept_name) AS department_information from department"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""

Query to get min salaries department wise
# """
# sql= "Select min(salary) as maxsal, dept_name as department from salary inner join employees on employees.employee_no=salary.employee_no inner join department on employees.dept_no=department.dept_no group by dept_name"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)


"""

Query to get avg salaries department wise
# """
# sql= "Select avg(salary) as maxsal, dept_name as department from salary inner join employees on employees.employee_no=salary.employee_no inner join department on employees.dept_no=department.dept_no group by dept_name"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)


"""

Query to get sum of salaries department wise
"""
# sql= "Select sum(salary) as maxsal, dept_name as department from salary inner join employees on employees.employee_no=salary.employee_no inner join department on employees.dept_no=department.dept_no group by dept_name"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""
TOP funtion
"""
# sql="Select distinct(name) from employees where name like \"%n%\""
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)

"""
Group_concat function
"""

# sql="Select dept_name,GROUP_CONCAT(employee_no) from employees inner join department on employees.dept_no=department.dept_no group by dept_name"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)


"""
SUbSTR built in function
"""

sql="Select SUBSTR(dept_name,1,3) from department"
mycursor.execute(sql)
myresult=mycursor.fetchall()
print(myresult)

