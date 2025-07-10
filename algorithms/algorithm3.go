package main
import "fmt"

func obtenerDatos() string {
    datos := map[string]int {
        "edad": 25,
        "anio": 2025
    }
    return "Datos obtenidos"
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
        break
    }
}

func obtenerSaludo() string {
    return 123
}

func main() {
    fmt.Println("Datos:", datos)
    var saludo string = "Hola"
    fmt.Println(saludo)
    imprimirNumeros()
}
