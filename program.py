# Calculator program lets gooooo §(*￣▽￣*)§

class Calculator:
    def __init__(self, first_value, second_value, operator):
        self.first_value = first_value
        self.second_value = second_value
        self.operator = operator

    def add(self):
        return "The result is %.3f" % (self.first_value + self.second_value)
    
    def subtract(self):
        return "The result is %.3f" % (self.first_value - self.second_value)
    
    def multiply(self):
        return "The result is %.3f" % (self.first_value * self.second_value)
    
    def divide(self):
        return "The result is %.3f" % (self.first_value / self.second_value)

    def askOperator(self):
        if self.operator == "*":
            print(Calculator.multiply(self))
        elif self.operator == "+":
            print(Calculator.add(self)) 
        elif self.operator == "-":
            print(Calculator.subtract(self)) 
        elif self.operator == "/":
            print(Calculator.divide(self))
        else:
            print("Invalid operator")
            return "Invalid"

condition = True

while condition:

    first_val = float(input("Enter the first value: "))
    Operator = input("Enter operator (*,+,-,/): ")
    second_val = float(input("Enter the second value: "))

    print("Calculating...")

    Calculation = Calculator(first_val, second_val, Operator)

    if Calculation.askOperator() == "Invalid":
        print("Restarting program.")
    elif Calculation.askOperator != "Invalid":
        askRestart = input("Calculation finished. Exit program? (y/n): ")
        if askRestart == "y":
            condition = False
        elif askRestart == "n":
            print("Restarting program.")
        else:
            print("Unknown input. Restarting program.")









