import ply.lex as lex

# Lista de tokens
tokens = [
    'VARIABLE',
    'NUMBER',
    'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'ASSIGN',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',
    'SEMICOLON', 'COLON', 'COMMA', 'DOT',
    'AMPER',
    'EQ', 'NE', 'LT', 'GT', 'LE', 'GE',
]

# Palabras clave de Go
reserved = {
    'main' : 'MAIN',
    'package': 'PACKAGE',
    'import': 'IMPORT',
    'func': 'FUNC',
    'type': 'TYPE',
    'struct': 'STRUCT',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'range': 'RANGE',
    'true': 'TRUE',
    'false': 'FALSE',
    'string': 'STRING_TYPE',
    'int': 'INT_TYPE',
    'bool': 'BOOL_TYPE',
    'return': 'RETURN',
    'append': 'APPEND',
    'len': 'LENGTH',
    'Printf': 'PRINTF',
    'Println': 'PRINTLN',
}

tokens += list(reserved.values())

# Reglas de expresiones regulares para tokens simples
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_MOD        = r'%'
t_ASSIGN     = r'='
t_EQ         = r'=='
t_NE         = r'!='
t_LT         = r'<'
t_GT         = r'>'
t_LE         = r'<='
t_GE         = r'>='
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'
t_SEMICOLON  = r';'
t_COLON      = r':'
t_COMMA      = r','
t_DOT        = r'\.'
t_AMPER      = r'\&'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Comentarios de línea
def t_COMMENT(t):
    r'\/\/.*'
    pass  # Ignora los comentarios

# Comentarios de bloque
def t_COMMENT_BLOCK(t):
    r'/\*(.|\n)*?\*/'
    pass

# Cadenas de texto
def t_STRING(t):
    r'"([^\\"]|\\.)*"'
    return t

# Números (enteros)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FUNCNAME(t):
    r'func\s+([a-zA-Z_][a-zA-Z0-9_]*)'
    t.value = t.value.split()[1]  # Extraer solo el nombre de la función
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE') # Verifica si es variable
    return t

# Contar líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en línea {t.lexer.lineno}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Prueba con el código Go proporcionado
if __name__ == "__main__":
    with open("algorithms/algorithm3.go", "r", encoding="utf-8") as f:
        data = f.read()
    lexer.input(data)
    for tok in lexer:
        print(tok)
