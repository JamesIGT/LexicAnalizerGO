import ply.lex as lex
import ply.yacc as yacc
import lexer  
import parser  

# Crear lexer y parser
lexer = lex.lex(module=lexer)
parser = yacc.yacc(module=parser)

# Ejemplos de código en Go:
tests = [
    'var x int',
    'var y int := 5',
    'x = 3 + 4 * (2 - 1)',
    'if x > 5 { fmt.Println(x) }',
    'for i := 0; i < 10; i++ { fmt.Println(i) }',
    'var m map[string]int',
    'm = make(map[string]int)',
    'switch x { case 1: fmt.Println("uno") default: fmt.Println("otro") }',
    'var s []int = []int{1, 2, 3}',
    'type Persona struct { nombre string edad int }',
    'var p Persona = Persona{ nombre: "Juan", edad: 30 }',
    
]

# Ejecutar cada prueba
for idx, code in enumerate(tests):
    print(f"\n--- Test #{idx + 1} ---")
    try:
        result = parser.parse(code, lexer=lexer)
        print("✔️ Sintaxis válida")
    except Exception as e:
        print(f"❌ Error: {e}")
