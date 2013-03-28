#Scott Snow
#Comp 141, Homework 7
#Python Calculator (calculator.py)

from calcExceptions import CalcExceptions
import token

#Scanner Class
#Takes in user input and splits into tokens
class Scanner:
    def __init__(self):
        self.tokens = list()
        self.cursor = 0
        self.EndExp = False
        self.CharNext = ''
        self.expr = ""

    def parseExpression(self, expression):
        self.tokens = list()
        self.expr = expression
        self.EndExp = False
        self.cursor = -1
        self.advCursor()
        self.token = None
        while True:
            self.token = self.getNextToken()
            if self.token is not None and self.EndExp is False:
                self.tokens.append(self.token)
            else:
                break
        return self.tokens

    def getNextToken(self):
        self.token = None
        if self.CharNext == " ":
            self.EndExp = True
        if self.EndExp is True:
            self.token = None
        elif self.isParenthesis(self.CharNext):
            self.token = token.ParenToken(self.CharNext)
            self.advCursor()
        elif self.isOperator(self.CharNext):
            self.token = token.OperatorToken(self.CharNext)
            self.advCursor()
        elif self.isDigitOrDecimal(self.CharNext):
            self.token = token.NumberToken(self.scanNumber())
        else:
            return self.token
        return self.token

    def scanNumber(self):
        self.isDigit = False
        self.wholePart = 0.0
        self.fractionalPart = 0.0
        self.fractionalMultiplier = 0.1
        self.past_decimal = False
        while self.EndExp is False and self.isDigitOrDecimal(self.CharNext):
            if self.CharNext == '.':
                if self.past_decimal:
                    raise CalcExceptions("badly formed number - multiple decimal points")
                self.past_decimal = True
            elif self.isDigitOrDecimal(self.CharNext):
                self.isDigit = True
                if self.past_decimal is False:
                    self.wholePart = int(self.wholePart) * 10 + int(self.CharNext)
                else:
                    self.fractionalPart += int(self.CharNext) * self.fractionalMultiplier
                    self.fractionalMultiplier /= 10.0
            self.advCursor()
        if self.isDigit is False:
            raise CalcExceptions("badly formed number - decimal point with no digits")
        return self.wholePart + self.fractionalPart

    def advCursor(self):
        self.cursor += 1
        if self.cursor >= len(self.expr):
            self.EndExp = True
        else:
            self.CharNext = self.expr[self.cursor]

    def isWhiteSpace(self, c):
        if (c == ' ') or (c == '\t') or (c == '\n'):
            return True

    def isParenthesis(self, c):
        if (c == '(') or (c == ')'):
            return True

    def isOperator(self, c):
        if (c == '+') or (c == '-') or (c == '*') or (c == '/') or (c == '~'):
            return True

    def isDigitOrDecimal(self, c):
        if ('0' <= c <= '9') or (c == '.'):
            return True
