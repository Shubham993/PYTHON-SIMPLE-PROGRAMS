#to find the largest and smallest number out of three number
a = int(input("\nEnter the first number ")) #It is taking input from the user to input 1st number
b = int(input("\nEnter the second number ")) #It is taking input from the user to input 2nd number
c = int(input("\nEnter the third number ")) #It is taking input from the user to input 3rd number

if a > b and a > c:   #Conditional Statement to check that ( if a is greater than b and c) this will be executed
  print("\n A is the greatest number")  #If the conditional Statement is true then this will be printed
elif b > a and b > c:   #Conditional Statement to check that ( if b is greater than a and c) this will be executed
  print("\n B is the greatest number")    #If the conditional Statement is true then this will be printed
elif c > a and c > b:   #Conditional Statement to check that ( if c is greater than a and b) this will be executed
  print("\n C is the greatest number")    #If the conditional Statement is true then this will be printed
else:   #Conditional Statement to check that ( if 2 or more numbers are input same ) this will be executed
  print("\n 2 or more numbers are same")    #If the conditional Statement is true then this will be printed

if a < b and a < c:
  print("\n A is the smallest number ")
if b < a and b < c:
  print("\n B is the smallest number")
if c < a and c < b:
  print("\n C is the smallest number")
else:
  print("\n 2 or more numbers are same ( For smallest number )")
