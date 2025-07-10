package main

import "fmt"

// ✅ Función válida
func saludar(nombre string) string {
    return "Hola " + nombre
}

func main() {
    fmt.Println("Dentro de main")

    // ✅ Declaraciones válidas
	var m, n int = 1, 2
    var lenguaje, ok = "Go", true
    var _cantidad int = 10
    var ACTIVO bool = true
    var peso_normal float64 = 65.5   
    
    // ✅ Arrays válidos
    var edades = [3]int{20, 25, 30}
    var nombres = [3]string{"Ana", "Luis", "Pedro"}

    fmt.Println(edades)
    fmt.Println(nombres)

    // ✅ Asignación entre arrays del mismo tipo y tamaño
    var a = [2]int{1, 2}
    var b [2]int
    b = a

    // ✅ Estructura de control válida
    var edad int = 10
    if edad > 18 {
        fmt.Println("Eres mayor de edad")
    } else {
        fmt.Println("Eres menor de edad")
    }  

}

// -------------------------------
//  PRUEBAS DE ERRORES
// -------------------------------

// ❌ Función con tipo de retorno incorrecto
func pruebaEdad(numero int) string {
    return numero // ❌ Error semántico: retorna int, se espera string
}

func errores() {

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
}
