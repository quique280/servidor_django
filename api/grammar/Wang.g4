/*
@author loriacarlos@gmail.com
@since II-2018
*/
grammar Wang;

deduction: formula ('.' formula)*EOF
;

formula:  (sequence ('=>'  sequence)?) #FormExpr
 | sequence '=>'#FormExpr
 | '=>' sequence #FormExpr
   
;
sequence: listexpr?           
;
listexpr: expr (',' expr)*   # SeqExpr
;

expr:   '~' expr              # NotExpr
    |   expr op='&' expr      # AndExpr
    |   expr op='|' expr      # OrExpr
    | <assoc=right>  
      expr op='->' expr       # ImplyExpr
    |   expr op='<=>' expr    # BicondExpr
    |   ID                    # Id
    |   '(' expr ')'          # Parens

;
COMMA : ','
;
DOT : '.'
;
LEADSTO : '=>'
;
NOT : '~'
;
AND : '&' 
; 
OR :  '|' 
;
IMPLIES: '->'
;
BICONDITIONAL: '<=>'
;
ID  :   [a-z][a-z0-9_]* 
;      
WS  :   [\r\n\t ]+ -> skip
;
ErrorChar : .
;
