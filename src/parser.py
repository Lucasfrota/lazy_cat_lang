from sys import *
import ply.yacc as yacc
from models.for_model import ForModel
from models.function_model import FunctionModel
from lex import tokens

parser = None
for_list = []
quantity_for = 0

if_list = []
quantity_if = 0

global current_function
current_function = None

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

variables = {}
functions = []

jumped = False

program_counter = 0
code_lines = []

def go_next_line():
    global jumped
    global program_counter
    if jumped == False:
        program_counter += 1
        jumped = True

def set_next_line(line):
        global program_counter
        program_counter = line

def call_function(name, called_in_line):

    there_is_function = False

    for function in functions:
        if name == function.function_name:
            current_line = program_counter
            set_next_line(function.function_line)

            code_lines[called_in_line-1] == "//"

            i = function.current_line - 1
            while function.function_line - 1 < i:
                code_lines.insert(called_in_line, code_lines[i])
                i -= 1

            set_next_line(called_in_line)
            there_is_function = True
            '''
            for i in range(function.function_line, function.current_line):
                #set_next_line(called_in_line, code_lines[i])
                code_lines.insert(called_in_line, code_lines[i])
                #print "PC: " + str(program_counter)
                #parser.parse(code_lines[i])
            '''


    if not there_is_function:
        print "there is no function called '" + name + "'"

#########################

def p_fun_expression(p):
    'statement : FUN ID LPAREN declaration_list RPAREN COLON'
    print "we got a function!"

def p_function_no_param(p):
    'statement : FUN ID COLON'

    go_next_line()

    global current_function
    current_function = p[2]

    current_line = program_counter
    first_line = program_counter

    line = code_lines[current_line]

    while line != "endfun\n":
        current_line += 1
        line = code_lines[current_line]

    set_next_line(current_line)

    functions.append( FunctionModel(p[2], first_line, current_line, None) )#[p[2], [first_line], [current_line], [None] ])

def p_function_no_param_paren(p):
    'statement : FUN ID LPAREN RPAREN COLON'

    go_next_line()

    global current_function
    current_function = p[2]

    current_line = program_counter
    first_line = program_counter

    line = code_lines[current_line]

    while line != "endfun\n":
        current_line += 1
        line = code_lines[current_line]

    set_next_line(current_line)


    functions.append( FunctionModel(p[2], first_line, current_line, None) ) #[p[2], [first_line], [current_line], None ])

def p_new_statement_function(p):
    'statement : VAR ID RECEIVE ID LPAREN RPAREN'
    go_next_line()

    call_function(p[4], program_counter)

    variables[p[2]] = None

    for function in functions:
        if current_function == function.function_name:
            variables[p[2]] = function.function_return

def p_statement_function(p):
    'statement : ID RECEIVE ID LPAREN RPAREN'

    go_next_line()

    call_function(p[3], program_counter)

    try:
        value = variables[p[1]]

        for function in functions:
            if current_function == function.function_name:
                variables[p[1]] = function.function_return

    except LookupError:
        print("Undefined variable '%s'" % p[1])
        p[0] = 0

def p_call_function(p):
    'expression : ID LPAREN RPAREN'

    go_next_line()

    call_function(p[1], program_counter)

def p_declaration_list_1(t):
    'declaration_list : expression'
    pass

def p_declaration_list_2(t):
    'declaration_list : declaration_list expression '
    pass

def p_function_for(p):
    'expression : ID LPAREN RPAREN FOR expression'

    go_next_line()

    number_of_iteration = p[5]
    function_name = p[1]

    for i in range(0, number_of_iteration):
        call_function(function_name, program_counter)

def p_for_expression(p):
    'statement : FOR expression TO expression COLON'

    is_increasing = None

    comand_list = []

    if p[2] < p[4]:
        is_increasing = True
    else:
        is_increasing = False

    current_line = program_counter + 1
    while code_lines[current_line] != 'endfor\n':
        comand_list.append(code_lines[current_line])
        current_line += 1

    comand_list.reverse()

    if is_increasing == True:
        aux_counter = p[2]
        while aux_counter < p[4]:
            for comand in comand_list:
                code_lines.insert(current_line, comand)
            aux_counter += 1

    else:
        aux_counter = p[2]
        while aux_counter > p[4]:
            for comand in comand_list:
                code_lines.insert(current_line, comand)
            aux_counter -= 1

    go_next_line()

def p_for_in_expression(p):
    'statement : FOR ID IN expression TO expression COLON'

    comand_list = []

    variables[p[2]] = None

    is_increasing = None

    if p[4] < p[6]:
        is_increasing = True
    else:
        is_increasing = False

    current_line = program_counter + 1
    while code_lines[current_line] != 'endfor\n':
        comand_list.append(code_lines[current_line])
        current_line += 1

    comand_list.reverse()

    if is_increasing == True:
        aux_counter = p[4]
        while aux_counter < p[6]:
            print "I: " + str(aux_counter)
            variables[p[2]] = aux_counter
            for comand in comand_list:
                code_lines.insert(current_line, comand)
            aux_counter += 1

    else:
        aux_counter = p[4]
        while aux_counter > p[6]:
            variables[p[2]] = aux_counter
            for comand in comand_list:
                code_lines.insert(current_line, comand)
            aux_counter -= 1

    go_next_line()

def p_endfor(p):
    'statement : ENDFOR'
    go_next_line()

def p_endfun(p):
    'statement : ENDFUN'
    go_next_line()

    '''
    global current_function

    for function in functions:
        if function.function_name == current_function:
            print "cojapoc: " + str(function.current_line)
            set_next_line(function.current_line)

    current_function = None
    '''
    pass

def p_return_string(p):
    'statement : RETURN STRING'

    go_next_line()

    for function in functions:
        if current_function == function.function_name:
            function.function_return = p[2][1:-1]

    pass

def p_return_expression(p):
    'statement : RETURN expression'

    go_next_line()

    for function in functions:
        if current_function == function.function_name:
            function.function_return = p[2]

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

    if p[2] == True:
        go_next_line()
    else:
        current_line = program_counter

        line = code_lines[current_line]

        while line != "endif\n":
            current_line += 1
            line = code_lines[current_line]

        set_next_line(current_line)

def p_endif(p):
    'statement : ENDIF'
    go_next_line()
    pass

def p_statement_assign(p):
    'statement : VAR ID RECEIVE expression'
    go_next_line()
    variables[p[2]] = p[4]

def p_string(p):
    'statement : VAR ID RECEIVE STRING'
    go_next_line()
    variables[p[2]] = p[4][1:-1]

def p_change_statement_assign(p):
    'statement : ID RECEIVE expression'
    go_next_line()
    if p[1] in variables:
        variables[p[1]] = p[3]
    else:
        print "This variable has to be created before being assigned"

def p_change_string(p):
    'statement : ID RECEIVE STRING'
    go_next_line()
    if  p[1] in variables:
        variables[p[1]] = p[3][1:-1]
    else:
        print "This variable has to be created before being assigned"

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

    is_running = True

    code_lines = open_file(argv[1])
    code_lines.append("program_end")
    if code_lines is not None:
        while is_running:
            if code_lines[program_counter] != 'program_end':
                #print code_lines[program_counter]
                parser.parse(code_lines[program_counter])
                jumped = False
            else:
                is_running = False
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
