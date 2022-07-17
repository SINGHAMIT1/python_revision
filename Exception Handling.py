from logging import exception

x=input("Enter Number 1: ")
y=input("Enter Number 2 :")
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print("Division by zero Exception occured ")
    z= None
except TypeError as e:
    print("TypeErrorException")
    z=None

print("the division is :" ,z)