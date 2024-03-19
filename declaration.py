from ply import lex, yacc

# Define the tokens
tokens = ('DATATYPE', 'VARIABLE', 'SEMICOLON')

# Define regular expressions for tokens
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_SEMICOLON = r';'
t_DATATYPE = r'\b(int|float|string|bool|char|double)\b'

# Define a list to store syntax errors
syntax_errors = []

# Define the lexer
def t_error(t):
    syntax_errors.append(f"Syntax error at line {t.lineno}: Unexpected token '{t.value[0]}'")
    t.lexer.skip(1)


# Add a rule to ignore spaces and tabs
t_ignore = ' \t'

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

# Define the parser
def p_program(p):
    '''program : declarations'''
    pass

def p_declarations(p):
    '''declarations : declaration
                   | declarations declaration'''

def p_declaration(p):
    '''declaration : DATATYPE VARIABLE SEMICOLON'''
    datatype = p[1].lower()
    variable = p[2]
    
    allowed_datatypes = {'int', 'float', 'string', 'bool','char','double'}
   
    
    if datatype not in allowed_datatypes:
        syntax_errors.append(f"Syntax error at line {p.lineno(1)}: Invalid datatype '{datatype}'")
    
    if not variable.isidentifier():
        syntax_errors.append(f"Syntax error at line {p.lineno(2)}: Invalid variable name '{variable}'")

def p_error(p):
    if p:
        syntax_errors.append(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
    else:
        syntax_errors.append("Syntax error at EOF")

parser = yacc.yacc()

# Sample input (with spaces and newlines)
input_text = '''float int_var ;
int i ;
string h;
char c;
string j_var ;
'''

# Parse the input
lexer.input(input_text)
for token in lexer:
    pass
parser.parse(input_text)

# Check for syntax errors
if not syntax_errors:
    print("Syntax is valid.")


else:
    print("Syntax errors:")
    for error in syntax_errors:
        print(error)