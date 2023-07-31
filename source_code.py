logo = """
 _____________________
|  _________________  |
| |                 | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""
print(logo)
def add(n1, n2):
  return n1 + n2

def sub(n1 , n2):
  return n1 - n2

def mul(n1 , n2):
  return n1 * n2

def div(n1 , n2):
  return n1 / n2

operators = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}

def calculator():                  ###########################################################33##   recursion   ########################################################
  num1 = float(input("first number "))
  for symbol in operators:
    print(symbol)
  want_to_continue = False
  while not want_to_continue:
      operation = input("pick the operation to do ")
      num2 = float(input("next number "))
      calculation = operators[operation]
      answer = calculation(num1,num2)
      print(f"{num1} {operation} {num2} = {answer} ")
      again = input(f"do you want to continue with the {answer} 'y' for yes 'n' for no ")
      if  again == "y":
        num1 =  answer
      elif again == "n":
        want_to_continue = True
        calculator()#               <<---------------------------------------------------------------------recursion

calculator()
