#Scott Snow
#Comp 141, Homework 7
#Python Calculator (calculator.py)

from expressionTree import NumberExpressionTree, OperatorExpressionTree

class Evaluators:
    def __init__(self):
        pass
    def evaluate(self, root):
        if isinstance(root, NumberExpressionTree):
            return root.getNumber()
        oper = root.getOperator()
        if oper == '~':
            return -1.0 * self.evaluate(root.right)
        else:
            leftChild = self.evaluate(root.left)
            rightChild = self.evaluate(root.right)
            if oper == '+':
                return leftChild + rightChild
            elif oper == '-':
                return leftChild - rightChild
            elif oper == '*':
                return leftChild * rightChild
            elif oper == '/':
                try:
                    return leftChild / rightChild
                except ZeroDivisionError:
                    return float('Inf')
        return 0.0
