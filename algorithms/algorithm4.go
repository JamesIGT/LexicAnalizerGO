package main

import "fmt"

// -------------------------------
// ✅ Declaraciones válidas
// -------------------------------
var _edad int = 10
var activo bool = true
var peso float64 = 65.5

// ✅ Variable con nombre válido, aunque poco recomendable
var iF float64 = 70.0

// -------------------------------
// ✅ Función válida
// -------------------------------
func saludar(nombre string) string {
    return "Hola " + nombre
}

// -------------------------------
// ✅ Función principal válida
// -------------------------------
func main() {
    fmt.Println("Dentro de main")

    // ✅ Declaraciones combinadas
    var name, age = "Ana", 30
    var count int
    var _peso float64 = 65.5

    // ✅ Arrays válidos
    var edades = [3]int{20, 25, 30}
    var nombres = [3]string{"Ana", "Luis", "Pedro"}

    fmt.Println(edades)
    fmt.Println(nombres)

    // ✅ Asignación entre arrays del mismo tipo y tamaño
    var a = [2]int{1, 2}
    var b [2]int
    b = a

    // ✅ Llamada válida
    saludo := saludar("Juan")
    fmt.Println(saludo)

    // ✅ Estructura de control válida
    if edad > 18 {
        fmt.Println("Eres mayor de edad")
    } else {
        fmt.Println("Eres menor de edad")
    }
}

// -------------------------------
// ❌ Declaraciones inválidas
// -------------------------------
// var 1peso float64 = 70.0       // ❌ Error léxico: no puede comenzar con número
// var if float64 = 70.0          // ❌ Error léxico: palabra reservada

// -------------------------------
// ❌ Función con tipo de retorno incorrecto
// -------------------------------
func pruebaEdad(edad int) string {
    return edad // ❌ Error semántico: retorna int, se espera string
}

func errores() {
    // ❌ Llamada con tipo incompatible
    pruebaEdad(12)

    // ❌ Array con demasiados elementos
    var numerosarray = [2]int{10, 20, 30}

    // ❌ Array con tipos incompatibles
    var mezclado = [2]int{10, "hola"}

    // ❌ Asignación entre arrays de distinto tamaño
    var x = [2]int{1, 2}
    var y [3]int
    y = x

    // ❌ Operaciones inválidas
    var suma int = 3 + "texto"        // tipos incompatibles
    var edadTexto int = "veinticinco" // string a int directo
    var resultado float64 = 5.0 / 2   // Ambiguo si se espera float / int

    // ❌ Estructura de control con error de sintaxis
    // if (edad > 18                 // ❌ falta paréntesis o llave de apertura
    //     fmt.Println("Mayor")     // ❌ error de bloque
    // else
    //     fmt.Println("Menor")     // ❌ else sin bloque
}
