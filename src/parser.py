from sys import *
import ply.yacc as yacc
from models.for_model import ForModel
from models.function_model import FunctionModel
from lex import tokens
import os

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

file_name = str(argv[1][:-3]+".cpp")#'out.cpp'
output_file = open(file_name,'w')
output_code = []

def p_main(p):
	'statement : MAIN COLON'
	output_code.append("int main() {")

def p_fun_expression(p):
    'statement : FUN ID LPAREN declaration_list RPAREN COLON'
    print "we got a function!"

def p_function_no_param(p):
	'statement : FUN ID COLON'
	output_code.append("void " + p[2] + "(){")

def p_function_no_param_paren(p):
	'statement : FUN ID LPAREN RPAREN COLON'
	output_code.append("void " + p[2] + "(){")

def p_new_statement_function(p):
	'statement : VAR ID RECEIVE ID LPAREN RPAREN'
	print "I am here!"

def p_statement_function(p):
	'statement : ID RECEIVE ID LPAREN RPAREN'
	pass

def p_call_function(p):
	'expression : ID LPAREN RPAREN'
	output_code.append(p[1] + "();")

def p_declaration_list_1(p):
    'declaration_list : expression'
    pass

def p_declaration_list_2(p):
    'declaration_list : declaration_list expression '
    pass

def p_boolean_expression_list_1(p):
	'bool_list : expression'
	pass
def p_boolean_expression_list_2(p):
	'bool_list : bool_list expression'
	pass

def p_function_for(p):
	'expression : ID LPAREN RPAREN FOR expression'
	pass

def p_for_expression(p):
	'statement : FOR expression TO expression COLON'
	if p[2] < p[4]:
		output_code.append("for(int i = " + str(p[2]) + "; i < " + str(p[4]) + "; i++ ){")
	else:
		output_code.append("for(int i = " + str(p[2]) + "; i > " + str(p[4]) + "; i-- ){")

def p_for_in_expression(p):
	'statement : FOR ID IN expression TO expression COLON'
	if p[4] < p[6]:
		output_code.append("for(int " + str(p[2]) + " = " + str(p[4]) + "; " + str(p[2]) + " < " + str(p[6]+1) + "; " + str(p[2]) + "++ ){")
	else:
		output_code.append("for(int " + str(p[2]) + " = " + str(p[4]) + "; " + str(p[2]) + " > " + str(p[6]-1) + "; " + str(p[2]) + "-- ){")

def p_endmain(p):
	'statement : ENDMAIN'
	output_code.append("return 0;")
	output_code.append("}")

def p_endfor(p):
	'statement : ENDFOR'
	output_code.append("}")

def p_endfun(p):
	'statement : ENDFUN'
	output_code.append("}")

def p_return_string(p):
    'statement : RETURN STRING'
    pass

def p_return_expression(p):
    'statement : RETURN expression'
    pass

def p_print_expression(p):
	'statement : PRINT expression'
	output_code.append("cout << " + str(p[2]) + " << endl;")

def p_print_string(p):
	'statement : PRINT STRING'
	output_code.append("cout << " + str(p[2]) + " << endl;")

def p_if(p):
	'statement : IF expression COLON'
	output_code.append("if ( " + p[2] + " ) {")

def p_endif(p):
	'statement : ENDIF'
	output_code.append("}")

def p_statement_assign_int(p):
	'statement : ID COLON INT RECEIVE expression'
	output_code.append("int " + p[1] + " = " + str(p[5]) + ";")

def p_statement_assign_string(p):
    'statement : ID COLON STRING_TYPE RECEIVE STRING'
    output_code.append("string " + p[1] + " = " + p[5] + ";")

def p_change_statement_assign(p):
	'statement : ID RECEIVE expression'
	output_code.append(str(p[1]) + " = " + str(p[3]) + ";")

def p_change_string(p):
	'statement : ID RECEIVE STRING'
	pass

def p_statement_expr(p):
    'statement : expression'
    pass

def p_statement_paren(p):
    'statement : LPAREN expression RPAREN'
    pass

def p_boolean_expression(p):
	'''expression : expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression'''

	p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3])

def p_expression_binop(p):
	'''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''

	p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3])

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_number(p):
    '''expression : FLOAT
                  | INTEGER'''
    p[0] = p[1]

def p_expression_comma(p):
    'expression : expression COMMA'

def p_expression_id(p):
    "expression : ID"
    p[0] = p[1]

def p_pause(p):
	"statement : PAUSE LPAREN RPAREN"
	output_code.append('cin.get();')

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        pass#print("Syntax error at EOF")

def p_null(p):
    'statement :'

parser = yacc.yacc()

def open_file(file_name):
    if file_name[-3:] == ".lc":
        code_lines = open(file_name, "r").readlines()
        return code_lines
    else:
        print "the file extension is incorrect, it should be .lc"
        return None

if __name__ == '__main__':

	code_lines = open_file(argv[1])

	output_code.append("#include <iostream>")
	output_code.append("using namespace std;")

	for line in code_lines:
		parser.parse(line)

	for line in output_code:
		output_file.write(line + "\n")

#
#
#
#
#
