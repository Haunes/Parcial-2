# Generated from Fourier.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("\64\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\6\b\'\n\b\r\b")
        buf.write("\16\b(\3\t\6\t,\n\t\r\t\16\t-\3\t\3\t\3\n\3\n\3\n\2\2")
        buf.write("\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\4\4\2")
        buf.write("C\\c|\5\2\13\f\17\17\"\"\2\65\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\31\3")
        buf.write("\2\2\2\7\35\3\2\2\2\t\37\3\2\2\2\13!\3\2\2\2\r#\3\2\2")
        buf.write("\2\17&\3\2\2\2\21+\3\2\2\2\23\61\3\2\2\2\25\26\7u\2\2")
        buf.write("\26\27\7k\2\2\27\30\7p\2\2\30\4\3\2\2\2\31\32\7e\2\2\32")
        buf.write("\33\7q\2\2\33\34\7u\2\2\34\6\3\2\2\2\35\36\7\u222d\2\2")
        buf.write("\36\b\3\2\2\2\37 \7\60\2\2 \n\3\2\2\2!\"\7*\2\2\"\f\3")
        buf.write("\2\2\2#$\7+\2\2$\16\3\2\2\2%\'\t\2\2\2&%\3\2\2\2\'(\3")
        buf.write("\2\2\2(&\3\2\2\2()\3\2\2\2)\20\3\2\2\2*,\t\3\2\2+*\3\2")
        buf.write("\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2./\3\2\2\2/\60\b\t\2")
        buf.write("\2\60\22\3\2\2\2\61\62\7g\2\2\62\63\7`\2\2\63\24\3\2\2")
        buf.write("\2\5\2(-\3\b\2\2")
        return buf.getvalue()


class FourierLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTEGRAL = 3
    DOT = 4
    LPAREN = 5
    RPAREN = 6
    ID = 7
    WS = 8
    EXP = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'sin'", "'cos'", "'\u222B'", "'.'", "'('", "')'", "'e^'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGRAL", "DOT", "LPAREN", "RPAREN", "ID", "WS", "EXP" ]

    ruleNames = [ "T__0", "T__1", "INTEGRAL", "DOT", "LPAREN", "RPAREN", 
                  "ID", "WS", "EXP" ]

    grammarFileName = "Fourier.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


