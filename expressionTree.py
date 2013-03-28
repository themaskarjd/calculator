#Scott Snow
#Comp 141, Homework 7
#Python Calculator (calculator.py)

class ExpressionTree(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

class OperatorExpressionTree(ExpressionTree):
    def __init__(self, data, left, right):
        ExpressionTree.__init__(self)
        self.data = data
        self.left = left
        self.right = right
    def getOperator(self):
        return self.data

class NumberExpressionTree(ExpressionTree):
    def __init__(self, data):
        ExpressionTree.__init__(self)
        self.data = data
    def getNumber(self):
        return self.data
