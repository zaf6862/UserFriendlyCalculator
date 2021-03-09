class InputParser:
    """
    A helper class used to parse the user input. Assumes that the user input is in human readable (infix notation).

    ...

    Attributes
    ----------
    operands : str
        A string that lists all allowed operands (the decimal digits in this case).
    operators : str
        A string that lists all allowed operators.
    specialCharacters: str
        A string that lists all allowed special characters (parentheses in this case).
    precedence: Dictionary
        A dictionary that stores the precedence order of operators.


    Methods
    -------
    checkForInvalidInput(InputExpression)
        Checks if the InputExpression is invalid.

    checkForSyntaxError(InputExpression)
        Checks if the InputExpression is in correct infix notation.

    prettifyInputExpression(InputExpression)
        Modifies the InputExpression so that it can easily be converted from
        infix notation to postfix notation.

    isOperand(token)
        Checks if a given token is an operand or an operator.

    infixToPostfix(infixExpression)
        Converts an arithmetic expression from infix to postfix notation.

    parseInput(inputExpression)
        Checks the input for all kinds of errors and returns it in postfix notation
        if none are found.

    """

    def __init__(self):
        """
            Initializes the class variables.
        """
        self.operands = "0123456789."
        self.operators = "+-*/"
        self.specialCharacters = "() "
        self.precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    def checkForInvalidInput(self, inputExpression):
        """
        Checks if the inputExpression is invalid.

        Parameters
        ----------
        inputExpression : str
            The arithmetic expression that is input by the user.

        Returns
        ------
        True : bool
            If the inputExpression is invalid.
        False : bool
            If the inputExpression is valid.
        """

        validCharacters = self.operators + self.operands + self.specialCharacters
        for eachCharacter in inputExpression:
            if eachCharacter not in validCharacters:
                return True
        return False

    def checkForSyntaxError(self, inputExpression):
        """
        Checks if the InputExpression has a syntax error. Assumes the 
        input is in infix notation.

        Parameters
        ----------
        inputExpression : str
            The arithmetic expression that is input by the user.

        Returns
        ------
        True : bool
            If the inputExpression has a syntax error.
        False : bool
            If the inputExpression does not have a syntax error.
        """

        # Unbalanced parentheses.
        if inputExpression.count("(") != inputExpression.count(")"):
            return True
        # Last char is decimal.
        if inputExpression[len(inputExpression) - 1] == ".":
            return True
        else:
            # A digit does not immediately follow a decimal.
            for i in range(len(inputExpression)):
                if inputExpression[i] == ".":
                    if inputExpression[i + 1] not in "0123456789":
                        return True

        # Removing all the whitespaces. Makes things easy.
        inputExpression = inputExpression.replace(" ", "")
        # Input only has whitespaces.
        if len(inputExpression) == 0:
            return True

        i = 0
        while i < len(inputExpression):
            # Last character is an operator.
            if i == len(inputExpression) - 1 and inputExpression[i] in self.operators:
                return True
            # Last two characters are operators.
            elif i == len(inputExpression) - 2 and inputExpression[i] in self.operators \
                    and inputExpression[i + 1] in self.operators:
                return True
            else:
                if inputExpression[i] in self.operators:
                    # Two operators next to each other but the second is * or /.
                    if inputExpression[i + 1] in "*/":
                        return True
                    # Two operators next to each other. Second one is either + or -.
                    # Third character is not an operand.
                    elif inputExpression[i + 1] in "+-" and inputExpression[i + 2] not in self.operands:
                        return True
                    elif inputExpression[i + 1] in "+-" and inputExpression[i + 2] in self.operands:
                        if i == 0 or (i >= 1 and inputExpression[i - 1] not in self.operands):
                            return True

            i += 1
        return False

    def prettifyInputExpression(self, inputExpression):
        """
        Prepares the input for conversion to postfix notation. Assumes input is valid
        with no syntax error. Works in three steps 1) Split up whole expression into
        operators and operands 2) Join + or - with operands to make signed
        numbers (if any) 3) Concatenate the whole expression with each operator and operand
        separated by a whitespace.

        Parameters
        ----------
        inputExpression : str
            The arithmetic expression that is input by the user.

        Returns
        ------
        prettyInputExpression: str
            InputExpression in its pretty form.

        """

        # removing all the whitespaces. Makes things easy.
        inputExpression = inputExpression.replace(" ", "")
        i = 0
        splitUpInputExpression = []
        while i < len(inputExpression):
            # if char is operand then loop till the entire number is read.
            if inputExpression[i] in self.operands:
                operand = inputExpression[i]
                i += 1
                while i < len(inputExpression):
                    if inputExpression[i] in self.operands:
                        operand += inputExpression[i]
                        i += 1
                    else:
                        break
                splitUpInputExpression.append(operand)
            else:
                # else just add the operator as is.
                splitUpInputExpression.append(inputExpression[i])
                i += 1

        prettyInputExpression = ""
        # If first token is + or - then the number that follows is signed.
        if splitUpInputExpression[0] in "+-":
            prettyInputExpression += splitUpInputExpression[0]
            i = 1
        else:
            i = 0
        while i < len(splitUpInputExpression):
            # If current token is + or - and it succeeds an operator
            # then the number that follows is signed.
            if splitUpInputExpression[i] in "+-" and \
                    splitUpInputExpression[i-1] in self.operators \
                    and self.isOperand(splitUpInputExpression[i+1]):
                prettyInputExpression += splitUpInputExpression[i]
                prettyInputExpression += splitUpInputExpression[i + 1]
                prettyInputExpression += " "
                i += 2
            # Else the token is an operator or an unsigned operand.
            else:
                prettyInputExpression += splitUpInputExpression[i] + " "
                i += 1
        prettyInputExpression = prettyInputExpression.strip()

        return prettyInputExpression

    def isOperand(self, token):
        """
        Check if a given token is an operand.

        Parameters
        ----------
        token : str
            A string that can either be an operand or an operator.

        Returns
        ------
        True : bool
            If token is operand.
        False: bool
            If token is not operand.
        """
        if len(token) == 1:
            if token in self.operands:
                return True
        elif len(token) > 1:
            validChars = self.operands + '+-'
            for eachChar in token:
                if eachChar not in validChars:
                    return False
            return True

    def infixToPostfix(self, infixExpression):
        """
        Converts the inputExpression from infix notation to postfix notation using
        the shunting yard algorithm. This method is adapted from an online tutorial
        (https://cutt.ly/czfwRLw).The online version of this code was very basic and
        I added the following things myself:
        1) Support for decimal numbers.
        2) Support for signed numbers.
        3) Support for parentheses.
        4) Error handling and robustness in face of crashes (e.g. handling division by zero errors).
        5) Changed the stack to use the standard python list data structure rather than a
         proprietary stack data structure that was originally used.

        Parameters
        ----------
        infixExpression : str
            The arithmetic expression that is input by the user in its infix form.

        Returns
        ------
        postfixExpression : str
            The arithmetic expression that is input by the user in its postfix form.

        """

        operatorStack = []
        postfixList = []
        tokenList = infixExpression.split(" ")  # prettified expression comes in handy here.

        for token in tokenList:
            # Token is operand. Push it to the postfix list.
            if self.isOperand(token):
                postfixList.append(token)
            elif token == '(':
                operatorStack.append(token)
            elif token == ')':
                topOperator = operatorStack.pop()
                # Keep popping operators until opening parentheses is popped.
                while topOperator != '(':
                    postfixList.append(topOperator)
                    topOperator = operatorStack.pop()

            else:  # Token is an operator. Push it on the stack.
                while (len(operatorStack) > 0) and \
                        (self.precedence[operatorStack[len(operatorStack) - 1]] >= self.precedence[token]):
                    postfixList.append(operatorStack.pop())
                operatorStack.append(token)

        # There might still be operators left on the stack.
        while len(operatorStack) > 0:
            postfixList.append(operatorStack.pop())

        postfixExpression = " ".join(postfixList)
        return postfixExpression

    def parseInput(self, inputExpression):
        """
        Parses the user input. Checks for errors. If none are found, prettifies the user
        input and converts it from infix to postfix notation.

        Parameters
        ----------
        inputExpression : str
            The arithmetic expression that is input by the user.

        Returns
        ------
        None:
            If the InputExpression has an error.

        inputExpression : str
            InputExpression in its postfix form, if it has no errors.

        """

        try:
            if len(inputExpression) == 0:
                raise ValueError("Empty expression. Please enter a valid arithmetic expression.")
            if "\"" in inputExpression:
                inputExpression = inputExpression.split("\"")[1]
            if self.checkForInvalidInput(inputExpression):
                raise ValueError("Invalid input. Please enter a valid arithmetic expression.")
            if self.checkForSyntaxError(inputExpression):
                raise SyntaxError("Syntax error. Please enter a valid arithmetic expression.")

            # No errors detected. Time to prettify the input.
            inputExpression = self.prettifyInputExpression(inputExpression)
            inputExpression = self.infixToPostfix(inputExpression)
            return inputExpression

        except Exception as error:
            print("Error: " + str(error))
            return None
