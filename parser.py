import ply.yacc as yacc
from lexer import tokens, reserved  # Asegúrate de que el lexer esté completo
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

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param
                  | empty'''
    logging.info("Regla: lista de parámetros")

def p_param(p):
    '''param : VARIABLE type'''
    logging.info("Regla: parámetro")

def p_return_type(p):
    '''return_type : type
                   | LPAREN type_list RPAREN
                   | empty'''
    logging.info("Regla: tipo de retorno")

def p_type_list(p):
    '''type_list : type_list COMMA type
                 | type'''
    logging.info("Regla: lista de tipos")

def p_type(p):
    '''type : STRING_TYPE
            | INT_TYPE
            | BOOL_TYPE
            | FLOAT64_TYPE
            | VARIABLE
            | LBRACKET RBRACKET VARIABLE'''
    logging.info("Regla: tipo")

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    logging.info("Regla: block → LBRACE statement_list RBRACE")

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    logging.info("Regla: statement_list → statement_list statement | ε")

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | short_declaration
                 | if_statement
                 | for_loop
                 | function_call SEMICOLON
                 | RETURN expression_list
                 | RETURN expression_list SEMICOLON
                 | FOR VARIABLE COMMA VARIABLE ASSIGN_SHORT RANGE variable block
                 | variable INCREMENT
                 | variable DECREMENT
                 | SWITCH LBRACE case_list RBRACE
                 | SWITCH expression LBRACE case_list RBRACE
                 | type_declaration'''
    logging.info("Regla: statement")

def p_declaration(p):
    '''declaration : VAR VARIABLE ASSIGN expression
                   | VAR VARIABLE ASSIGN expression SEMICOLON'''
    logging.info("Regla: declaración")

def p_assignment(p):
    '''assignment : variable ASSIGN expression
                 | variable ASSIGN expression SEMICOLON'''
    logging.info("Regla: assignment")

def p_assignment_compound(p):
    '''assignment : variable PLUS_ASSIGN expression
                 | variable MINUS_ASSIGN expression
                 | variable TIMES_ASSIGN expression
                 | variable DIVIDE_ASSIGN expression'''
    logging.info("Regla: assignment compuesto")

def p_if_statement(p):
    '''if_statement : IF expression block else_clause'''
    logging.info("Regla: if")

def p_else_clause(p):
    '''else_clause : ELSE block
                   | empty'''
    logging.info("Regla: else")

def p_for_loop(p):
    '''for_loop : FOR VARIABLE ASSIGN expression SEMICOLON expression SEMICOLON assignment block
                | FOR VARIABLE ASSIGN_SHORT expression SEMICOLON expression SEMICOLON increment_statement block
                | FOR variable_list ASSIGN_SHORT RANGE variable block'''
    logging.info("Regla: for")

def p_increment_statement(p):
    '''increment_statement : variable INCREMENT
                           | variable DECREMENT'''
    logging.info("Regla: incremento/decremento")

def p_function_call(p):
    '''function_call : variable LPAREN argument_list RPAREN
                     | variable LPAREN RPAREN
                     | APPEND LPAREN argument_list RPAREN
                     | APPEND LPAREN RPAREN
                     | variable DOT APPEND LPAREN argument_list RPAREN
                     | variable DOT APPEND LPAREN RPAREN
                     | PRINTLN LPAREN argument_list RPAREN
                     | PRINTLN LPAREN RPAREN
                     | variable DOT PRINTLN LPAREN argument_list RPAREN
                     | variable DOT PRINTLN LPAREN RPAREN
                     | PRINTF LPAREN argument_list RPAREN
                     | PRINTF LPAREN RPAREN
                     | variable DOT PRINTF LPAREN argument_list RPAREN
                     | variable DOT PRINTF LPAREN RPAREN'''
    logging.info("Regla: llamada a función")

def p_argument_list(p):
    '''argument_list : expression
                     | argument_list COMMA expression'''
    logging.info("Regla: argumentos")

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression AND expression
                  | expression OR expression
                  | LPAREN expression RPAREN
                  | NUMBER
                  | variable
                  | function_call
                  | STRING
                  | TRUE
                  | FALSE'''
    logging.info("Regla: expresión")

def p_expression_type_cast(p):
    '''expression : LBRACKET RBRACKET variable LPAREN expression RPAREN'''
    logging.info("Regla: conversión tipo → []tipo(expr)")

def p_expression_type_cast_simple(p):
    '''expression : FLOAT64_TYPE LPAREN expression RPAREN
                  | INT_TYPE LPAREN expression RPAREN
                  | STRING_TYPE LPAREN expression RPAREN
                  | BOOL_TYPE LPAREN expression RPAREN
                  | VARIABLE LPAREN expression RPAREN'''
    logging.info("Regla: conversión simple → tipo(expr)")

def p_type_declaration(p):
    '''type_declaration : TYPE VARIABLE STRUCT LBRACE struct_fields RBRACE'''
    logging.info("Regla: struct")

def p_struct_fields(p):
    '''struct_fields : struct_fields struct_field
                     | struct_field
                     | empty'''
    logging.info("Regla: campos struct")

def p_struct_field(p):
    '''struct_field : VARIABLE type
                    | empty'''
    logging.info("Regla: campo de struct")

def p_expression_struct_literal(p):
    '''expression : VARIABLE LBRACE field_list RBRACE'''
    logging.info("Regla: struct literal")

def p_field_list(p):
    '''field_list : field_list COMMA field
                  | field
                  | empty'''
    logging.info("Regla: lista de campos")

def p_field(p):
    '''field : VARIABLE COLON expression'''
    logging.info("Regla: campo literal")

def p_variable(p):
    '''variable : VARIABLE
                | variable DOT VARIABLE
                | variable LBRACKET expression RBRACKET'''
    logging.info("Regla: variable")

def p_short_declaration(p):
    '''short_declaration : variable_list ASSIGN_SHORT expression_list
                         | variable_list ASSIGN_SHORT expression_list SEMICOLON'''
    logging.info("Regla: declaración corta")

def p_variable_list(p):
    '''variable_list : variable
                     | variable COMMA variable_list'''
    logging.info("Regla: lista de variables")

def p_expression_list(p):
    '''expression_list : expression
                       | expression COMMA expression_list'''
    logging.info("Regla: lista de expresiones")

def p_case_list(p):
    '''case_list : case_list case
                 | case'''
    logging.info("Regla: lista de casos")

def p_case(p):
    '''case : CASE expression COLON statement_list
            | DEFAULT COLON statement_list'''
    logging.info("Regla: case/default")

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print(f"[ERROR] Línea {p.lineno}: Error de sintaxis cerca de '{p.value}' (tipo: {p.type})")
        with open("algorithms/algorithm3.go", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if p.lineno <= len(lines):
                print(f"Línea {p.lineno}: {lines[p.lineno-1].strip()}")
    else:
        print("Error de sintaxis al final del archivo")

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
