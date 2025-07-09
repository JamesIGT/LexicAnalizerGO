package main

import "fmt"

// Función que retorna un tipo incorrecto (debería retornar string, pero retorna int)
func pruebaEdad(edad int) string {
    return edad  // ❌ Error esperado: se retorna int, pero se espera string
}

func saludar(nombre string) string {
 return "Hola " + nombre
}

// Función principal sin parámetros
func mains() {
    // Llamada correcta en cantidad de argumentos
    pruebaEdad(12)

    // Llamada a función sin parámetros
    // mensaje := saludar("HOLA")  // ❌ Error esperado si 'saludar' no está declarada
    // fmt.Println(mensaje)

    // Declaración de arrays válidos
    
    var pesso float64 = 65.5
    var activo bool = true
    var edades = [3]int{20, 25, 30}  // falta que funcione con :=

    fmt.Println(edades)

    var nombres = [3]string{"Ana", "Luis", "Pedro"}

    // ❌ Array con más valores que el tamaño
    var numerosarray = [2]int{10, 20, 30}

    // ❌ Array con tipos incompatibles
    var mezclado = [2]int{10, "hola"}   //falta corregir la compatibilidad

    // Asignación entre arrays válidos
    var a = [2]int{1, 2}
    var b [2]int
    b = a

    // ❌ Asignación entre arrays de distinto tamaño
    var x = [2]int{1, 2}
    var y [3]int
    y = x

    // Tipos válidos
    var nombre string = "Ana"
    var cantidad int = 2

    // ❌ Errores de tipo
    var suma int = 3 + "texto"
    var edad int = "veinticinco"
    var resultado float64 = 5.0 / 2
}
