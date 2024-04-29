grammar Fourier;

start: expr EOF;

expr: INTEGRAL LPAREN function DOT exponent RPAREN;

INTEGRAL: '∫';
DOT: '.';
LPAREN: '(';
RPAREN: ')';
ID: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;

function: ID | sinFunction | cosFunction; // Define otras funciones si es necesario

sinFunction: 'sin' LPAREN expr RPAREN;
cosFunction: 'cos' LPAREN expr RPAREN;

exponent: EXP LPAREN ID RPAREN;

EXP: 'e^';
