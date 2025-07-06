package main

func iniciar() {
fmt.Println("Iniciando programa...")
}
m := map[string]int{"uno": 1, "dos": 2}

var resultado float64 = 5.0 / 2     // Este lo detecta si implementas bien los FLOAT
var suma = 3 + "texto"              // Ya detectas error de tipos
var edad int = "veinticinco"        // Detectas error

// type Persona struct {
// 	Nombre string
// 	Edad   int
// }

// func (p Persona) Saludar() string {
// 	return "Hola " + p.Nombre
// }

// func main() {
// 	Declaraciones
// 	var edad int
// 	edad = 25

// 	var altura float64 = 1.75
// 	nombre := "Luis"
// 	activa := true

// 	Array y Slice
// 	var numeros [3]int
// 	numeros = [3]int{1, 2, 3}

// 	lista := []string{"Go", "Python", "Java"}

// 	Map
// 	edades := make(map[string]int)
// 	edades["Juan"] = 30
// 	edades["Ana"] = 25

// 	Struct e instancia
// 	p1 := Persona{"Carlos", 40}
// 	fmt.Println(p1.Saludar())

// 	Entrada/Salida
// 	fmt.Print("Ingresa tu nombre: ")
// 	var input string
// 	fmt.Scanln(&input)

// 	Condicional
// 	if edad > 18 {
// 		fmt.Println("Mayor de edad")
// 	} else {
// 		fmt.Println("Menor de edad")
// 	}

// 	Switch
// 	dia := "lunes"
// 	switch dia {
// 	case "lunes":
// 		fmt.Println("Inicio de semana")
// 	case "viernes":
// 		fmt.Println("Fin de semana")
// 	default:
// 		fmt.Println("Día normal")
// 	}

// 	Bucle For clásico
// 	for i := 0; i < 3; i++ {
// 		fmt.Println(i)
// 	}

// 	For tipo while
// 	j := 0
// 	for j < 3 {
// 		fmt.Println(j)
// 		j++
// 	}

// 	Incrementadores
// 	k := 0
// 	k++
// 	k--
// }
