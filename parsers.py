#Scott Snow
#Comp 141, Homework 7
#Python Calculator (calculator.py)

from calcExceptions import CalcExceptions
import expressionTree
from token import TokenType

#Parsers class - parses tokens
class Parsers:
    def __init__(self):
        self.tokens = list()
        self.tokenIterator = 0
        self.currentToken = None
        self.eTree = None

    def parse(self, tokens):
        if len(tokens) == 1:
            raise CalcExceptions("Parser received an empty token list.")
        self.tokens = tokens
        self.currentToken = self.tokens[0]
        eTree = self.parseExpression()
        if self.currentToken is not None:
            raise CalcExceptions("Unconsumed tokens at end of expression.")
        return eTree

    def consumeToken(self):
        if self.tokenIterator <= self.tokens.index(self.tokens[-1]):
            self.tokenIterator += 1
        if self.tokenIterator > self.tokens.index(self.tokens[-1]):
            self.currentToken = None
        else:
            self.currentToken = self.tokens[self.tokenIterator]

    def parseExpression(self):
        expr = self.parseTerm()
        while self.currentToken is not None and self.currentToken.getType() == TokenType.OPERATOR_TOKEN and (
                    self.currentToken.getValue() == '+' or self.currentToken.getValue() == '-'):
            oper = self.currentToken.getValue()
            self.consumeToken()
            expr = expressionTree.OperatorExpressionTree(oper, expr, self.parseTerm())
        return expr

    def parseTerm(self):
        term = self.parseFactor()
        while self.currentToken is not None and self.currentToken.getType() == TokenType.OPERATOR_TOKEN and (
                    self.currentToken.getValue() == '*' or self.currentToken.getValue() == '/'):
            oper = self.currentToken.getValue()
            self.consumeToken()
            term = expressionTree.OperatorExpressionTree(oper, term, self.parseFactor())
        return term

    def parseFactor(self):
        if self.currentToken is None:
            raise CalcExceptions('Reached end of tokens while expecting a number.')
        factor = None
        if self.currentToken.getType() == TokenType.PAREN_TOKEN and self.currentToken.getValue() == '(':
            self.consumeToken()
            factor = self.parseExpression()
            if self.currentToken is None or self.currentToken.getValue() != ')':
                raise CalcExceptions('Badly formed parenthesized expression.')
            self.consumeToken()
        elif self.currentToken.getType() == TokenType.OPERATOR_TOKEN and self.currentToken.getValue() == '~':
            self.consumeToken()
            subExpr = self.parseNumber()
            factor = expressionTree.OperatorExpressionTree('~', None, subExpr)
        else:
            factor = self.parseNumber()
        return factor


    def parseNumber(self):
        if self.currentToken is None:
            raise CalcExceptions('Reached end of tokens while expecting a number.')
        if self.currentToken.getType() == TokenType.NUMBER_TOKEN:
            value = self.currentToken.getValue()
            self.consumeToken()
            return expressionTree.NumberExpressionTree(value)
        else:
            raise CalcExceptions("Expected a number.")
