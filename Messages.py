class Messages:
    """
    This class stores all messages the calculator can produce.
    It keeps the main file clutter-free.
    """

    def __init__(self):
        self.welcomeMessage = "Welcome to the user-friendly calculator. \nPlease type in your expression to evaluate " \
                              "it.\n" \
                              "You can quit the program by typing \"exit\".\n" \
                              "To get help about the calculator, please type \"help\". \n\n "
        self.exitMessage = "Thank you for using the calculator. The program will close now."
        self.helpMessage = "\nFollowing are the key things you should know about the calculator: \n" \
                           "1) You should write your arithmetic expressions in human readable form (infix notation).\n" \
                           "2) You can use negative numbers as well as floats. \n" \
                           "3) Your query should be of the form \"calculate \"1 + 2\"\". \n" \
                           "4) Division by zero is handled by the calculator.\n" \
                           "5) You cannot use english alphabets in your expressions. \n" \
                           "6) You can type \"exit\" to quit the program at any time. \n\n"
