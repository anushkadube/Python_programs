"""
class employee:
    pass
#no attributes and methods
emp_1=employee()
emp_2=employee()
#instance variable can be created manually
emp_1.first='aayushi'
emp_1.last='Johari'
emp_1.email='aayushi@edureka.co'
emp_1.pay=10000
 
emp_2.first='test'
emp_2.last='abc'
emp_2.email='test@company.com'
emp_2.pay=10000
print(emp_1.email)
print(emp_2.email)
"""
class employee:
    def __init__(self, first, last, sal):
        self.fname=first
        self.lname=last
        self.sal=sal
        self.email=first + '.' + last + '@company.com'
 
emp_1=employee('aayushi','johari',350000)
emp_2=employee('test','test',100000)
print(emp_1.email)
print(emp_2.email)
