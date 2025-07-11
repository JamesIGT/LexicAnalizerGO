package main

import "fmt"

// Definir el struct
type Persona struct {
	edad int
}


//✅ VALIDO 

func operar() {
    x := 5      // int
    y := 3    // int
    result := x + y 
    fmt.Println("Resultado válido:", result)
}

func main() {
    operar()  // Esto imprimirá Resultado válido
}


//❌INVALIDO
package main

import "fmt"

func operar() {
    x := "Hello"  // string
    y := 5        // int
    result := x + y // Error: no se puede sumar un string con un int
    fmt.Println("Resultado con error:", result)
}

func main() {
    operar()  // Esto generará un error semántico en tiempo de compilación
}



// ✅ VALIDACION Función para realizar operaciones y conversión de tipos
func operar() {
    x := 5       // int
    y := 3.2     // float64

    // Convertir implícitamente el int a float64 para realizar la operación
    result := float64(x) + y  // Conversión explícita de int a float64

    fmt.Println("Resultado con conversión explícita:", result)
}

func main() {
    operar()  // Esto generará la salida con la conversión explícita de tipos
}

//❌// Función para realizar operaciones con tipos incompatibles
func operar() {
    x := "Hello"  // string
    y := 5        // int

    // Intentar sumar un string con un int (esto dará un error)
    result := x + y  // Error: no se puede sumar un string con un int

    fmt.Println("Resultado con error:", result)
}

func main() {
    operar()  // Esto generará un error semántico en tiempo de compilación
}


//✅VALIDACION DE SWITCH
func main() {
    // Crear una instancia de Persona
    p := Persona{edad: 25}

    // Usar un switch con la edad
    switch p.edad {
    case 25:
        fmt.Println("Edad es 25")
    case 30:
        fmt.Println("Edad es 30")
    default:
        fmt.Println("Edad no coincidente")
    }
}

