# Basic Console Calculator

# Definitions
def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def div(x, y):
  return x / y

def power(x, y):
  return x ** y

# Prompts the user to make a selection
print("Basic Console Calculator \n"
      "\n"
      "Please make a selection:\n"
      "1) Addition\n"
      "2) Subtraction\n"
      "3) Multiplication\n"
      "4) Divide\n"
      "5) Exponential\n")

while True:
  choice=input("Enter choice: 1/2/3/4/5: ")

  if choice in ('1', '2', '3', '4'):
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
  elif choice in ('5'):
    base=float(input("Enter base: "))
    exp=float(input("Enter exponent: "))

    if choice == '1':
      print(num1, '+', num2, '=', add(num1, num2))
  
    if choice == '2':
      print(num1, '-', num2, '=', sub(num1, num2))
  
    if choice == '3':
      print(num1, 'x', num2, '=', mult(num1, num2))
  
    if choice == '4':
      print(num1, '/', num2, '=', div(num1, num2))
  
    if choice == '5':
      print(base, '^', exp, '=', power(base, exp))

    next_calc=(input("Would you like to perform another calculation? y/n \n"))
    if next_calc == 'n':
      break

  else:
    print("Invalid input!")