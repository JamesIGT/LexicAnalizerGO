package main
// Diego Alay
import "fmt"

// Función que saluda a una persona
// func pruebaEdad(edad int) int {
//     return edad  // ← Error semántico esperado: se retorna int, pero se espera string
// }


//func mains(){
    
    
    //Declaración con tipo explícito y asignación posterior
    // var temperaturas [2]float64
    // temperaturas[0] = 22.5
    // temperaturas[1] = 18.9


    //Acceso y uso en expresión
    //var notas = [3]int{80, 90, 100}
    //var suma = notas[0] + notas[1] + notas[2]

//   }

//Llamado a la función
mensaje := saludar( )
fmt.Println(mensaje)

   
// //}


// pruebas que funcionan     
    var numeros [3]int
    var edades = [3]int{20, 25, 30}
    fmt.Println(edades)
    var nombres = [3]string{"Ana", "Luis", "Pedro"}
    // error 
    var numerosarray = [2]int{10, 20, 30}  // ❌ Error esperado: se esperaban 2, se dieron 3
    var mezclado = [2]int{10, "hola"}  // ❌ Error: "hola" no es int

    //Asignación entre arrays del mismo tipo
    var a = [2]int{1, 2}
    var b [2]int
    b = a 

    //Asignación entre arrays de distinto tipo
    var x = [2]int{1, 2}
    var y [3]int
    y = x  // ❌ Error esperado: tipos incompatibles (array[3]int ≠ array[2]int)

    //Verificación de tipos válidos
    var nombre string = "Ana"
    var cantidad int = 2

    //Ejemplos con errores de tipos (incompatibles)
    var suma int = 3 + "texto"         // Error: int + string
    var edad int = "veinticinco"       // Error: string asignado a int
    var resultado float64 = 5.0 / 2    // Error: float64 / int