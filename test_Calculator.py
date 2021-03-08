from Calculator import Calculator


def testIsOperand():
    calculator = Calculator()
    assert calculator.isOperand("22.3321") == True, "Should be True."
    assert calculator.isOperand(".99") == True, "Should be True."
    assert calculator.isOperand("-12121") == True, "Should be True."
    assert calculator.isOperand("+123124") == True, "Should be True."
    assert calculator.isOperand("-.002") == True, "Should be True."
    assert calculator.isOperand("-+") == True, "Should be True."
    assert calculator.isOperand("++") == True, "Should be True."
    assert calculator.isOperand("/*") == False, "Should be False."
    assert calculator.isOperand("cinnamon") == False, "Should be False."


def testApplyOperator():
    calculator = Calculator()
    assert calculator.applyOperator(1, 1, "+") == 2, "Should be 2."
    assert calculator.applyOperator(3, 2, "-") == 1, "Should be 1."
    assert calculator.applyOperator(2, 2, "*") == 4, "Should be 4."
    assert calculator.applyOperator(25, 5, "/") == 5, "Should be 5."
    assert calculator.applyOperator(443, 1, "/") == 443, "Should be 443."


def testEvaluatePostfixExp():
    calculator = Calculator()
    assert calculator.evaluatePostfixExp("4 2 - 3.5 *") == 7.0, "Should be 7."
    assert calculator.evaluatePostfixExp("1 2 +") == 3, "Should be 3."
    assert calculator.evaluatePostfixExp("4 5 * 2 /") == 10, "Should be 10."
    assert calculator.evaluatePostfixExp("-5 -8 + -11 2 * -") == 9, "Should be 9."
    assert calculator.evaluatePostfixExp("-.32 .5 /") == -0.64, "Should be -0.64."


def main():
    testIsOperand()
    testApplyOperator()
    testEvaluatePostfixExp()


if __name__ == "__main__":
    main()
