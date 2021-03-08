"""
This file is a very basic interface for the calculator.
It calls relevant functions as they are needed.
"""

from Calculator import Calculator
from InputParser import InputParser
from Messages import Messages


def main():
    inputParser = InputParser()
    calculator = Calculator()
    messages = Messages()
    print(messages.welcomeMessage)

    while True:
        userInput = input("Please input your expression: ")
        if userInput == "exit" or userInput == "Exit":
            print(messages.exitMessage)
            break
        elif userInput == "help" or userInput == "Help":
            print(messages.helpMessage)
        else:
            userExpression = inputParser.parseInput(userInput)
            if userExpression is None:
                continue
            result = calculator.evaluateExpression(userExpression)
            print("Answer: " + str(result))


if __name__ == "__main__":
    main()
