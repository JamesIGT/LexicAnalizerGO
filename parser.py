import ply.yacc as yacc
from lexer import tokens, reserved # Importa tus tokens desde lexer.py
import os
import logging
from datetime import datetime

usuario_git = "vnguti"
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

# === REGLAS SINTÁCTICAS ===

def p_program(p):
    'program : PACKAGE MAIN imports declarations main_function'
    logging.info("Regla: program → PACKAGE MAIN ...")

def p_imports(p):
    'imports : IMPORT LPAREN import_list RPAREN'
    logging.info("Regla: imports → IMPORT (...)")

def p_import_list(p):
    '''import_list : import_list STRING
                   | STRING'''
    logging.info("Regla: import_list")

def p_main_function(p):
    'main_function : FUNC MAIN LPAREN RPAREN block'
    logging.info("Regla: main_function")

def p_block(p):
    'block : LBRACE statements RBRACE'
    logging.info("Regla: block")

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    logging.info("Regla: statements")

def p_statement(p):
    '''statement : VARIABLE ASSIGN expression SEMICOLON
                 | function_call SEMICOLON
                 | for_loop
                 | if_statement
                 | declaration'''
    logging.info("Regla: statement")

def p_for_loop(p):
    'for_loop : FOR expression block'
    logging.info("Regla: for")

def p_if_statement(p):
    '''if_statement : IF expression block
                    | IF expression block ELSE block'''
    logging.info("Regla: if")

def p_function_call(p):
    '''function_call : VARIABLE DOT VARIABLE LPAREN arguments RPAREN
                     | VARIABLE LPAREN arguments RPAREN'''
    logging.info("Regla: función o método")

def p_arguments(p):
    '''arguments : arguments COMMA expression
                 | expression
                 | empty'''
    logging.info("Regla: argumentos")

def p_expression(p):
    '''expression : STRING
                  | NUMBER
                  | VARIABLE
                  | VARIABLE DOT VARIABLE
                  | VARIABLE LBRACKET expression RBRACKET
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression AND expression
                  | expression OR expression
                  | LPAREN expression RPAREN'''
    logging.info("Regla: expression")

def p_declarations(p):
    '''declarations : declarations declaration
                    | declaration'''
    logging.info("Regla: declarations")

def p_declaration(p):
    '''declaration : type_struct
                   | VAR VARIABLE ASSIGN expression SEMICOLON
                   | FUNC receiver VARIABLE LPAREN params RPAREN block'''
    logging.info("Regla: declaration")

def p_receiver(p):
    'receiver : LPAREN VARIABLE TIMES VARIABLE RPAREN'
    logging.info("Regla: receptor de método")

def p_type_struct(p):
    'type_struct : TYPE VARIABLE STRUCT LBRACE struct_fields RBRACE'
    logging.info("Regla: struct")

def p_struct_fields(p):
    '''struct_fields : struct_fields type VARIABLE
                     | type VARIABLE'''
    logging.info("Regla: campos struct")

def p_params(p):
    '''params : params COMMA param
              | param
              | empty'''
    logging.info("Regla: parámetros")

def p_param(p):
    'param : VARIABLE type'
    logging.info("Regla: parámetro")

def p_type(p):
    '''type : STRING_TYPE
            | INT_TYPE
            | BOOL_TYPE
            | FLOAT64_TYPE'''
    logging.info("Regla: tipo")

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        mensaje = f"[ERROR SINTÁCTICO] Línea {p.lineno}: token inesperado '{p.value}'"
    else:
        mensaje = "[ERROR SINTÁCTICO] Fin de archivo inesperado"
    print(mensaje)
    logging.error(mensaje)

parser = yacc.yacc()

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
