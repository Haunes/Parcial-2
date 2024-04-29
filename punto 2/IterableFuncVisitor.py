# Generated from IterableFunc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .IterableFuncParser import IterableFuncParser
else:
    from IterableFuncParser import IterableFuncParser

# This class defines a complete generic visitor for a parse tree produced by IterableFuncParser.

class IterableFuncVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IterableFuncParser#start.
    def visitStart(self, ctx:IterableFuncParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFuncParser#function.
    def visitFunction(self, ctx:IterableFuncParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFuncParser#iterable.
    def visitIterable(self, ctx:IterableFuncParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFuncParser#list.
    def visitList(self, ctx:IterableFuncParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFuncParser#tuple.
    def visitTuple(self, ctx:IterableFuncParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFuncParser#elements.
    def visitElements(self, ctx:IterableFuncParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFuncParser#element.
    def visitElement(self, ctx:IterableFuncParser.ElementContext):
        return self.visitChildren(ctx)



del IterableFuncParser