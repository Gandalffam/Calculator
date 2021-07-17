# Calculator program lets gooooo §(*￣▽￣*)§

class Calculator:
    def __init__(self, first_value, second_value, operator):
        self.first_value = first_value
        self.second_value = second_value
        self.operator = operator
    
    def add(self):
        print("The result is %.3f" % (self.first_value + self.second_value))
    
    def subtract(self):
        print("The result is %.3f" % (self.first_value - self.second_value))
    
    def multiply(self):
        print("The result is %.3f" % (self.first_value * self.second_value))
    
    def divide(self):
        print("The result is %.3f" % (self.first_value / self.second_value))

    def calculate(self):
        if self.operator == "*":
            Calculator.multiply(self)
        elif self.operator == "+":
            Calculator.add(self) 
        elif self.operator == "-":
            Calculator.subtract(self)
        elif self.operator == "/":
            Calculator.divide(self)
        else:
            print("Invalid operator")
            return "Invalid"

condition = True

while condition:

    while True:
        try:
            first_val = float(input("Enter the first value: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue
        else:
            break

    Operator = input("Enter operator (*,+,-,/): ")

    while True: 
        try:
            second_val = float(input("Enter the second value: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue
        else:
            break

    print("Calculating...")

    Calculation = Calculator(first_val, second_val, Operator)
    traceback = Calculation.calculate()
    
    if traceback == "Invalid":
        print("Restarting program.")
        continue
    elif traceback != "Invalid":
        askRestart = input("Calculation finished. Exit program? (y/n): ")
        if askRestart == "y":
            condition = False
        elif askRestart == "n":
            print("Restarting program.")
            continue
        else:
            print("Unknown input. Restarting program.")
            continue







