
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftPLUSMINUSleftTIMESDIVIDErightUMINUSID INTEGER FLOAT STRING PLUS MINUS TIMES DIVIDE LPAREN RPAREN SQUARED QUOTATION RECEIVE NEWLINE COLON COMMA LT LE GT GE AND FUN NONE FALSE FOR ENDIF NOT VAR ENDFUN ELSE TO ENDFOR IN PRINT RETURN TRUE OR IFstatement : FUN ID LPAREN declaration_list RPAREN COLONstatement : FUN ID COLONstatement : FUN ID LPAREN RPAREN COLONstatement : VAR ID RECEIVE ID LPAREN RPARENstatement : ID RECEIVE ID LPAREN RPARENexpression : ID LPAREN RPARENdeclaration_list : expressiondeclaration_list : declaration_list expression expression : ID LPAREN RPAREN FOR expressionstatement : FOR expression TO expression COLONstatement : FOR ID IN expression TO expression COLONstatement : ENDFORstatement : ENDFUNstatement : RETURN STRINGstatement : RETURN expressionstatement : PRINT expressionstatement : PRINT STRINGstatement : IF expression COLONstatement : ENDIFstatement : VAR ID RECEIVE expressionstatement : VAR ID RECEIVE STRINGstatement : ID RECEIVE expressionstatement : ID RECEIVE STRINGstatement : expressionstatement : LPAREN expression RPARENexpression : expression LT expression\n                  | expression LE expression\n                  | expression GT expression\n                  | expression GE expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : '-' expression %prec UMINUSexpression : '(' expression ')'expression : FLOAT\n                  | INTEGERexpression : expression COMMAexpression : IDstatement :"
    
