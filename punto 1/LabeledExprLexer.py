# Generated from LabeledExpr.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("A\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\6\n-\n\n\r\n\16\n.\3\13\6\13\62\n\13\r\13\16")
        buf.write("\13\63\3\f\5\f\67\n\f\3\f\3\f\3\r\6\r<\n\r\r\r\16\r=\3")
        buf.write("\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\3\2\5\4\2C\\c|\3\2\62;\4\2\13\13\"\"")
        buf.write("\2D\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3")
        buf.write("\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2")
        buf.write("\2\r%\3\2\2\2\17\'\3\2\2\2\21)\3\2\2\2\23,\3\2\2\2\25")
        buf.write("\61\3\2\2\2\27\66\3\2\2\2\31;\3\2\2\2\33\34\7?\2\2\34")
        buf.write("\4\3\2\2\2\35\36\7*\2\2\36\6\3\2\2\2\37 \7+\2\2 \b\3\2")
        buf.write("\2\2!\"\7k\2\2\"\n\3\2\2\2#$\7,\2\2$\f\3\2\2\2%&\7\61")
        buf.write("\2\2&\16\3\2\2\2\'(\7-\2\2(\20\3\2\2\2)*\7/\2\2*\22\3")
        buf.write("\2\2\2+-\t\2\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2")
        buf.write("\2/\24\3\2\2\2\60\62\t\3\2\2\61\60\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\61\3\2\2\2\63\64\3\2\2\2\64\26\3\2\2\2\65\67\7\17")
        buf.write("\2\2\66\65\3\2\2\2\66\67\3\2\2\2\678\3\2\2\289\7\f\2\2")
        buf.write("9\30\3\2\2\2:<\t\4\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=")
        buf.write(">\3\2\2\2>?\3\2\2\2?@\b\r\2\2@\32\3\2\2\2\7\2.\63\66=")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class LabeledExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    MUL = 5
    DIV = 6
    ADD = 7
    SUB = 8
    ID = 9
    INT = 10
    NEWLINE = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'i'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "ID", "INT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "MUL", "DIV", "ADD", "SUB", 
                  "ID", "INT", "NEWLINE", "WS" ]

    grammarFileName = "LabeledExpr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


