# Simple calculator in python
 
# Get the first number from the user
num1=float(input("Enter first number:")) 

# Get the operator from the user
operator=input("Enter operator(+,-,*,/):") 

# Get the second number from the user
num2=float(input("Enter second number:")) 

# Perform caculation based on the operator
if operator=="+" :
 print(num1+num2) 
elif operator=="-":
 print(num1-num2)
elif operator=="*":
 print(num1*num2)
elif operator=="/":
 # chek for division by zero
 if num2!=0:
  print(num1/num2)
 else:
   print("Cannot divide by zero!")
else:
  # Handle invalid operatpr input
  print("Invalid operator")

 