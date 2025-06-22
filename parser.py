import ply.yacc as yacc
from lexer import tokens, reserved  # Asegúrate de que el lexer esté completo
import os
import logging
from datetime import datetime

usuario_git = "dalay20"
os.makedirs("logs", exist_ok=True)
now = datetime.now()
nombre_log = f"sintactico-{usuario_git}-{now.day:02d}-{now.month:02d}-{now.year}-{now.hour:02d}h{now.minute:02d}.txt"
ruta_log = os.path.join("logs", nombre_log)

logging.basicConfig(
    filename=ruta_log,
    filemode='w',
    format='%(message)s',
    level=logging.INFO,
    encoding='utf-8'
)

# === REGLAS SINTÁCTICAS INICIALES ===
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'ASSIGN'),
)

def p_program(p):
    '''program : PACKAGE MAIN import_section function_list
               | PACKAGE MAIN import_section empty
               | PACKAGE VARIABLE import_section function_list
               | PACKAGE VARIABLE import_section empty'''
    logging.info("Regla: program")

def p_import_section(p):
    '''import_section : IMPORT import_list
                      | empty'''
    logging.info("Regla: import_section")

def p_import_list(p):
    '''import_list : STRING
                   | LPAREN string_list RPAREN'''
    logging.info("Regla: import_list")

def p_string_list(p):
    '''string_list : string_list STRING
                   | STRING'''
    logging.info("Regla: string_list")

def p_function_list(p):
    '''function_list : function_list function
                     | function
                     | function_list type_declaration
                     | type_declaration
                     | empty'''
    logging.info("Regla: function_list")

def p_function(p):
    '''function : FUNC VARIABLE LPAREN param_list RPAREN return_type block'''
    logging.info(f"Regla: function con parámetros y retorno → FUNC {p[2]} (...)")

def p_function_with_receiver(p):
    '''function : FUNC LPAREN VARIABLE VARIABLE RPAREN VARIABLE LPAREN param_list RPAREN return_type block
                | FUNC LPAREN VARIABLE VARIABLE RPAREN VARIABLE LPAREN RPAREN return_type block
                | FUNC LPAREN VARIABLE TIMES VARIABLE RPAREN VARIABLE LPAREN param_list RPAREN return_type block
                | FUNC LPAREN VARIABLE TIMES VARIABLE RPAREN VARIABLE LPAREN RPAREN return_type block'''
    logging.info("Regla: función con receptor (método de struct y puntero)")



if __name__ == "__main__":
    try:
        with open("algorithms/algorithm2.go", "r", encoding="utf-8") as f:
            data = f.read()
        result = parser.parse(data)
        if result is None:
            logging.info("✅ Análisis sintáctico completado correctamente.")
            print(f"\n✅ Análisis sintáctico completado. Log guardado en: {ruta_log}")
    except Exception as e:
        logging.error(f"[ERROR GENERAL] {str(e)}")
        print(f"[ERROR] {str(e)}")
