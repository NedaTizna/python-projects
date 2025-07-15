# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c): #function1
 return(c*9/5)+32

# Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f): #function2
 return(f-32)*5/9

# Ask user to choose Celsius or Fahrenheit
choice=input("Convert from(C/F?)".upper())

if choice=='C':
 # Get temperature in Celsius and convert to Fahrenheit 
 temp=float(input("Enter temperature in Celsius:"))
 print("In Fahrenheit:" , celsius_to_fahrenheit(temp))
elif choice=='F':
 # Get temperature in Fahrenheit and convert to Celsius
 temp=float(input("Enter temperature in Fahrenheit:"))
 print("In Celsius:" , fahrenheit_to_celsius(temp))
else:
 # Handle invalid input
 print("Invalid choice.")
 

 
