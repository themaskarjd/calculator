#Scott Snow
#Comp 141, Homework 7
#Python Calculator (calculator.py)

import evaluators
from parsers import Parsers
from token import TokenType
from calcExceptions import *
import scanner

#Function used to print a description of the token
#followed by the token itself
def printTokens(tokens):
    iterator = 0
    expressions = ''
    while iterator != len(tokens):
        if tokens[iterator].getType() == TokenType.NUMBER_TOKEN:
            print "Number:\t\t",
            print tokens[iterator].getValue()
            expressions += str(tokens[iterator].getValue()) + ' '
        elif tokens[iterator].getType() == TokenType.OPERATOR_TOKEN:
            print "Operator:\t",
            print tokens[iterator].getValue()
            expressions += str(tokens[iterator].getValue()) + ' '
        elif tokens[iterator].getType() == TokenType.PAREN_TOKEN:
            print "Parenthesis:\t",
            print tokens[iterator].getValue()
            expressions += str(tokens[iterator].getValue()) + ' '
        iterator += 1
    print 'Expression:',
    print expressions

def main():
    while True:
        print "\nPython Calculator: "
        line = list()
        while True:
            user_input = raw_input("Enter Expression: ")
            user_input = user_input.replace(' ', '')
            if user_input is not None and len(user_input.strip()) == 0:
                break
            user_input += " "
            line.append(user_input)
            break
        expr = line
        if len(expr) == 0:
            break
        try:
            scan = scanner.Scanner()
            tokens = list()
            tokens = scan.parseExpression(expr[0])
            printTokens(tokens)
            parsers = Parsers()
            expressionTree = parsers.parse(tokens)
            evaluator = evaluators.Evaluators()
            result = evaluator.evaluate(expressionTree)
            print '\nResult:',
            print result
        except CalcExceptions, x:
            print 'Error!:',
            print x.message


if __name__ == '__main__':
    main()
a = input("Enter number 1")
b = input("Enter number 2")
c = a + b
print(c)
