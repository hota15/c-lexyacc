from ply import lex, yacc

# Define the tokens
tokens = ('FOR','IDENTIFIER', 'SEMICOLON', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'CONDITION', 'COMMENT', 'INDENT', 'DEDENT')

# Define regular expressions for tokens
t_FOR = r'for'
t_SEMICOLON = r';'
t_LBRACE = r'\{'
t_RBRACE = r'\}'


def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_COMMENT(t):
    r'//.*'
    pass

# Define regular expressions for IDENTIFIER and CONDITION
def t_IDENTIFIER(t):
    r'(?!for\b|i\b|x\b|y\b)[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_CONDITION(t):
    r'(?!for\b)[a-zA-Z_][a-zA-Z0-9_]*|[0-9]+|[<>=!+]'
    return t

# Tracks the indentation level
indent_level = 0
indent_stack = [0]

# Define a list to keep track of loop syntax errors
loop_syntax_errors = []

# Define the lexer
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_WHITESPACE(t):
    r'[ \t]+'
    pass

def t_error(t):
    print(t)
    loop_syntax_errors.append(f"Syntax error at line {t.lexer.lineno}: character number {t.lexer.lexpos}; Unexpected token '{t.value[0]}'")
    t.lexer.skip(1)

# Define the parser
def p_statements(p):
    '''statements : statement
                  | statements statement'''

def p_statement(p):
    '''statement : for_loop
                 | other_statement
                 | empty_statement'''
def p_loop_body(p):
    '''loop_body : statement
                 | INDENT statements DEDENT
                 | comment '''
def p_comment(p):
    '''comment : COMMENT'''

def p_for_loop(p):
    '''for_loop : FOR LPAREN expressions RPAREN LBRACE  RBRACE'''

def p_other_statement(p):
    '''other_statement : IDENTIFIER SEMICOLON'''

def p_empty_statement(p):
    '''empty_statement : SEMICOLON'''

def p_expressions(p):
    ''' expressions : expression
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

# Create the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Sample C# code with loops
sample_input = '''
for (int i = 0 i < 5; i++)
{
    // loop_body
}
'''

# Parse the C-like code and validate loops
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