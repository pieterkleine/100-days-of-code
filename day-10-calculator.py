def addition(n1, n2):
  """Takes two integers or floats and adds them together."""
  return n1 + n2

def subtract(n1, n2):
  """Takes two integers or floats and subtracts the second from the first."""
  return n1 - n2

def multiply(n1, n2):
  """Takes two integers or floats and multiplies them."""
  return n1 * n2

def divide(n1, n2):
  """Takes two integers or floats and divides the first by the second."""
  return n1 / n2

operations = {
  "+": addition, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

def calculator():
  """
  Simple calculator which asks for two numbers (floats) and performs the requested operation. The calculator provides the option to use the answer as the first number in a new calculation.
  """
  from art3 import logo
  print(logo)
  num1 = float(input("What's the first number?: "))
  keep_calculating = True

  while keep_calculating == True:
    for operation in operations:
      print(operation)
    operator = input("Choose the operation from the line above: ")

    num2 = float(input("What's the next number?: "))

    function = operations[operator]
    answer = function(num1, num2)

    print(f"{num1} {operator} {num2} = {answer}")

    next = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type any other character to exit.: ")
    if next == 'n':
      keep_calculating = False
      calculator()
    elif next =='y':
      num1 = answer
    else:
      return

calculator()