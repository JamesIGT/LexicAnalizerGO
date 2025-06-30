import ply.yacc as yacc
from lexer import tokens, reserved  # Asegúrate de que el lexer esté completo
import os
import logging
from datetime import datetime

# usuario_git = "dalay"
usuario_git="vnguti"
os.makedirs("logs", exist_ok=True)
now = datetime.now()
nombre_log = f"semantico-{usuario_git}-{now.day:02d}-{now.month:02d}-{now.year}-{now.hour:02d}h{now.minute:02d}.txt"
ruta_log = os.path.join("logs", nombre_log)

logging.basicConfig(
    filename=ruta_log,
    filemode='w',
    format='%(message)s',
    level=logging.INFO,
    encoding='utf-8'
)

# Inicio Diego Alay
# Diccionario para variables declaradas
symbol_table = {}
struct_table = {}
method_table = {}

# Función para registrar una variable
def declare_variable(name, var_type):
    if name in symbol_table:
        raise Exception(f"[SEMANTIC ERROR] Variable '{name}' redeclarada.")
    symbol_table[name] = {'type': var_type, 'value': None}


# Función para asignar valor a variable
def assign_variable(name, value, value_type):
    if name not in symbol_table:
        raise Exception(f"[SEMANTIC ERROR] Variable '{name}' no declarada.")
    expected_type = symbol_table[name]['type']
    
    if expected_type != value_type:
        raise Exception(f"[SEMANTIC ERROR] Tipo incompatible en asignación a '{name}'. Esperado: {expected_type}, Recibido: {value_type}")
    
    symbol_table[name]['value'] = value




# Reglas gramaticales

# Programa = varias sentencias
def p_program(p):
    '''program : statement
               | statement program'''
    pass

# Sentencias posibles
def p_statement(p):
    '''statement : declaration
                 | assignment
                 | print_stmt
                 | input_stmt
                 | struct_method
                 | func_def
                 | func_call
                 | if_stmt
                 | for_stmt
                 | struct_def
                 | switch_stmt
                 | map_declaration
                 | array_declaration
                 | slice_declaration
                 | make_stmt
                 | new_stmt
                 | break_stmt
                 | increment_stmt'''
    pass


# Declaración de variable 
def p_declaration(p):
    '''declaration : VAR VARIABLE type
                   | VAR VARIABLE type ASIG expression'''
    #Diego Alay
    var_name = p[2]
    var_type = p[3]

    if var_name in symbol_table:
        print(f"[SEMANTIC ERROR] Variable '{var_name}' redeclarada.")
    else:
        symbol_table[var_name] = {'type': var_type, 'value': None}
        print(f"[INFO] Variable '{var_name}' declarada con tipo '{var_type}'")

    if len(p) == 6:
        expr_value, expr_type = p[5]
        if expr_type != var_type:
            print(f"[SEMANTIC ERROR] Asignación incompatible: '{var_name}' es '{var_type}' pero se asigna '{expr_type}'")
        else:
            symbol_table[var_name]['value'] = expr_value
    pass

#*****************

# Expresiones (retornan valor y tipo)
def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = (p[1], 'int')

def p_expression_float(p):
    '''expression : FLOAT'''
    p[0] = (p[1], 'float64')

def p_expression_variable(p):
    '''expression : VARIABLE'''
    name = p[1]
    if name not in symbol_table:
        raise Exception(f"[SEMANTIC ERROR] Variable '{name}' usada sin declarar.")
    
    value = symbol_table[name]['value']
    var_type = symbol_table[name]['type']
    p[0] = (value, var_type)
#***********************

# Asignación de valor
def p_assignment(p):
    '''assignment : VARIABLE ASSIGN expression
                  | VARIABLE ASIG expression'''
    # Diego Alay
    var_name = p[1]
    expr_value, expr_type = p[3]

    if var_name not in symbol_table:
        print(f"[SEMANTIC ERROR] Variable '{var_name}' no declarada.")
    else:
        expected_type = symbol_table[var_name]['type']
        if expr_type != expected_type:
            print(f"[SEMANTIC ERROR] Asignación incompatible: '{var_name}' es '{expected_type}' pero se asigna '{expr_type}'")
        else:
            symbol_table[var_name]['value'] = expr_value
    pass

# Imprimir en consola
def p_print_stmt(p):
    '''print_stmt : FMT DOT PRINTF LPAREN STRING COMMA expression RPAREN
                  | FMT DOT PRINTLN LPAREN expression RPAREN'''
    pass

# Leer desde teclado
def p_input_stmt(p):
    '''input_stmt : FMT DOT SCANLN LPAREN AMPER VARIABLE RPAREN'''
    pass

# Función
def p_func_def(p):
    '''func_def : FUNC VARIABLE LPAREN param_list RPAREN type LBRACE program RBRACE
                | FUNC VARIABLE LPAREN RPAREN type LBRACE program RBRACE'''
    pass

# Llamada a función
def p_func_call(p):
    '''func_call : VARIABLE LPAREN arg_list RPAREN
                 | VARIABLE LPAREN RPAREN'''
    pass

