package main

import (
	"fmt"
)

test_cases = [
 
    "var x int",
    "var y float64 := 3.14",
    
 
    "x = 10",
    "y := 5.5",
    

    fmt.Println(x)
    fmt.Printf("Valor: ", y)
    


    func suma(a int, b int) int {
        var resultado int
        resultado = a + b
        return resultado
    }
    

    "suma(3, 4)"
]

Recorrer los casos de prueba
for i, code in enumerate(test_cases, 1):
    print(f"\nTest {i}: {code}")
    result = parser.parse(code, lexer=lexer)
    print("Parse OK")