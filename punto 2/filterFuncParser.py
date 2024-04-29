# Generated from filterFunc.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,3,2,26,8,2,1,3,1,3,
        3,3,30,8,3,1,3,1,3,1,4,1,4,3,4,36,8,4,1,4,1,4,1,5,1,5,1,5,5,5,43,
        8,5,10,5,12,5,46,9,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,7,
        9,46,0,14,1,0,0,0,2,21,1,0,0,0,4,25,1,0,0,0,6,27,1,0,0,0,8,33,1,
        0,0,0,10,39,1,0,0,0,12,47,1,0,0,0,14,15,5,6,0,0,15,16,5,1,0,0,16,
        17,3,2,1,0,17,18,5,2,0,0,18,19,3,4,2,0,19,20,5,3,0,0,20,1,1,0,0,
        0,21,22,5,10,0,0,22,3,1,0,0,0,23,26,3,6,3,0,24,26,3,8,4,0,25,23,
        1,0,0,0,25,24,1,0,0,0,26,5,1,0,0,0,27,29,5,4,0,0,28,30,3,10,5,0,
        29,28,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,5,5,0,0,32,7,1,0,
        0,0,33,35,5,1,0,0,34,36,3,10,5,0,35,34,1,0,0,0,35,36,1,0,0,0,36,
        37,1,0,0,0,37,38,5,3,0,0,38,9,1,0,0,0,39,44,3,12,6,0,40,41,5,2,0,
        0,41,43,3,12,6,0,42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,
        1,0,0,0,45,11,1,0,0,0,46,44,1,0,0,0,47,48,7,0,0,0,48,13,1,0,0,0,
        4,25,29,35,44
    ]

class filterFuncParser ( Parser ):

    grammarFileName = "filterFunc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'['", "']'", "'FILTER'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FILTER", "INT", "FLOAT", 
                      "STRING", "ID", "WS" ]

    RULE_start = 0
    RULE_function = 1
    RULE_iterable = 2
    RULE_list = 3
    RULE_tuple = 4
    RULE_elements = 5
    RULE_element = 6

    ruleNames =  [ "start", "function", "iterable", "list", "tuple", "elements", 
                   "element" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    FILTER=6
    INT=7
    FLOAT=8
    STRING=9
    ID=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(filterFuncParser.FILTER, 0)

        def function(self):
            return self.getTypedRuleContext(filterFuncParser.FunctionContext,0)


        def iterable(self):
            return self.getTypedRuleContext(filterFuncParser.IterableContext,0)


        def getRuleIndex(self):
            return filterFuncParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = filterFuncParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(filterFuncParser.FILTER)
            self.state = 15
            self.match(filterFuncParser.T__0)
            self.state = 16
            self.function()
            self.state = 17
            self.match(filterFuncParser.T__1)
            self.state = 18
            self.iterable()
            self.state = 19
            self.match(filterFuncParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(filterFuncParser.ID, 0)

        def getRuleIndex(self):
            return filterFuncParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = filterFuncParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(filterFuncParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(filterFuncParser.ListContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(filterFuncParser.TupleContext,0)


        def getRuleIndex(self):
            return filterFuncParser.RULE_iterable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = filterFuncParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_iterable)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.list_()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.tuple_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(filterFuncParser.ElementsContext,0)


        def getRuleIndex(self):
            return filterFuncParser.RULE_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = filterFuncParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(filterFuncParser.T__3)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0):
                self.state = 28
                self.elements()


            self.state = 31
            self.match(filterFuncParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(filterFuncParser.ElementsContext,0)


        def getRuleIndex(self):
            return filterFuncParser.RULE_tuple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = filterFuncParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(filterFuncParser.T__0)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0):
                self.state = 34
                self.elements()


            self.state = 37
            self.match(filterFuncParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(filterFuncParser.ElementContext)
            else:
                return self.getTypedRuleContext(filterFuncParser.ElementContext,i)


        def getRuleIndex(self):
            return filterFuncParser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = filterFuncParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.element()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 40
                self.match(filterFuncParser.T__1)
                self.state = 41
                self.element()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(filterFuncParser.INT, 0)

        def FLOAT(self):
            return self.getToken(filterFuncParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(filterFuncParser.STRING, 0)

        def getRuleIndex(self):
            return filterFuncParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = filterFuncParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





