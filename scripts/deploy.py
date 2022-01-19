from ssl import VERIFY_DEFAULT
from brownie import SimpleCalculator
from scripts.helpful_scripts import get_account
from scripts.calculator_ascii import calculator

def main():
    account = get_account()
    simple_calculator = SimpleCalculator.deploy({"from": account})
    print(f"Contract deployed to the blockchain at this {simple_calculator.address} address.")
    print(calculator)

    verify = False
    add_complete = False
    while not verify:
        choice = input('What arithmetic do you want to do now? Choose either add, subtract, divide or multiply: ').lower()
        option = ["add", "subtract", "divide", "multiply"]
        if choice not in option:
            print('Invalid response! Try again.')
        else:
            if choice == "add":
                numberArray = []
                try:
                    count = int(input("How many number do you want to add? E.g enter 5 to add five numbers! "))
                    if isinstance(count, int):
                        for num in range(count):
                            num = int(input('Enter numbers to add: '))
                            numberArray.append(num)
                    result = simple_calculator.add(numberArray)
                    print(f"Your result is {result}")
                    verify = True
                except ValueError as e:
                    print("Ooops! Wrong input. Insert only numeric figures")
            elif choice == "subtract": 
                num1 = input("Enter first number: ")
                num2 = input("Enter second number: ")
                tx = simple_calculator.subtract(num1, num2)
                print(f"Your result {tx.return_value}")
                verify = True
            elif choice == "multiply": 
                num1 = input("Enter first number: ")
                num2 = input("Enter second number: ")
                tx = simple_calculator.multiply(num1, num2)
                print(f"Your result is {tx.return_value}")
                verify = True
            elif choice == "divide": 
                num1 = input("Enter first number: ")
                num2 = input("Enter second number: ")
                tx = simple_calculator.divide(num1, num2)
                print(f"Your result is {tx.return_value}")
                verify = True
            else: 
                print("Wrong response! Try again.")
                verify = False            
    print('Calculation done!')
