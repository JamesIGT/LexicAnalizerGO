package main
import "fmt"

func obtenerDatos() map[string]int {
    datos := map[string]int {
        "edad": 25,
        "anio": 2025
    }
    return datos
}

func imprimirNumeros() {
    for i := 0; i < 10; i++ {
        if i == 3 {
            continue
        }
        if i == 7 {
            break
        }
        fmt.Println(i)
    }
}

func obtenerSaludo() string {
    return "hola"
}

func main() {

    //datos := obtenerDatos()
    fmt.Println("Datos:", datos)

    //saludo := obtenerSaludo()
    var saludo string = "Hola"
    fmt.Println(saludo)

    imprimirNumeros()
}
