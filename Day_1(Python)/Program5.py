#Functions
def function1():
    print("Function 1")
def function2(num1,num2):
    print(num1,num2)
    #print()__str__
def function3(num1,num2):
    return (num1+num2)
def function4(num1,num2):
    return (num1+num2)
def function5(num1,num2):
    num3 = float(num1) + num2
    return num3
#print(function4(10,20.2))
print(function5('10',20.2))

#categories of functions
#based on arguments
#1.positional arguments
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,22,33,44)
#2.Keyword argments
def function2(num1,num2,num3,num4): 
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num1=10,num2=23,num3=69)    

#3.default arguments
def fun3(name,roll,branch="CSE",clgname="GIET"):
    print(name,roll,branch,clgname)
fun3("fraz",239)
fun3("ash",229)
fun3("abc",219,"ECE")
fun3("xyz",209,"CSE")

#4.variable number of arguments
def fun4(*var):
    for i in var:
        print(i,end=' ')
fun4(1,2,3)

def add(*var):
    sum = 0
    for i in var:
        sum=sum+i 
    return sum    
print(add(10,20))
print(add(10,20,20))
