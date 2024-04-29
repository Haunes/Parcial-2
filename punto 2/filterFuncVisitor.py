# Generated from filterFunc.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .filterFuncParser import filterFuncParser
else:
    from filterFuncParser import filterFuncParser

# This class defines a complete generic visitor for a parse tree produced by filterFuncParser.

class filterFuncVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by filterFuncParser#start.
    def visitStart(self, ctx:filterFuncParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filterFuncParser#function.
    def visitFunction(self, ctx:filterFuncParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filterFuncParser#iterable.
    def visitIterable(self, ctx:filterFuncParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filterFuncParser#list.
    def visitList(self, ctx:filterFuncParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filterFuncParser#tuple.
    def visitTuple(self, ctx:filterFuncParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filterFuncParser#elements.
    def visitElements(self, ctx:filterFuncParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filterFuncParser#element.
    def visitElement(self, ctx:filterFuncParser.ElementContext):
        return self.visitChildren(ctx)



del filterFuncParser