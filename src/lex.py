import ply.lex as lex

tokens = [
   'ID',
   'INTEGER',
   'FLOAT',
   'STRING',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'SQUARED',
   'QUOTATION',
   'RECEIVE',
   'NEWLINE',
   'COLON',
   'COMMA',
]

boolean_operators = [
    'LT',
    'LE',
    'GT',
    'GE',
]

reserved = {
   'print' : 'PRINT',
   'if' : 'IF',
   'for' : 'FOR',
   'to' : 'TO',
   'else' : 'ELSE',
   'true' : 'TRUE',
   'false' : 'FALSE',
   'none' : 'NONE',
   'or' : 'OR',
   'and' : 'AND',
   'not' : 'NOT',
   'return' : 'RETURN',
   'var' : 'VAR',
   'in' : 'IN',
   'endfor' : 'ENDFOR',
   'endfun' : 'ENDFUN',
   'endif' : 'ENDIF',
   'fun' : 'FUN',
}

literals = [ '{', '}']

tokens = tokens + boolean_operators + list(reserved.values())

t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_QUOTATION = r'\"'
t_RECEIVE   = r'\='
t_STRING    = r'\".*?\"'
t_COLON     = r':'
t_COMMA = r'\,'

t_LT        = r'<'
t_LE        = r'<='
t_GT        = r'>'
t_GE        = r'>='

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
    t.value = float(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_COMMENT(t):
    r'\//.*'
    pass

def t_SQUARED(t):
    r'\*\*'
    return t

def find_column(input,token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
	       last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

lexer = lex.lex()

data = '''
while 3 = ** 4.4 "" {
    1
}
'''

lexer.input(data)

if __name__ == '__main__':
    for tok in lexer:
        print(tok)
