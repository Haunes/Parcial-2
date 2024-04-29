# Generated from Fourier.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("-\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4\34")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2(\2\16\3\2\2\2\4")
        buf.write("\21\3\2\2\2\6\33\3\2\2\2\b\35\3\2\2\2\n\"\3\2\2\2\f\'")
        buf.write("\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21\22")
        buf.write("\7\5\2\2\22\23\7\7\2\2\23\24\5\6\4\2\24\25\7\6\2\2\25")
        buf.write("\26\5\f\7\2\26\27\7\b\2\2\27\5\3\2\2\2\30\34\7\t\2\2\31")
        buf.write("\34\5\b\5\2\32\34\5\n\6\2\33\30\3\2\2\2\33\31\3\2\2\2")
        buf.write("\33\32\3\2\2\2\34\7\3\2\2\2\35\36\7\3\2\2\36\37\7\7\2")
        buf.write("\2\37 \5\4\3\2 !\7\b\2\2!\t\3\2\2\2\"#\7\4\2\2#$\7\7\2")
        buf.write("\2$%\5\4\3\2%&\7\b\2\2&\13\3\2\2\2\'(\7\13\2\2()\7\7\2")
        buf.write("\2)*\7\t\2\2*+\7\b\2\2+\r\3\2\2\2\3\33")
        return buf.getvalue()


class FourierParser ( Parser ):

    grammarFileName = "Fourier.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sin'", "'cos'", "'\u222B'", "'.'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "'e^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INTEGRAL", 
                      "DOT", "LPAREN", "RPAREN", "ID", "WS", "EXP" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_function = 2
    RULE_sinFunction = 3
    RULE_cosFunction = 4
    RULE_exponent = 5

    ruleNames =  [ "start", "expr", "function", "sinFunction", "cosFunction", 
                   "exponent" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INTEGRAL=3
    DOT=4
    LPAREN=5
    RPAREN=6
    ID=7
    WS=8
    EXP=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(FourierParser.ExprContext,0)


        def EOF(self):
            return self.getToken(FourierParser.EOF, 0)

        def getRuleIndex(self):
            return FourierParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = FourierParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.expr()
            self.state = 13
            self.match(FourierParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGRAL(self):
            return self.getToken(FourierParser.INTEGRAL, 0)

        def LPAREN(self):
            return self.getToken(FourierParser.LPAREN, 0)

        def function(self):
            return self.getTypedRuleContext(FourierParser.FunctionContext,0)


        def DOT(self):
            return self.getToken(FourierParser.DOT, 0)

        def exponent(self):
            return self.getTypedRuleContext(FourierParser.ExponentContext,0)


        def RPAREN(self):
            return self.getToken(FourierParser.RPAREN, 0)

        def getRuleIndex(self):
            return FourierParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = FourierParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(FourierParser.INTEGRAL)
            self.state = 16
            self.match(FourierParser.LPAREN)
            self.state = 17
            self.function()
            self.state = 18
            self.match(FourierParser.DOT)
            self.state = 19
            self.exponent()
            self.state = 20
            self.match(FourierParser.RPAREN)
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
            return self.getToken(FourierParser.ID, 0)

        def sinFunction(self):
            return self.getTypedRuleContext(FourierParser.SinFunctionContext,0)


        def cosFunction(self):
            return self.getTypedRuleContext(FourierParser.CosFunctionContext,0)


        def getRuleIndex(self):
            return FourierParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = FourierParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FourierParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(FourierParser.ID)
                pass
            elif token in [FourierParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.sinFunction()
                pass
            elif token in [FourierParser.T__1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.cosFunction()
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

    class SinFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(FourierParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(FourierParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(FourierParser.RPAREN, 0)

        def getRuleIndex(self):
            return FourierParser.RULE_sinFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinFunction" ):
                listener.enterSinFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinFunction" ):
                listener.exitSinFunction(self)




    def sinFunction(self):

        localctx = FourierParser.SinFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sinFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(FourierParser.T__0)
            self.state = 28
            self.match(FourierParser.LPAREN)
            self.state = 29
            self.expr()
            self.state = 30
            self.match(FourierParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CosFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(FourierParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(FourierParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(FourierParser.RPAREN, 0)

        def getRuleIndex(self):
            return FourierParser.RULE_cosFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosFunction" ):
                listener.enterCosFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosFunction" ):
                listener.exitCosFunction(self)




    def cosFunction(self):

        localctx = FourierParser.CosFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cosFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(FourierParser.T__1)
            self.state = 33
            self.match(FourierParser.LPAREN)
            self.state = 34
            self.expr()
            self.state = 35
            self.match(FourierParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXP(self):
            return self.getToken(FourierParser.EXP, 0)

        def LPAREN(self):
            return self.getToken(FourierParser.LPAREN, 0)

        def ID(self):
            return self.getToken(FourierParser.ID, 0)

        def RPAREN(self):
            return self.getToken(FourierParser.RPAREN, 0)

        def getRuleIndex(self):
            return FourierParser.RULE_exponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponent" ):
                listener.enterExponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponent" ):
                listener.exitExponent(self)




    def exponent(self):

        localctx = FourierParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exponent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(FourierParser.EXP)
            self.state = 38
            self.match(FourierParser.LPAREN)
            self.state = 39
            self.match(FourierParser.ID)
            self.state = 40
            self.match(FourierParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





