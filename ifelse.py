from ply import lex, yacc

tokens = (
    'IF', 'ELSE', 'IDENTIFIER', 'SEMICOLON', 'LBRACE', 'RBRACE',
    'LPAREN', 'RPAREN', 'CONDITION',
)

t_IF = r'if'
t_ELSE = r'else'
t_SEMICOLON = r';'

loop_syntax_errors=[]
def t_LPAREN(t):
    r'\('
    return t
def t_RPAREN(t):
    r'\)'
    return t
def t_LBRACE(t):
    r'\{'
    return t
def t_RBRACE(t):
    r'\}'
    return t


def t_IDENTIFIER(t):
    r'(?!if\b|else\b)[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_CONDITION(t):
    r'(?!if\b|else\b)[a-zA-Z_][a-zA-Z0-9_]*|[0-9]+|[<>=!+]'
    return t
def t_WHITESPACE(t):
    r'[ \t]+'
    pass

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def p_statements(p):
    '''statements : statement
                  | statements statement'''

def p_statement(p):
    '''statement : if_statement
                 | else_if_statement
                 | else_statement
                 | other_statement
                 | empty_statement'''

def p_if_statement(p):
    '''if_statement : IF LPAREN expressions RPAREN LBRACE expressions RBRACE'''

def p_else_if_statement(p):
    '''else_if_statement : ELSE IF LPAREN expressions RPAREN LBRACE expressions RBRACE'''

def p_else_statement(p):
    '''else_statement : ELSE LBRACE expressions RBRACE'''

def p_other_statement(p):
    '''other_statement : IDENTIFIER SEMICOLON'''

def p_empty_statement(p):
    '''empty_statement : SEMICOLON'''

def p_expressions(p):
    '''expressions : expression
                   | expressions expression'''

def p_expression(p):
    '''expression : IDENTIFIER
                  | CONDITION
                  | SEMICOLON'''
    
def p_error(p):
    print("error is :",p)
    if p:
        loop_syntax_errors.append(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
    else:
        loop_syntax_errors.append("Syntax error: Unexpected end of input")

lexer = lex.lex()
parser = yacc.yacc()

print("Enter function declaration code. Type 'end' on a new line to finish:")
print("Use 'end' as the last line to indicate the end of input.")

input_lines = []
while True:
    line = input()
    if line.strip().lower() == 'end':
        break
    input_lines.append(line)

sample_input = '\n'.join(input_lines)

lexer.input(sample_input)

for token in lexer:
    
    pass

parser.parse(sample_input)
if not loop_syntax_errors:
    print("Loop syntax is valid.")
else:
    print("Loop syntax errors:")
    for error in loop_syntax_errors:
        print(error)