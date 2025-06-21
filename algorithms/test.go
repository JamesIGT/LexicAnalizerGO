package main

import (
	"fmt"
)

// 1. Definición de clase con propiedades y métodos (struct + método)
type Persona struct {
	Nombre string
	Edad   int
}

func (p Persona) Saludar() {
	fmt.Println("Hola, mi nombre es", p.Nombre)
}

// 2. Definición de función
func saludar(nombre string) string {
	return "Hola, " + nombre
}

func main() {
	// 3. Impresión
	fmt.Println("=== Inicio del Programa ===")

	// 4. Ingreso de datos por teclado
	var nombreUsuario string
	fmt.Print("Ingresa tu nombre: ")
	fmt.Scanln(&nombreUsuario)
	fmt.Println("Hola,", nombreUsuario)

	// 5. Expresiones aritméticas
	a := 10
	b := 3
	resultadoArit := a + b*2 - a/2
	fmt.Println("Resultado de expresión aritmética:", resultadoArit)

	// 6. Condiciones con conectores lógicos
	edad := 25
	tieneLicencia := true

	if edad >= 18 && tieneLicencia {
		fmt.Println("Puedes conducir")
	} else {
		fmt.Println("No puedes conducir")
	}

	// 7. Asignación de variables con distintos tipos
	var edadVar int = 30
	var nombreVar string = "Juan"
	var altura float64 = 1.75
	var activo bool = true
	var resultadoCond int

	if edadVar > 18 {
		resultadoCond = edadVar * 2
	} else {
		resultadoCond = edadVar + 10
	}
	fmt.Println("Variables:", nombreVar, edadVar, altura, activo, resultadoCond)

	// 8. Estructuras de datos
	numeros := []int{1, 2, 3}
	personaMap := map[string]string{
		"nombre": "Ana",
		"edad":   "22",
	}
	fmt.Println("Slice:", numeros)
	fmt.Println("Mapa:", personaMap)

	// 9. Estructuras de control (for + if)
	for i := 0; i < 5; i++ {
		if i%2 == 0 {
			fmt.Println(i, "es par")
		} else {
			fmt.Println(i, "es impar")
		}
	}

	// 10. Uso de función
	mensaje := saludar("Carlos")
	fmt.Println(mensaje)

	// 11. Uso de clase/struct con método
	p := Persona{Nombre: "Lucía", Edad: 28}
	p.Saludar()

	fmt.Println("=== Fin del Programa ===")
}
