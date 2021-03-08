from InputParser import InputParser


def testCheckForInvalidInput():
    inputParser = InputParser()
    assert inputParser.checkForInvalidInput("1 + 2") == False, "Should be valid."
    assert inputParser.checkForInvalidInput("4*5/2") == False, "Should be valid."
    assert inputParser.checkForInvalidInput("-5+-8--11*2") == False, "Should be valid."
    assert inputParser.checkForInvalidInput("-.32       /.5") == False, "Should be valid."
    assert inputParser.checkForInvalidInput("(4-2)*3.5") == False, "Should be valid."
    assert inputParser.checkForInvalidInput("2+-+-4") == False, "Should be invalid."
    assert inputParser.checkForInvalidInput("19 + cinnamon") == True, "Should be invalid."


def testCheckForSyntaxError():
    inputParser = InputParser()
    assert inputParser.checkForSyntaxError("1 + 2") == False, "Should be correct syntax."
    assert inputParser.checkForSyntaxError("4*5/2") == False, "Should be correct syntax."
    assert inputParser.checkForSyntaxError("-5+-8--11*2") == False, "Should be correct syntax."
    assert inputParser.checkForSyntaxError("-.32       /.5") == False, "Should be correct syntax."
    assert inputParser.checkForSyntaxError("(4-2)*3.5") == False, "Should be correct syntax."
    assert inputParser.checkForSyntaxError("19 + cinnamon") == False, "Should be correct syntax."
    assert inputParser.checkForSyntaxError("2+-+-4") == True, "Should be incorrect syntax."
    assert inputParser.checkForSyntaxError("       ") == True, "Should be incorrect syntax."
    assert inputParser.checkForSyntaxError("+-+-4") == True, "Should be incorrect syntax."
    assert inputParser.checkForSyntaxError("+-+-") == True, "Should be incorrect syntax."
    assert inputParser.checkForSyntaxError("2+-+-/*+4") == True, "Should be incorrect syntax."


def testPrettifyInputExpression():
    inputParser = InputParser()
    assert inputParser.prettifyInputExpression("(1+2)") == "( 1 + 2 )", "Did not prettify correctly."
    assert inputParser.prettifyInputExpression("4*5/2") == "4 * 5 / 2", "Did not prettify correctly."
    assert inputParser.prettifyInputExpression("-5+-8--11*2") == "-5 + -8 - -11 * 2", "Did not prettify correctly."
    assert inputParser.prettifyInputExpression("-.32       /.5") == "-.32 / .5", "Did not prettify correctly."
    assert inputParser.prettifyInputExpression("(4-2)*3.5") == "( 4 - 2 ) * 3.5", "Did not prettify correctly."


def testIsOperand():
    inputParser = InputParser()
    assert inputParser.isOperand("22.3321") == True, "Should be True."
    assert inputParser.isOperand(".99") == True, "Should be True."
    assert inputParser.isOperand("-12121") == True, "Should be True."
    assert inputParser.isOperand("+123124") == True, "Should be True."
    assert inputParser.isOperand("-.002") == True, "Should be True."
    assert inputParser.isOperand("-+") == True, "Should be True."
    assert inputParser.isOperand("++") == True, "Should be True."
    assert inputParser.isOperand("/*") == False, "Should be False."
    assert inputParser.isOperand("cinnamon") == False, "Should be False."


def testInfixToPostfix():
    inputParser = InputParser()
    assert inputParser.infixToPostfix("( 4 - 2 ) * 3.5") == "4 2 - 3.5 *", "Should be correct."
    assert inputParser.infixToPostfix("-.32 / .5") == "-.32 .5 /", "Should be correct."
    assert inputParser.infixToPostfix("-5 + -8 - -11 * 2") == "-5 -8 + -11 2 * -", "Should be correct."
    assert inputParser.infixToPostfix("4 * 5 / 2") == "4 5 * 2 /", "Should be correct."
    assert inputParser.infixToPostfix("4 * 5 / 2") != "4 5 * / 2 ", "Should be correct."


def testParseInput():
    inputParser = InputParser()
    assert inputParser.parseInput("calculate \"(4-2)*3.5\"") == "4 2 - 3.5 *", "Should be correct."
    assert inputParser.parseInput("calculate \"1 + 2\"") == "1 2 +", "Should be correct."
    assert inputParser.parseInput("calculate \"4*5/2\"") == "4 5 * 2 /", "Should be correct."
    assert inputParser.parseInput("calculate \"-5+-8--11*2\"") == "-5 -8 + -11 2 * -", "Should be correct."
    assert inputParser.parseInput("calculate \"-.32       /.5\"") == "-.32 .5 /", "Should be correct."
    assert inputParser.parseInput("calculate \"2+-+-4\"") == None, "Should be None."
    assert inputParser.parseInput("calculate \"19 + cinnamon\"") == None, "Should be None."




def main():
    testCheckForInvalidInput()
    testCheckForSyntaxError()
    testPrettifyInputExpression()
    testIsOperand()
    testInfixToPostfix()
    testParseInput()


if __name__ == "__main__":
    main()