_lr_action_items = {'RETURN':([0,],[1,]),'IN':([26,],[45,]),'ENDFUN':([0,],[2,]),'PRINT':([0,],[4,]),'COLON':([15,16,20,21,25,32,40,44,52,54,55,56,57,58,59,60,61,62,66,73,79,81,],[-37,-36,-39,42,-34,53,-38,-35,-6,-27,-33,-29,-32,-26,-28,-30,-31,72,76,80,-9,83,]),'FUN':([0,],[3,]),'MINUS':([13,15,16,17,19,20,23,24,25,26,27,28,32,40,44,50,51,52,54,55,56,57,58,59,60,61,64,65,66,68,69,74,78,79,81,82,],[-39,-37,-36,41,41,-39,41,41,-34,-39,41,41,41,-38,-35,41,-39,-6,41,-33,41,-32,41,41,-30,-31,41,41,41,-39,41,41,-6,41,41,-6,]),'STRING':([1,4,30,48,],[18,22,49,67,]),'LE':([13,15,16,17,19,20,23,24,25,26,27,28,32,40,44,50,51,52,54,55,56,57,58,59,60,61,64,65,66,68,69,74,78,79,81,82,],[-39,-37,-36,33,33,-39,33,33,-34,-39,33,33,33,-38,-35,33,-39,-6,33,-33,33,-32,33,33,-30,-31,33,33,33,-39,33,33,-6,33,33,-6,]),'RPAREN':([15,16,20,25,28,31,40,43,44,52,54,55,56,57,58,59,60,61,63,64,70,74,77,79,],[-37,-36,-39,-34,47,52,-38,62,-35,-6,-27,-33,-29,-32,-26,-28,-30,-31,73,-7,78,-8,82,-9,]),')':([15,16,20,24,25,40,44,52,54,55,56,57,58,59,60,61,79,],[-37,-36,-39,44,-34,-38,-35,-6,-27,-33,-29,-32,-26,-28,-30,-31,-9,]),'(':([0,1,4,5,6,9,10,14,15,16,20,25,30,33,34,35,36,37,38,39,40,41,43,44,45,46,48,52,54,55,56,57,58,59,60,61,63,64,71,74,75,79,],[5,5,5,5,5,5,5,5,-37,-36,-39,-34,5,5,5,5,5,5,5,5,-38,5,5,-35,5,5,5,-6,-27,-33,-29,-32,-26,-28,-30,-31,5,-7,5,-8,5,-9,]),'-':([0,1,4,5,6,9,10,14,15,16,20,25,30,33,34,35,36,37,38,39,40,41,43,44,45,46,48,52,54,55,56,57,58,59,60,61,63,64,71,74,75,79,],[6,6,6,6,6,6,6,6,-37,-36,-39,-34,6,6,6,6,6,6,6,6,-38,6,6,-35,6,6,6,-6,-27,-33,-29,-32,-26,-28,-30,-31,6,-7,6,-8,6,-9,]),'TO':([15,16,20,25,26,27,40,44,52,54,55,56,57,58,59,60,61,65,79,],[-37,-36,-39,-34,-39,46,-38,-35,-6,-27,-33,-29,-32,-26,-28,-30,-31,75,-9,]),'LT':([13,15,16,17,19,20,23,24,25,26,27,28,32,40,44,50,51,52,54,55,56,57,58,59,60,61,64,65,66,68,69,74,78,79,81,82,],[-39,-37,-36,37,37,-39,37,37,-34,-39,37,37,37,-38,-35,37,-39,-6,37,-33,37,-32,37,37,-30,-31,37,37,37,-39,37,37,-6,37,37,-6,]),'PLUS':([13,15,16,17,19,20,23,24,25,26,27,28,32,40,44,50,51,52,54,55,56,57,58,59,60,61,64,65,66,68,69,74,78,79,81,82,],[-39,-37,-36,39,39,-39,39,39,-34,-39,39,39,39,-38,-35,39,-39,-6,39,-33,39,-32,39,39,-30,-31,39,39,39,-39,39,39,-6,39,39,-6,]),'ENDFOR':([0,],[7,]),'INTEGER':([0,1,4,5,6,9,10,14,15,16,20,25,30,33,34,35,36,37,38,39,40,41,43,44,45,46,48,52,54,55,56,57,58,59,60,61,63,64,71,74,75,79,],[15,15,15,15,15,15,15,15,-37,-36,-39,-34,15,15,15,15,15,15,15,15,-38,15,15,-35,15,15,15,-6,-27,-33,-29,-32,-26,-28,-30,-31,15,-7,15,-8,15,-9,]),'$end':([0,2,7,8,11,13,15,16,17,18,19,20,22,23,25,40,42,44,47,49,50,51,52,53,54,55,56,57,58,59,60,61,67,68,69,72,76,78,79,80,82,83,],[-40,-13,-12,0,-19,-39,-37,-36,-24,-14,-15,-39,-17,-16,-34,-38,-2,-35,-25,-23,-22,-39,-6,-18,-27,-33,-29,-32,-26,-28,-30,-31,-21,-39,-20,-3,-10,-5,-9,-1,-4,-11,]),'GT':([13,15,16,17,19,20,23,24,25,26,27,28,32,40,44,50,51,52,54,55,56,57,58,59,60,61,64,65,66,68,69,74,78,79,81,82,],[-39,-37,-36,38,38,-39,38,38,-34,-39,38,38,38,-38,-35,38,-39,-6,38,-33,38,-32,38,38,-30,-31,38,38,38,-39,38,38,-6,38,38,-6,]),'DIVIDE':([13,15,16,17,19,20,23,24,25,26,27,28,32,40,44,50,51,52,54,55,56,57,58,59,60,61,64,65,66,68,69,74,78,79,81,82,],[-39,-37,-36,34,34,-39,34,34,-34,-39,34,34,34,-38,-35,34,-39,-6,34,-33,34,-32,34,34,34,34,34,34,34,-39,34,34,-6,34,34,-6,]),'FOR':([0,52,78,82,],[9,71,71,71,]),'RECEIVE':([13,29,],[30,48,]),'TIMES':([13,15,16,17,19,20,23,24,25,26,27,28,32,40,44,50,51,52,54,55,56,57,58,59,60,61,64,65,66,68,69,74,78,79,81,82,],[-39,-37,-36,36,36,-39,36,36,-34,-39,36,36,36,-38,-35,36,-39,-6,36,-33,36,-32,36,36,36,36,36,36,36,-39,36,36,-6,36,36,-6,]),'GE':([13,15,16,17,19,20,23,24,25,26,27,28,32,40,44,50,51,52,54,55,56,57,58,59,60,61,64,65,66,68,69,74,78,79,81,82,],[-39,-37,-36,35,35,-39,35,35,-34,-39,35,35,35,-38,-35,35,-39,-6,35,-33,35,-32,35,35,-30,-31,35,35,35,-39,35,35,-6,35,35,-6,]),'LPAREN':([0,13,20,21,26,51,68,],[10,31,31,43,31,70,77,]),'ENDIF':([0,],[11,]),'VAR':([0,],[12,]),'ID':([0,1,3,4,5,6,9,10,12,14,15,16,20,25,30,33,34,35,36,37,38,39,40,41,43,44,45,46,48,52,54,55,56,57,58,59,60,61,63,64,71,74,75,79,],[13,20,21,20,20,20,26,20,29,20,-37,-36,-39,-34,51,20,20,20,20,20,20,20,-38,20,20,-35,20,20,68,-6,-27,-33,-29,-32,-26,-28,-30,-31,20,-7,20,-8,20,-9,]),'IF':([0,],[14,]),'FLOAT':([0,1,4,5,6,9,10,14,15,16,20,25,30,33,34,35,36,37,38,39,40,41,43,44,45,46,48,52,54,55,56,57,58,59,60,61,63,64,71,74,75,79,],[16,16,16,16,16,16,16,16,-37,-36,-39,-34,16,16,16,16,16,16,16,16,-38,16,16,-35,16,16,16,-6,-27,-33,-29,-32,-26,-28,-30,-31,16,-7,16,-8,16,-9,]),'COMMA':([13,15,16,17,19,20,23,24,25,26,27,28,32,40,44,50,51,52,54,55,56,57,58,59,60,61,64,65,66,68,69,74,78,79,81,82,],[-39,-37,-36,40,40,-39,40,40,-34,-39,40,40,40,-38,-35,40,-39,-6,40,-33,40,-32,40,40,-30,-31,40,40,40,-39,40,40,-6,40,40,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,4,5,6,9,10,14,30,33,34,35,36,37,38,39,41,43,45,46,48,63,71,75,],[17,19,23,24,25,27,28,32,50,54,55,56,57,58,59,60,61,64,65,66,69,74,79,81,]),'statement':([0,],[8,]),'declaration_list':([43,],[63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> FUN ID LPAREN declaration_list RPAREN COLON','statement',6,'p_fun_expression','parser.py',63),
  ('statement -> FUN ID COLON','statement',3,'p_function_no_param','parser.py',67),
  ('statement -> FUN ID LPAREN RPAREN COLON','statement',5,'p_function_no_param_paren','parser.py',89),
  ('statement -> VAR ID RECEIVE ID LPAREN RPAREN','statement',6,'p_new_statement_function','parser.py',111),
  ('statement -> ID RECEIVE ID LPAREN RPAREN','statement',5,'p_statement_function','parser.py',123),
  ('expression -> ID LPAREN RPAREN','expression',3,'p_call_function','parser.py',141),
  ('declaration_list -> expression','declaration_list',1,'p_declaration_list_1','parser.py',148),
  ('declaration_list -> declaration_list expression','declaration_list',2,'p_declaration_list_2','parser.py',152),
  ('expression -> ID LPAREN RPAREN FOR expression','expression',5,'p_function_for','parser.py',156),
  ('statement -> FOR expression TO expression COLON','statement',5,'p_for_expression','parser.py',159),
  ('statement -> FOR ID IN expression TO expression COLON','statement',7,'p_for_in_expression','parser.py',173),
  ('statement -> ENDFOR','statement',1,'p_endfor','parser.py',192),
  ('statement -> ENDFUN','statement',1,'p_endfun','parser.py',221),
  ('statement -> RETURN STRING','statement',2,'p_return_string','parser.py',226),
  ('statement -> RETURN expression','statement',2,'p_return_expression','parser.py',237),
  ('statement -> PRINT expression','statement',2,'p_print_expression','parser.py',248),
  ('statement -> PRINT STRING','statement',2,'p_print_string','parser.py',253),
  ('statement -> IF expression COLON','statement',3,'p_if','parser.py',258),
  ('statement -> ENDIF','statement',1,'p_endif','parser.py',274),
  ('statement -> VAR ID RECEIVE expression','statement',4,'p_statement_assign','parser.py',279),
  ('statement -> VAR ID RECEIVE STRING','statement',4,'p_string','parser.py',284),
  ('statement -> ID RECEIVE expression','statement',3,'p_change_statement_assign','parser.py',289),
  ('statement -> ID RECEIVE STRING','statement',3,'p_change_string','parser.py',297),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',305),
  ('statement -> LPAREN expression RPAREN','statement',3,'p_statement_paren','parser.py',309),
  ('expression -> expression LT expression','expression',3,'p_boolean_expression','parser.py',313),
  ('expression -> expression LE expression','expression',3,'p_boolean_expression','parser.py',314),
  ('expression -> expression GT expression','expression',3,'p_boolean_expression','parser.py',315),
  ('expression -> expression GE expression','expression',3,'p_boolean_expression','parser.py',316),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',328),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',329),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',330),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',331),
  ('expression -> - expression','expression',2,'p_expression_uminus','parser.py',343),
  ('expression -> ( expression )','expression',3,'p_expression_group','parser.py',347),
  ('expression -> FLOAT','expression',1,'p_expression_number','parser.py',351),
  ('expression -> INTEGER','expression',1,'p_expression_number','parser.py',352),
  ('expression -> expression COMMA','expression',2,'p_expression_comma','parser.py',356),
  ('expression -> ID','expression',1,'p_expression_id','parser.py',359),
  ('statement -> <empty>','statement',0,'p_null','parser.py',373),
]
