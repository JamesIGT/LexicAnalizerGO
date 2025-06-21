import ply.lex as lex
import os
import logging
from datetime import datetime


# usuario_git = "jamesigt"  # Cambia esto por tu usuario de GitHub

# os.makedirs("logs", exist_ok=True)

# now = datetime.now()
# nombre_log = f"lexico-{usuario_git}-{now.day:02d}-{now.month:02d}-{now.year}-{now.hour:02d}h{now.minute:02d}.txt"
# ruta_log = os.path.join("logs", nombre_log)

# # Configurar logger
# logging.basicConfig(
#     filename=ruta_log,
#     filemode='w',
#     format='%(message)s',
#     level=logging.INFO,
#     encoding='utf-8'
# )

# APORTE HECHO POR JARED GONZALEZ
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
    'EQ', 'NE', 'LT', 'GT', 'LE', 'GE', 'FUNCNAME', 
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

#INICIO DEL APORTE DE VALERIA GUTIERREZ
reserved.update({
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'map': 'MAP',
    'float64': 'FLOAT64_TYPE',
    'var': 'VAR',
})

tokens += ['INCREMENT', 'DECREMENT', 'AND', 'OR']

t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_AND       = r'&&'
t_OR        = r'\|\|'

#FIN DEL APORTE DE VALERIA GUTIERREZ

#INICIO DEL APORTE DE DIEGO ALAY
reserved.update({
    'strings': 'STRINGS',
    'tolower': 'TOLOWER',
    'char': 'CHAR',
    'containsRune': 'CONTAINSRUNE',
    'unicode': 'UNICODE',
    'isletter': 'ISLETTER',
    'isdigit': 'ISDIGIT',
    'runes': 'RUNES',
})
#FIN DEL APORTE DE DIEGO ALAY
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

# Regla para identificar identificadores y palabras clave


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
    mensaje = f"[ERROR] Línea {t.lineno}: Caracter ilegal '{t.value[0]}'"
    print(mensaje)           # Imprime en consola
    logging.info(mensaje)    # Escribe en el log
    t.lexer.skip(1)     

# FIN DEL APORTE DE JARED GONZALEZ

# Construcción del lexer
lexer = lex.lex()

# Prueba con el codigo del algorithm1.go proporcionado
# DIEGO ALAY
if __name__ == "__main__":
    with open("algorithms/algorithm2.go", "r", encoding="utf-8") as f:
        data = f.read()

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        mensaje = f"[TOKEN] Línea {tok.lineno}: Tipo={tok.type}, Valor={tok.value}"
        print(mensaje)
        logging.info(mensaje)

    print(f"\n✅ Análisis completado. Log guardado en: {ruta_log}")


# Prueba con el codigo del algorithm2.go proporcionado
# VALERIA GUTIERREZ
# with open("algorithms/algorithm2.go", "r", encoding="utf-8") as f:

# Prueba con el codigo del algorithm3.go proporcionado
# JARED GONZALEZ
# with open("algorithms/algorithm3.go", "r", encoding="utf-8") as f:

