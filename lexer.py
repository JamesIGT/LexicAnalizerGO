import ply.lex as lex
import os
import logging
from datetime import datetime


# usuario_git = "dalay"  # Cambia esto por tu usuario de GitHub

# os.makedirs("logs", exist_ok=True)

# now = datetime.now()
# nombre_log = f"lexico-{usuario_git}-{now.day:02d}-{now.month:02d}-{now.year}-{now.hour:02d}h{now.minute:02d}.txt"
# ruta_log = os.path.join("logs", nombre_log)

# #Configurar logger
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
    'EQ', 'NE', 'LT', 'GT', 'LE', 'GE', 'FUNCNAME', 'FLOAT', 
]

# Palabras clave de Go
reserved = {
    'package': 'PACKAGE',
    'main': 'MAIN',
    'import': 'IMPORT',
    'continue': 'CONTINUE',
    'func': 'FUNC',
    'type': 'TYPE',
    'true': 'TRUE',
    'false': 'FALSE',
    'return': 'RETURN',
    #estructura de datos
    'struct': 'STRUCT',
    'range': 'RANGE',
    #estructura de control
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    #tipos de datos
    'string': 'STRING_TYPE',
    'int': 'INT_TYPE',
    'bool': 'BOOL_TYPE',
    #libreria
    'Printf': 'PRINTF',
    'Println': 'PRINTLN',
    'Print': 'PRINT',

}

#INICIO DEL APORTE DE VALERIA GUTIERREZ
reserved.update({
    'var': 'VAR',
    #estructura de control
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK',
    #estructura de datos
    'map': 'MAP',
    # tipos de datos
    'float64': 'FLOAT64_TYPE',

})

tokens += ['INCREMENT', 'DECREMENT', 'AND', 'OR', 'NOT', "ASIG",]

t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_AND       = r'&&'
t_OR        = r'\|\|'
t_ASIG = r':='
t_NOT = r'!'

#FIN DEL APORTE DE VALERIA GUTIERREZ

#INICIO DEL APORTE DE DIEGO ALAY
reserved.update({
    #tipo de dato
    'uint':'UINT',
    #liberia
    'fmt': 'FMT',
    'Scanln': 'SCANLN',
    'make': 'MAKE',
    #estructura de datos
    'new': 'NEW',

})
#FIN DEL APORTE DE DIEGO ALAY
tokens += list(reserved.values())

# Reglas de expresiones regulares para tokens simples
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_MOD        = r'%'
t_ASSIGN     = r'\='
t_EQ         = r'=='
t_NE         = r'!='
t_LT         = r'<'
t_LE         = r'<='
t_GT         = r'\^'
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

def t_FLOAT(t):
    r'[0-9]*\.[0-9]+'
    t.value = float(t.value)
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
# Fin de expresiones regulares

# Prueba con el codigo del algorithm1.go proporcionado
# DIEGO ALAY
# if __name__ == "__main__":
#     with open("algorithms/algorithm4.go", "r", encoding="utf-8") as f:
#         data = f.read()

#     lexer.input(data)

#     while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         mensaje = f"[TOKEN] Línea {tok.lineno}: Tipo={tok.type}, Valor={tok.value}"
#         print(mensaje)
#         logging.info(mensaje)

#     print(f"\n✅ Análisis completado. Log guardado en: {ruta_log}")

