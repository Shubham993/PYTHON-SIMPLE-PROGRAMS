#To make Calculator with Python
print("Welcome to Shubham calculator")
a = float(input("Enter your first number:"))
b = float(input("Enter your second number:"))
r = input ("Enter the operator you want to use: add, substract, divide, multiply:")
if r == "add":
  print ("you have chosen add operator")
elif r == "substract":
  print ("you have chosen substract operator")
elif r == "multiply":
  print ("you have chosen multiply operator")
elif r == "divide":
 print ("you have chosen divide operator")
else:
  print ("you have chosen wrong operator:")
if r == "add":
  print("Your answer is", a + b)
if r == "substract":
  print("Your answer is", a - b)
if r =="multiply":  
  print("Your answer is", a * b)
if r =="divide":
 print("Your answer is", a / b)
elif():
  print("This Answer is not possible")
print("Thank You")