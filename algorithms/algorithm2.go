package main

import "fmt"

func main() {
    var nombre string = "Valeria"
    edad := 22
    acceso := true
    dia := 2 // número del día elegido  (1, 2 o 3)

    if edad >= 18 {
        acceso = true
    }

    fmt.Println("Nombre:", nombre)
    fmt.Println("Edad:", edad)

    if acceso {
        fmt.Println("Acceso permitido ✅")
        fmt.Println("Día seleccionado:", dia)

        switch dia {
        case 1:
            fmt.Println("Actividad: Consulta médica")
        case 2:
            fmt.Println("Actividad: Taller de bienestar")
        case 3:
            fmt.Println("Actividad: Atención al cliente")
        default:
            fmt.Println("Día no válido")
        }

    } else {
        fmt.Println("Acceso denegado ❌. Solo mayores de edad pueden seleccionar un día.")
    }
}
