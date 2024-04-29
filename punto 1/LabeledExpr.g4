grammar LabeledExpr; 

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   expr (op=('+'|'-')) expr      # AddSub
    |   expr (op=('*'|'/')) expr      # MulDiv
    |   INT                         # int
    |   ID                          # id
    |   '(' expr ')'                # parens
    |   'i'                         # imagLit
    |   INT 'i'                     # imagLitWithInt
    |   INT ('+'|'-') INT 'i'       # complexLit
    ;

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
