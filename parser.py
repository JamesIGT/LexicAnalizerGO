import ply.yacc as yacc
from lexer import tokens, reserved  # Asegúrate de que el lexer esté completo
import os
import logging
from datetime import datetime

usuario_git = "dalay"
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
def report_error(mensaje):
    print(mensaje)
    logging.error(mensaje)

# Inicio Diego Alay
# Diccionario para variables declaradas
symbol_table = {}

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

# Inicio Jared Gonzalez
# Pila para controlar el contexto (por ejemplo, si estamos dentro de un bucle)
context_stack = []

# Tabla para almacenar funciones declaradas
function_table = {}
def declare_function(name, return_type, params=None):
    if name in function_table:
        raise Exception(f"[SEMANTIC ERROR] Función '{name}' redeclarada.")
    function_table[name] = {'return_type': return_type, 'params': params or [], 'has_return': False}



# Reglas gramaticales


# Programa = varias sentencias
# Detectar 'package main'
def p_start(p):
    '''start : PACKAGE VARIABLE import_stmt program'''
    if p[2] != 'main':
        report_error(f"[SEMANTIC ERROR] Se esperaba 'main' como nombre del paquete, pero se recibió '{p[2]}'")


def p_import_function(p):
    '''import_stmt : IMPORT LPAREN STRING RPAREN
                    | IMPORT STRING'''
    pass

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
                 | continue_stmt
                 | struct_method
                 | func_def
                 | func_no_params
                 | func_call
                 | if_stmt
                 | for_stmt
                 | struct_def
                 | switch_stmt
                 | map_declaration
                 | map_declaration_values
                 | array_declaration
                 | array_literal
                 | slice_declaration
                 | make_stmt
                 | new_stmt
                 | break_stmt
                 | increment_stmt
                 | return_stmt'''
    p[0] = p[1]


# Declaración de variable 
def p_declaration(p):
    '''declaration : VAR VARIABLE type 
                   | VAR VARIABLE type ASIG expression
                   | VAR VARIABLE type ASSIGN expression'''
    #Diego Alay
    var_name = p[2]
    var_type = p[3]

    if var_name in symbol_table:
        report_error(f"[SEMANTIC ERROR] Variable '{var_name}' redeclarada.")
    else: # Declaración básica
        symbol_table[var_name] = {'type': var_type, 'value': None}
        report_error(f"[INFO] Variable '{var_name}' declarada con tipo '{var_type}'")

    if len(p) == 6:
        expr_value, expr_type = p[5]
        if expr_type != var_type:
            report_error(f"[SEMANTIC ERROR] Asignación incompatible: '{var_name}' es '{var_type}' pero se asigna '{expr_type}'")
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
        report_error(f"[SEMANTIC ERROR] Variable '{name}' usada sin declarar.")
        p[0] = (None, 'error')  # ← necesario
        return
    value = symbol_table[name]['value']
    var_type = symbol_table[name]['type']
    p[0] = (value, var_type)  # ← siempre se debe asignar p[0]

#***********************

# Asignación de valor
def p_assignment(p):
    '''assignment : VARIABLE ASSIGN expression
                  | VARIABLE ASIG expression'''
    var_name = p[1]

    if p[3] is None or not isinstance(p[3], tuple):
        report_error(f"[SEMANTIC ERROR] Expresión inválida en asignación a '{var_name}'.")
        return

    expr_value, expr_type = p[3]

    if var_name not in symbol_table:
        report_error(f"[SEMANTIC ERROR] Variable '{var_name}' no declarada.")
    else:
        expected_type = symbol_table[var_name]['type']
        if expr_type != expected_type:
            report_error(f"[SEMANTIC ERROR] Asignación incompatible: '{var_name}' es '{expected_type}' pero se asigna '{expr_type}'")
        else:
            symbol_table[var_name]['value'] = expr_value


# Imprimir en consola
def p_print_stmt(p):
    '''print_stmt : FMT DOT PRINTF LPAREN STRING COMMA expression RPAREN
                  | FMT DOT PRINTLN LPAREN expression RPAREN
                  | FMT DOT PRINTLN LPAREN STRING COMMA VARIABLE RPAREN'''
    if p[3] == 'Printf':
        string_literal = p[5]
        expr_value, expr_type = p[7]
        print(f"[INFO] Printf con formato: {string_literal}, valor: {expr_value} (tipo: {expr_type})")
    else:  # Println
        expr_value, expr_type = p[5]
        print(f"[INFO] Println: {expr_value} (tipo: {expr_type})")

# Leer desde teclado
def p_input_stmt(p):
    '''input_stmt : FMT DOT SCANLN LPAREN AMPER VARIABLE RPAREN'''
    pass

# Función
def p_func_def(p):
    '''func_def : func_header func_body'''
    func_name = p[1]

def p_func_header(p):
    '''func_header : FUNC VARIABLE LPAREN param_list RPAREN type'''
    func_name = p[2]
    params = p[4]
    return_type = p[6]

    param_types = [ptype for _, ptype in params]
    declare_function(func_name, return_type, param_types)
    p[0] = func_name  # opcional

def p_func_body(p):
    '''func_body : LBRACE program RBRACE'''
    pass


# Retorno de la funcion
def p_return_stmt(p):
    '''return_stmt : RETURN expression'''
    print("return_stmt len:", len(p))
    print("return_stmt slice:", p.slice)
    print("p[2] =", p[2])
    print("type(p[2]) =", type(p[2]))

    if not function_table:
        report_error("[SEMANTIC ERROR] 'return' fuera de una función.")
        return
    
    # Obtenemos la función actual (última registrada)
    current_function = list(function_table.keys())[-1]
    expected_type = function_table[current_function]['return_type']

    expr_value, expr_type = p[2]
    function_table[current_function]['has_return'] = True

    if expr_type != expected_type:
        report_error(f"[SEMANTIC ERROR] Retorno incompatible en función '{current_function}': se espera '{expected_type}' pero se retorna '{expr_type}'")

#Jared Gonzalez
# Funcion sin parametros
def p_func_def_no_params(p):
    '''func_no_params : FUNC VARIABLE LPAREN RPAREN type LBRACE program RBRACE'''
    func_name = p[2]
    return_type = p[5]
    declare_function(func_name, return_type, [])

def p_func_def_no_params_void(p):
    '''func_no_params : FUNC VARIABLE LPAREN RPAREN LBRACE program RBRACE'''
    func_name = p[2]
    declare_function(func_name, 'void', [])  # o 'None', si prefieres

def p_func_call(p):
    '''func_call : VARIABLE LPAREN arg_list RPAREN
                 | VARIABLE LPAREN RPAREN'''
    func_name = p[1]

    if func_name not in function_table:
        report_error(f"[SEMANTIC ERROR] Función '{func_name}' no declarada.")
        p[0] = (None, 'error')
        return

    func_info = function_table[func_name]
    expected_params = func_info.get('params', [])

    if len(p) == 4:  # Sin argumentos
        if len(expected_params) != 0:
            report_error(f"[SEMANTIC ERROR] Función '{func_name}' espera {len(expected_params)} argumentos, pero no se proporcionaron.")
        p[0] = (None, func_info['return_type'])

    elif len(p) == 5:  # Con argumentos
        args = p[3]
        if args is None:
            report_error(f"[SEMANTIC ERROR] Argumentos inválidos en llamada a '{func_name}'.")
            p[0] = (None, 'error')
            return

        if len(args) != len(expected_params):
            report_error(f"[SEMANTIC ERROR] Función '{func_name}' espera {len(expected_params)} argumentos, pero se recibieron {len(args)}.")
            p[0] = (None, 'error')
            return

        for i, ((_, arg_type), expected_type) in enumerate(zip(args, expected_params)):
            if arg_type != expected_type:
                report_error(f"[SEMANTIC ERROR] Argumento {i+1} de '{func_name}' tiene tipo '{arg_type}', se esperaba '{expected_type}'.")

        p[0] = (None, func_info['return_type'])
    else:
        # Protección extra: nunca dejar sin asignar p[0]
        report_error(f"[SYNTAX ERROR] Llamada a función mal formada.")
        p[0] = (None, 'error')


# Lista de parámetros
def p_param_list(p):
    '''param_list : param
                  | param COMMA param_list'''
    print("param_list len:", len(p))
    print("param_list slice:", p.slice)
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_param(p):  
    '''param : VARIABLE type'''
    print("param len:", len(p))
    print("param slice:", p.slice)
    var_name = p[1]
    var_type = p[2]
    p[0] = (var_name, var_type)

    if var_name in symbol_table:
        report_error(f"[SEMANTIC ERROR] Parámetro '{var_name}' ya fue declarado.")
    else:
        symbol_table[var_name] = {'type': var_type, 'value': None}

# Lista de argumentos
def p_arg_list(p):
    '''arg_list : expression
                | expression COMMA arg_list'''
    if len(p) == 2:
        # Solo un argumento
        p[0] = [p[1]]
    else:
        # Lista de argumentos acumulada
        p[0] = [p[1]] + p[3]

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
    
    if len(p) == 2:
        # Aquí p[1] debe ser una tupla (valor, tipo)
        if p[1] is None:
            report_error("[SEMANTIC ERROR] Expresión inválida (None) en expresión simple")
            p[0] = (None, 'error')
        else:
            p[0] = p[1]

    else:
        left_value, left_type = p[1]
        right_value, right_type = p[3]
        op = p[2]

        if left_type != right_type:
            if op == '+' and left_type == 'string' and right_type == 'string':
                p[0] = (None, 'string')
                return
            else:
                report_error(f"[SEMANTIC ERROR] Operación entre tipos incompatibles: {left_type} y {right_type}")
                p[0] = (None, "error")
                return

        # Si es operador lógico o comparación, el resultado es booleano
        result_type = 'bool' if op in ('==', '!=', '<', '>', '<=', '>=', '&&', '||') else left_type
        p[0] = (None, result_type)


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
            report_error(f"[SEMANTIC ERROR] Operación entre tipos incompatibles: {left_type} y {right_type}")
            p[0] = (None, "error")
        else:
            p[0] = (None, left_type)
    
def p_term_variable(p):
    'term : VARIABLE'
    var_name = p[1]
    if var_name not in symbol_table:
        report_error(f"[SEMANTIC ERROR] Variable '{var_name}' no declarada.")
        p[0] = (None, 'error')
    else:
        var_info = symbol_table[var_name]
        p[0] = (var_info.get('value', None), var_info['type'])


def p_factor(p):
    '''factor : NUMBER
              | FLOAT
              | STRING
              | VARIABLE
              | TRUE
              | FALSE
              | LPAREN expression RPAREN
              | make_expr
              | struct_instance
              | func_call'''
    if p.slice[1].type == 'NUMBER':
        p[0] = (p[1], 'int')
    elif p.slice[1].type == 'FLOAT':
        p[0] = (p[1], 'float64')
    elif p.slice[1].type == 'STRING':
        p[0] = (p[1], 'string')
    elif p.slice[1].type == 'TRUE':
        p[0] = (True, 'bool')
    elif p.slice[1].type == 'FALSE':
        p[0] = (False, 'bool')
    elif p.slice[1].type == 'VARIABLE':
        # Manejo variables, ver si declarada
        if p[1] in symbol_table:
            p[0] = (symbol_table[p[1]]['value'], symbol_table[p[1]]['type'])
        else:
            raise Exception(f"[SEMANTIC ERROR] Variable '{p[1]}' usada sin declarar.")
    elif p.slice[1].type == 'LPAREN':
        p[0] = p[2]

    

# Tipos básicos de Go
def p_type(p):
    '''type : INT_TYPE
            | FLOAT64_TYPE
            | STRING_TYPE
            | BOOL_TYPE'''
    p[0] = p[1]  # ← esto es lo que le da el valor real al tipo

# IF - ELSE
def p_if_stmt(p):
    '''if_stmt : IF expression block
               | IF expression block ELSE block'''
    
    condition_value, condition_type = p[2]

    if condition_type != 'bool':
        report_error(f"[SEMANTIC ERROR] Condición en 'if' debe ser de tipo 'bool', pero se recibió '{condition_type}'")

# FOR Loop (Go tiene varias formas, empezamos con la básica tipo while)
def p_for_stmt(p):
    '''for_stmt : FOR expression block
                | FOR assignment SEMICOLON expression SEMICOLON for_update block'''
    context_stack.append("loop") # Estamos dentro de un bucle for
    context_stack.pop() #
    pass

def p_continue_stmt(p):
    '''continue_stmt : CONTINUE'''
    if "loop" not in context_stack:
        report_error("[SEMANTIC ERROR] 'continue' fuera de un bucle.")
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

# Jared Gonzalez
# MAP
def p_map_declaration(p):
    '''map_declaration : VAR VARIABLE MAP LBRACKET type RBRACKET type
                       | VARIABLE ASIG MAP LBRACKET type RBRACKET type
                       | VARIABLE ASIG MAP LBRACKET type RBRACKET type LBRACE  map_params RBRACE'''
    pass

def p_map_params(p):
    '''map_params : map_param
                    | map_param COMMA map_params'''
    pass

def p_map_param(p):
    '''map_param : STRING COLON factor'''
    pass

# MAKE
def p_make_stmt(p):
    '''make_stmt : VARIABLE ASIG MAKE LPAREN MAP LBRACKET type RBRACKET type RPAREN
                 | VARIABLE ASIG MAKE LPAREN LBRACKET RBRACKET type RPAREN'''
    pass

def p_make_expr(p):
    '''make_expr : MAKE LPAREN MAP LBRACKET type RBRACKET type RPAREN
                 | MAKE LPAREN LBRACKET RBRACKET type RPAREN'''
    if len(p) == 9:
        key_type = p[5]
        value_type = p[7]
        p[0] = (None, f"map[{key_type}]{value_type}")
    elif len(p) == 7:
        slice_type = p[5]
        p[0] = (None, f"[] {slice_type}")

# MAP CON VALORES

def p_map_literal_declaration(p):
    '''map_declaration_values : VARIABLE ASIG MAP LBRACKET type RBRACKET type LBRACE map_kv_pairs RBRACE'''
    pass

def p_map_kv_pairs(p):
    '''map_kv_pairs : map_kv_pair
                    | map_kv_pair COMMA map_kv_pairs'''
    pass

def p_map_kv_pair(p):
    '''map_kv_pair : STRING COLON expression'''
    pass

# ARRAY
def p_array_declaration(p):
    '''array_declaration : VAR VARIABLE LBRACKET NUMBER RBRACKET type
                         | VAR VARIABLE ASSIGN array_literal'''

    if len(p) == 7:  # var numeros [3]int
        var_name = p[2]
        array_size = p[4]
        element_type = p[6]

        if var_name in symbol_table:
            report_error(f"[SEMANTIC ERROR] Variable '{var_name}' redeclarada.")
        else:
            symbol_table[var_name] = {'type': f'array[{array_size}]{element_type}', 'value': None}
            report_error(f"[INFO] Array '{var_name}' declarado con tipo y tamaño correctamente.")

    elif len(p) == 5:  # var numeros = [3]int{...}
        var_name = p[2]
        array_value, array_type = p[4]

        if var_name in symbol_table:
            report_error(f"[SEMANTIC ERROR] Variable '{var_name}' redeclarada.")
        else:
            symbol_table[var_name] = {'type': array_type, 'value': array_value}
            report_error(f"[INFO] Array '{var_name}' declarado e inicializado correctamente.")

def p_array_literal(p):
    '''array_literal : LBRACKET NUMBER RBRACKET type LBRACE array_values RBRACE'''
    array_size = p[2]
    element_type = p[4]
    values = p[6]

    if len(values) != array_size:
        report_error(f"[SEMANTIC ERROR] Se esperaban {array_size} elementos, pero se proporcionaron {len(values)}.")
    else:
        for i, (val, val_type) in enumerate(values):
            if val_type != element_type:
                report_error(f"[SEMANTIC ERROR] Elemento {i} debe ser de tipo '{element_type}', pero se recibió '{val_type}'.")

    p[0] = (values, f'array[{array_size}]{element_type}')


def p_array_values(p):
    '''array_values : expression
                    | expression COMMA array_values'''
    if len(p) == 2:
        # Solo un elemento
        p[0] = [p[1]]
    else:
        # Elemento + lista de elementos
        p[0] = [p[1]] + p[3]

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
    if "loop" not in context_stack:
        report_error("[SEMANTIC ERROR] 'break' fuera de un bucle.")
    pass

# Incrementadores ++ --
def p_increment_stmt(p):
    '''increment_stmt : VARIABLE INCREMENT
                      | VARIABLE DECREMENT'''
    pass

# Manejo de errores
def p_error(p):
    if p:
        report_error(f"[SYNTAX ERROR] Unexpected token '{p.value}' at line {p.lineno}")
    else:
        report_error("[SYNTAX ERROR] Unexpected end of input")





# Construir el parser
parser = yacc.yacc(start='start')


if __name__ == "__main__":
    try:
        with open("algorithms/algorithm3.go", "r", encoding="utf-8") as f:
            data = f.read()
        result = parser.parse(data)
        if result is None:
            logging.info("✅ Análisis semántico completado correctamente.")
            print(f"\n✅ Análisis semántico completado. Log guardado en: {ruta_log}")
    except Exception as e:
        logging.error(f"[ERROR GENERAL] {str(e)}")
        print(f"[ERROR] {str(e)}")

