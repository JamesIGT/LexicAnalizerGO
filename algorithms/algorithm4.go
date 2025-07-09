package main

import "fmt"

// ✅ Función correcta que recibe un string y devuelve un string
func saludar(nombre string) string {
    return "Hola " + nombre
}

// ✅ Función principal correcta
func main() {
    // ✅ Llamada a la función con argumento de tipo string
    var mensaje string = saludar("Go")
    
    // ✅ Mostrar resultado
    fmt.Println(mensaje)
}
