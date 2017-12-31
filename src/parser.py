from sys import *
import ply.yacc as yacc
from lex import tokens

parser = None

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

variables = {}
current_line = 0
code_lines = []

def p_for_expression(p):
    'statement : FOR expression TO expression COLON'

    commands_in_loop = []

    line_counter = current_line + 1
    is_in_loop = True
    while code_lines[line_counter] != 'end\n':
        commands_in_loop.append(code_lines[line_counter])
        line_counter += 1

    if p[4] > p[2]:
        for i in range(p[2], p[4]):
            for j in commands_in_loop:
                parser.parse(j)
    else:
        sec_num = p[4]
        while sec_num < p[2]:
            for j in commands_in_loop:
                parser.parse(j)
            sec_num += 1

def p_for_in_expression(p):
        'statement : FOR ID IN expression TO expression COLON'

        variables[p[2]] = None

        commands_in_loop = []

        line_counter = current_line + 1
        is_in_loop = True
        while code_lines[line_counter] != 'end\n':
            commands_in_loop.append(code_lines[line_counter])
            line_counter += 1

        if p[6] > p[4]:
            for i in range(p[4], p[6]):
                variables[p[2]] = i
                for j in commands_in_loop:
                    parser.parse(j)
            variables[p[2]] = variables[p[2]] + 1
        else:
            sec_num = p[4]
            while sec_num > p[6]:
                variables[p[2]] = sec_num
                for j in commands_in_loop:
                    parser.parse(j)
                sec_num -= 1
            variables[p[2]] = variables[p[2]] - 1

def p_end(p):
    'statement : END'
    pass

def p_print_expression(p):
    'statement : PRINT expression'
    print p[2]

def p_print_string(p):
    'statement : PRINT STRING'
    print p[2][1:-1]

def p_if(p):
    'statement : IF expression '
    print p[2]

def p_statement_assign(p):
    'statement : ID RECEIVE expression'
    variables[p[1]] = p[3]

def p_string(p):
    'statement : ID RECEIVE STRING'
    variables[p[1]] = p[3][1:-1]

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_statement_paren(p):
    'statement : LPAREN expression RPAREN'
    p[0] = p[2]

def p_boolean_expression(p):
    '''expression : expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression'''
    if p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

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

def p_expression_id(p):
    "expression : ID"
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print("Undefined variable '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        pass#print("Syntax error at EOF")

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
    if code_lines is not None:
        for line in code_lines:
            parser.parse(line)
            current_line += 1
'''
    try:

    except:

        while True:
           try:
               s = raw_input('lazy_cat> ')
           except EOFError:
               break
           if not s:
               continue
           parser.parse(s)
'''