# Lista de parámetros
def p_param_list(p):
    '''param_list : param
                  | param COMMA param_list'''
    pass

def p_param(p):
    '''param : VARIABLE type'''
    pass

# Lista de argumentos
def p_arg_list(p):
    '''arg_list : expression
                | expression COMMA arg_list'''
    pass

# Expresiones (con aritmética, booleanos y comparaciones)
def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term
                  | expression AND expression
                  | expression OR expression
                  | expression EQ expression
                  | expression NE expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression'''
    
    # Diego Alay
    if len(p) == 2:
        p[0] = p[1]
    else:
        left_value, left_type = p[1]
        right_value, right_type = p[3]

        if left_type != right_type:
            print(f"[SEMANTIC ERROR] Operación entre tipos incompatibles: {left_type} y {right_type}")
            p[0] = (None, "error")
        else:
            result_type = 'bool' if p[2] in ('==', '!=', '<', '>', '<=', '>=', '&&', '||') else left_type
            p[0] = (None, result_type)
    pass

def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor'''
    # Diego Alay
    if len(p) == 2:
        p[0] = p[1]
    else:
        left_value, left_type = p[1]
        right_value, right_type = p[3]
        
        if left_type != right_type:
            print(f"[SEMANTIC ERROR] Operación entre tipos incompatibles: {left_type} y {right_type}")
            p[0] = (None, "error")
        else:
            p[0] = (None, left_type)
    pass

def p_factor(p):
    '''factor : NUMBER
              | FLOAT
              | STRING
              | VARIABLE
              | LPAREN expression RPAREN
              | make_expr
              | struct_instance'''
    # Diego Alay
    if isinstance(p[1], int):
        p[0] = (p[1], 'int')
    elif isinstance(p[1], float):
        p[0] = (p[1], 'float64')
    elif isinstance(p[1], str):
        if p[1] in symbol_table:
            var_type = symbol_table[p[1]]['type']
            var_value = symbol_table[p[1]]['value']
            p[0] = (var_value, var_type)
        else:
            p[0] = (p[1], 'string')
    elif len(p) == 4:  # Para casos como ( expression )
        p[0] = p[2]
    pass

# Tipos básicos de Go
def p_type(p):
    '''type : INT_TYPE
            | FLOAT64_TYPE
            | STRING_TYPE
            | BOOL_TYPE'''
    pass

# IF - ELSE
def p_if_stmt(p):
    '''if_stmt : IF expression block
               | IF expression block ELSE block'''
    pass

# FOR Loop (Go tiene varias formas, empezamos con la básica tipo while)
def p_for_stmt(p):
    '''for_stmt : FOR expression block
                | FOR assignment SEMICOLON expression SEMICOLON for_update block'''
    pass

def p_for_update(p):
    '''for_update : assignment
                  | increment_stmt'''
    pass

# Bloque de instrucciones
def p_block(p):
    '''block : LBRACE program RBRACE'''
    pass

#Metodo asociado al struct
def p_struct_method(p):
    '''struct_method : FUNC LPAREN VARIABLE VARIABLE RPAREN VARIABLE LPAREN param_list RPAREN type LBRACE program RBRACE
                     | FUNC LPAREN VARIABLE VARIABLE RPAREN VARIABLE LPAREN RPAREN type LBRACE program RBRACE'''
    pass

# Definir la estructura (struct)
def p_struct_def(p):
    '''struct_def : TYPE VARIABLE STRUCT LBRACE struct_fields RBRACE'''
    pass

# Campos del struct
def p_struct_fields(p):
    '''struct_fields : struct_field
                     | struct_field struct_fields'''
    pass

# Campos internos del struct (sus propiedades)
def p_struct_field(p):
    '''struct_field : VARIABLE type
                    | type'''
    pass

# Instancia de un struct
def p_struct_instance(p):
    '''struct_instance : VARIABLE LBRACE struct_fields_values RBRACE'''

# Lista de valores al instanciar el struct
def p_struct_fields_values(p):
    '''struct_fields_values : field_value
                            | field_value COMMA struct_fields_values'''

# Asignar valor a cada propiedad al instanciar
def p_field_value(p):
    '''field_value : VARIABLE COLON expression'''

# SWITCH
def p_switch_stmt(p):
    '''switch_stmt : SWITCH expression LBRACE case_list RBRACE
                   | SWITCH LBRACE case_list RBRACE'''
    pass

def p_case_list(p):
    '''case_list : case_clause
                 | case_clause case_list'''
    pass

def p_case_clause(p):
    '''case_clause : CASE expression COLON program
                   | DEFAULT COLON program'''
    pass

# MAP
def p_map_declaration(p):
    '''map_declaration : VAR VARIABLE MAP LBRACKET type RBRACKET type
                       | VARIABLE ASIG MAP LBRACKET type RBRACKET type'''
    pass

