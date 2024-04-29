grammar filterFunc;

// Regla de inicio
start : FILTER '(' function ',' iterable ')' ;

// Función condicional
function : ID ;

// Objeto iterable
iterable : list | tuple ;
list : '[' elements? ']' ;
tuple : '(' elements? ')' ;
elements : element (',' element)* ;
element : INT | FLOAT | STRING ;

// Tokens
FILTER : 'FILTER' ;
INT : [0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]* ;
STRING : '"' ~('"')* '"' ;
ID : [a-zA-Z_] [a-zA-Z_0-9]* ;
WS : [ \t\r\n]+ -> skip ;

