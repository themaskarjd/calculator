#Scott Snow
#Comp 141, Homework 7
#Python Calculator (calculator.py)

class TokenType:
    NUMBER_TOKEN   = 'NUMBER_TOKEN'
    OPERATOR_TOKEN = 'OPERATOR_TOKEN'
    PAREN_TOKEN    = 'PAREN_TOKEN'

#Python Calculator (token.py)
#Abstract base class to be extended by other token classes
class Token:
    def __init__(self):
        pass
    def getType(self):
        return 0
    
#This class extends the base Token class
#Stores a real number
class NumberToken(Token):
    def __init__(self, value):
        Token.__init__(self)
        self.value = value
    def getType(self):
        return TokenType.NUMBER_TOKEN
    def getValue(self):
        return self.value

#This class extends the base Token class
#Stores an operator as a single character
class OperatorToken(Token):
    def __init__(self, value):
        Token.__init__(self)
        self.value = value
    def getType(self):
        return TokenType.OPERATOR_TOKEN
    def getValue(self):
        return self.value

#This class extends the base Token class
#Stores parentheses as a single character
class ParenToken(Token):
    def __init__(self, value):
        Token.__init__(self)
        self.value = value
    def getType(self):
        return TokenType.PAREN_TOKEN
    def getValue(self):
        return self.value