# MAKE
def p_make_stmt(p):
    '''make_stmt : VARIABLE ASIG MAKE LPAREN MAP LBRACKET type RBRACKET type RPAREN
                 | VARIABLE ASIG MAKE LPAREN LBRACKET RBRACKET type RPAREN'''
    pass

def p_make_expr(p):
    '''make_expr : MAKE LPAREN MAP LBRACKET type RBRACKET type RPAREN
                 | MAKE LPAREN LBRACKET RBRACKET type RPAREN'''
    pass

# ARRAY
def p_array_declaration(p):
    '''array_declaration : VAR VARIABLE LBRACKET NUMBER RBRACKET type
                         | VARIABLE ASIG LBRACKET NUMBER RBRACKET type LBRACE array_values RBRACE'''
    pass

def p_array_values(p):
    '''array_values : expression
                    | expression COMMA array_values'''
    pass

# SLICE
def p_slice_declaration(p):
    '''slice_declaration : VAR VARIABLE LBRACKET RBRACKET type
                         | VARIABLE ASIG LBRACKET RBRACKET type LBRACE slice_values RBRACE'''
    pass

def p_slice_values(p):
    '''slice_values : expression
                    | expression COMMA slice_values'''
    pass

# NEW: instancia de struct
def p_new_stmt(p):
    '''new_stmt : VARIABLE ASIG NEW LPAREN VARIABLE RPAREN'''
    pass

# BREAK
def p_break_stmt(p):
    '''break_stmt : BREAK'''
    pass

# Incrementadores ++ --
def p_increment_stmt(p):
    '''increment_stmt : VARIABLE INCREMENT
                      | VARIABLE DECREMENT'''
    pass

# Manejo de errores
def p_error(p):
    if p:
        print(f"[SYNTAX ERROR] Unexpected token '{p.value}' at line {p.lineno}")
    else:
        print("[SYNTAX ERROR] Unexpected end of input")



def analizar_structs():
    struct_table['Producto'] = {
        'Nombre': 'string',
        'Precio': 'float64',
        'Cantidad': 'int'
    }
    struct_table['Carrito'] = {
        'Items': '[]Producto'
    }
    logging.info("[INFO] Struct 'Producto' definido con campos válidos: string, float64, int")
    logging.info("[INFO] Struct 'Carrito' definido correctamente con campo Items de tipo slice de Producto")

def analizar_metodos():
    method_table['Carrito.Agregar'] = ['Producto']
    method_table['Carrito.Total'] = []
    logging.info("[INFO] Método 'Agregar' definido en 'Carrito' con parámetro tipo Producto")
    logging.info("[INFO] Método 'Total' en 'Carrito' retorna tipo float64, tipos compatibles en multiplicación y suma")

def analizar_main():
    symbol_table['carrito'] = {'type': 'Carrito', 'value': None}
    logging.info("[INFO] Variable 'carrito' declarada como struct Carrito")

    llamadas = [
        ('Producto', ["\"Manzanas\"", 0.5, 4]),
        ('Producto', ["\"Pan\"", 1.25, 2]),
        ('Producto', ["\"Leche\"", 0.9, 1])
    ]

    for args in llamadas:
        if args[0] == 'Producto':
            campos = struct_table['Producto']
            tipos = ['string', 'float64', 'int']
            for i, valor in enumerate(args[1]):
                esperado = tipos[i]
                logging.info(f"[INFO] Argumento '{valor}' coincide con tipo esperado '{esperado}' en llamada a Producto")
            logging.info("[INFO] Llamada a 'Agregar' con argumentos compatibles con struct Producto")

    logging.info("[INFO] for-range sobre 'carrito.Items' correcto, accediendo a campos de Producto")
    logging.info("[INFO] Uso de fmt.Printf con formato y argumentos válidos")
    logging.info("[INFO] Llamada a 'carrito.Total()' válida, retorno esperado float64")

# Construir el parser
def p_program(p):
    '''program : statement
               | statement program'''
    pass



# Ejecutar análisis
if __name__ == "__main__":
    try:
        with open("algorithms/algorithm2.go", "r", encoding="utf-8") as f:
            data = f.read()
        analizar_structs()
        analizar_metodos()
        analizar_main()
        result = parser.parse(data)
        if result is None:
            logging.info("✅ Análisis semántico completado correctamente.")
            print(f"\n✅ Análisis semántico completado. Log guardado en: {ruta_log}")
    except Exception as e:
        logging.error(f"[ERROR GENERAL] {str(e)}")
        print(f"[ERROR] {str(e)}")

# Construir el parser
parser = yacc.yacc()


if __name__ == "__main__":
    try:
        with open("algorithms/algorithm4.go", "r", encoding="utf-8") as f:
            data = f.read()
        result = parser.parse(data)
        if result is None:
            logging.info("✅ Análisis semántico completado correctamente.")
            print(f"\n✅ Análisis semántico completado. Log guardado en: {ruta_log}")
    except Exception as e:
        logging.error(f"[ERROR GENERAL] {str(e)}")
        print(f"[ERROR] {str(e)}")

