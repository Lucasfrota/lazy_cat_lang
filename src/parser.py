from sys import *
import ply.yacc as yacc
from lex import tokens

parser = None
for_list = []
quantity_for = 0

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

variables = {}
procedures = []
for_base_line = -1

for_first_number = -1
for_sec_number = -1

jumped = False

program_counter = -1
code_lines = []

def set_for_base_line(line):
    global for_base_line
    for_base_line = line

def set_for_numbers(first_num, sec_num):
    global for_first_number
    global for_sec_number
    for_first_number = first_num
    for_sec_number = sec_num

def go_next_line():
    global jumped
    global program_counter
    if jumped == False:
        program_counter += 1
        jumped = True

def set_next_line(line):
        global program_counter
        program_counter = line

def p_fun_expression(p):
    'statement : FUN ID LPAREN declaration_list RPAREN COLON'
    print "we got a function!"

def p_procedure_expression(p):
    'statement : FUN ID COLON'

    go_next_line()
    '''
    commands_in_procedure = []

    line_counter = current_line + 1
    while code_lines[line_counter] != 'endfun\n':
        commands_in_procedure.append(code_lines[line_counter])
        null_lines_list.append(line_counter)
        line_counter += 1

    procedures.append([p[2], commands_in_procedure])
    '''

def p_procedure_expression_paren(p):
    'statement : FUN ID LPAREN RPAREN COLON'

    go_next_line()
    '''
    commands_in_procedure = []

    line_counter = current_line + 1
    while code_lines[line_counter] != 'endfun\n':
        commands_in_procedure.append(code_lines[line_counter])
        null_lines_list.append(line_counter)
        line_counter += 1

    procedures.append([p[2], commands_in_procedure])
    '''

def p_call_procedure(p):
    'expression : ID LPAREN RPAREN'

    go_next_line()
    '''
    there_is_procedure = False

    for i in procedures:
        if p[1] == i[0]:
            there_is_procedure = True

            #null_lines_list.append(code_lines.index(code_lines[current_line]))
            #print "code: " + code_lines[current_line] + ", " + str(current_line)
            code_lines.
            sub_line_counter = code_lines.index(code_lines[current_line]) + 1
            #print p[1] + ": " + str(i[1])
            for j in i[1]:
                #print "j: " + j
                code_lines.insert(sub_line_counter, j)
                sub_line_counter += 1

    if not there_is_procedure:
        print "there is no procedure called '" + p[1] + "'"
    '''

def p_declaration_list_1(t):
    'declaration_list : expression'
    pass

def p_declaration_list_2(t):
    'declaration_list : declaration_list expression '
    pass

def p_for_expression(p):
    'statement : FOR expression TO expression COLON'

    set_for_base_line(program_counter + 1)

    is_increasing = None

    if p[2] < p[4]:
        is_increasing = True
    else:
        is_increasing = False

    for_list.append([["for" + str(quantity_for)], [ p[2], p[4] ], [is_increasing] ])#in this case 'true' is to show that the for is increasing

    set_for_numbers(p[2], p[4])

    go_next_line()

def p_for_in_expression(p):
    'statement : FOR ID IN expression TO expression COLON'

    go_next_line()
    '''
    variables[p[2]] = None

    commands_in_loop = []

    line_counter = current_line + 1
    while code_lines[line_counter][-4:] != 'end\n':
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
    '''

def p_endfor(p):
    'statement : ENDFOR'
    go_next_line()

    global quantity_for

    if for_list[quantity_for][2][0] == True:
        if for_list[quantity_for][1][0] < for_list[quantity_for][1][1]:
            for_list[quantity_for][1][0] += 1
            set_next_line(for_base_line)
        else:
            quantity_for += 1
    else:
        if for_list[quantity_for][1][0] > for_list[quantity_for][1][1]:
            for_list[quantity_for][1][1] += 1
            set_next_line(for_base_line)
        else:
            quantity_for += 1

def p_endfun(p):
    'statement : ENDFUN'
    go_next_line()
    pass

def p_print_expression(p):
    'statement : PRINT expression'
    go_next_line()
    print p[2]

def p_print_string(p):
    'statement : PRINT STRING'
    go_next_line()
    print p[2][1:-1]

def p_if(p):
    'statement : IF expression COLON'
    go_next_line()

    '''
    commands_in_loop = []

    if p[2] == False:
        line_counter = current_line + 1
        while code_lines[line_counter] != 'end\n':
            null_lines_list.append(line_counter)
            line_counter += 1
    '''

def p_statement_assign(p):
    'statement : ID RECEIVE expression'
    go_next_line()
    variables[p[1]] = p[3]

def p_string(p):
    'statement : ID RECEIVE STRING'
    go_next_line()
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
    go_next_line()
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
    go_next_line()
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

def p_expression_comma(p):
    'expression : expression COMMA'

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

def p_null(p):
    'statement :'
    go_next_line()

parser = yacc.yacc()

def open_file(file_name):
    if file_name[-3:] == ".lc":
        code_lines = open(file_name, "r").readlines()
        return code_lines
    else:
        print "the file extension is incorrect, it should be .lc"
        return None

if __name__ == '__main__':

    program_counter = 0

    code_lines = open_file(argv[1])
    code_lines.append("program_end")
    if code_lines is not None:
        while code_lines[program_counter] != 'program_end':
            #print code_lines[program_counter]
            parser.parse(code_lines[program_counter])
            jumped = False
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
