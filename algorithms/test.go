package main

import "fmt"

// Declaraciones válidas
var edad int = 10
var activo bool = true
var peso float64 = 65.5

// Imprimir mensajes
fmt.Println("Hola mundo")
fmt.Printf("Edad: %d\n", edad)

// ❌ Error: 'return' devuelve tipo incorrecto (debería ser string)
func pruebaEdad(edad int) string {
    return edad
}

// ✅ Función que retorna un string
func saludar(nombre string) string {
    return "Hola " + nombre
}

// ❌ Nombre de función incorrecto ('mains' en lugar de 'main')
func mains() {
    // ❌ Error: llamada correcta en número de argumentos, pero tipo devuelto no coincide
    pruebaEdad(12)

    // ✅ Llamada correcta
    mensaje := saludar("Go")
    fmt.Println(mensaje)

    // Declaraciones combinadas
    name, age := "Ana", 30
    var count int
    var _peso float64 = 65.5
    var iF float64 = 70.0  // Palabra clave como nombre (válido pero no recomendable)
    // var 1peso float64 = 70.0 // ❌ Error léxico: variable no puede comenzar con número

    var edades = [3]int{20, 25, 30}
    fmt.Println(edades)

    // ✅ Array con tipos válidos
    var nombres = [3]string{"Ana", "Luis", "Pedro"}

    // ❌ Array con más valores de los permitidos
    var numerosarray = [2]int{10, 20, 30}

    // ❌ Array con tipos incompatibles
    var mezclado = [2]int{10, "hola"}

    // ✅ Asignación entre arrays del mismo tipo
    var a = [2]int{1, 2}
    var b [2]int
    b = a

    // ❌ Asignación entre arrays de diferente tamaño
    var x = [2]int{1, 2}
    var y [3]int
    y = x

    // ✅ Tipos compatibles
    var nombre string = "Ana"
    var cantidad int = 2

    // ❌ Operaciones con tipos incompatibles
    var suma int = 3 + "texto"
    var edadTexto int = "veinticinco"
    var resultado float64 = 5.0 / 2  // ← ¿tu compilador permite dividir float entre int?
}
