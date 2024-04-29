# Generated from Fourier.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FourierParser import FourierParser
else:
    from FourierParser import FourierParser

# This class defines a complete listener for a parse tree produced by FourierParser.
class FourierListener(ParseTreeListener):

    # Enter a parse tree produced by FourierParser#start.
    def enterStart(self, ctx:FourierParser.StartContext):
        pass

    # Exit a parse tree produced by FourierParser#start.
    def exitStart(self, ctx:FourierParser.StartContext):
        pass


    # Enter a parse tree produced by FourierParser#expr.
    def enterExpr(self, ctx:FourierParser.ExprContext):
        pass

    # Exit a parse tree produced by FourierParser#expr.
    def exitExpr(self, ctx:FourierParser.ExprContext):
        pass


    # Enter a parse tree produced by FourierParser#function.
    def enterFunction(self, ctx:FourierParser.FunctionContext):
        pass

    # Exit a parse tree produced by FourierParser#function.
    def exitFunction(self, ctx:FourierParser.FunctionContext):
        pass


    # Enter a parse tree produced by FourierParser#sinFunction.
    def enterSinFunction(self, ctx:FourierParser.SinFunctionContext):
        pass

    # Exit a parse tree produced by FourierParser#sinFunction.
    def exitSinFunction(self, ctx:FourierParser.SinFunctionContext):
        pass


    # Enter a parse tree produced by FourierParser#cosFunction.
    def enterCosFunction(self, ctx:FourierParser.CosFunctionContext):
        pass

    # Exit a parse tree produced by FourierParser#cosFunction.
    def exitCosFunction(self, ctx:FourierParser.CosFunctionContext):
        pass


    # Enter a parse tree produced by FourierParser#exponent.
    def enterExponent(self, ctx:FourierParser.ExponentContext):
        pass

    # Exit a parse tree produced by FourierParser#exponent.
    def exitExponent(self, ctx:FourierParser.ExponentContext):
        pass



del FourierParser