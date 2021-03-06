class Calculator:
    """
    Main class that evaluates user's input.
    ...

    Attributes
    ----------
    operands : str
        A string that lists all allowed operands (the decimal digits in this case).

    Methods
    -------
    isOperand(token)
        Checks if a given token is an operand or not.

    applyOperator(operand1, operand2, operator)
        Takes the input operator and applies it to the two operands.

    evaluatePostfixExp(postfixExpression)
        Evaluates the given postfixExpression.

    evaluateExpression(userExpression):
        Calls the evaluatePostfixExp() method with user input as the parameter.

    """

    def __init__(self):
        self.operands = "0123456789."

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

    def applyOperator(self, operand1, operand2, operator):
        """
        Applies the operator to the two operands.

        Parameters
        ----------
        operand1 : Integer or Float
            The first operand.
        operand2 : Integer or Float
            The second operand.
        operator: str
            The arithmetic operator to be applied.

        Returns
        ------
            Result : Integer or Float
                The result of applying the operator to the two operands.
        """

        if operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2
        elif operator == "+":
            return operand1 + operand2
        else:
            return operand1 - operand2

    def evaluatePostfixExp(self, postfixExpr):
        """
        Evaluates an expression that's given in postfix notation. This code is
        adapted from an online tutorial (https://cutt.ly/czfwRLw). The online version
        of this code was very basic and I added the following things myself:
        1) Support for decimal numbers
        2) Error handling and robustness in face of crashes (e.g. handling division by zero errors).
        3) Changed the stack to use the standard python list data structure rather than a proprietary
         data structure that was originally used.

        Parameters
        ----------
        postfixExpr : str
            An arithmetic expression in postfix notation that needs to be evaluated.


        Returns
        ------
            Result : Integer or Float
                The result of evaluating the arithmetic expression.
        """

        operandStack = []
        tokenList = postfixExpr.split(" ")

        for token in tokenList:
            if self.isOperand(token):
                if "." in token:
                    token = float(token)
                else:
                    token = int(token)
                operandStack.append(token)
            else:  # token is an operator
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                try:
                    result = self.applyOperator(operand1, operand2, token)
                except Exception as error:
                    print("Invalid input. Please enter a valid arithmetic expression.")  # Most likely division by
                    # zero error.
                    return
                operandStack.append(result)
        return operandStack.pop()

    def evaluateExpression(self, userExpression):
        """
        Evaluates the arithmetic expression input by the user.
        Does not currently support unary arithmetic operators.
        So expressions like "--2" which are actually "-1 * -2", cannot be
        evaluated. Support for this feature can be added by changing the
        applyOperator method. Its parameters could be relaxed to have more than
        one operator instead of having just one operator and two operands.

        Parameters
        ----------
        userExpression : str
            The arithmetic expression input by the user in its postfix notation.

        Returns
        ------
            Result : Integer or Float
                The result from evaluatePostfixExp() method.
        """
        return self.evaluatePostfixExp(userExpression)
