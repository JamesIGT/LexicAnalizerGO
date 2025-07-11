package main

import (
	"fmt"
	"strconv"
)

/* ---------- Struct ---------- */
type Persona struct {
	nombre string
	edad   int
}

/* ---------- Función con múltiples retornos ---------- */
func dividir(dividendo, divisor int) (int, int) {
	cociente := dividendo / divisor
	resto    := dividendo % divisor
	return cociente, resto
}

func main() int {

	/* -----------------------------------
	   1. Conversiones explícitas correctas
	   ----------------------------------- */
	var numero int     = int(3.14)        // ✅ float64 → int (trunca a 3)
	//var texto  string  = strconv.Itoa(42) // ✅ int → string  ("42")

	/* -----------------------------------
	   2. Conversión implícita (debe fallar)
	   ----------------------------------- */
	// var falla int = 3.14      // ❌ ERROR: asignación implícita float64 → int

	/* -----------------------------------
	   3. Operaciones mixtas
	   ----------------------------------- */
	var resultado = float64(5) + 2.5 // ✅ 5 → 5.0, tipos compatibles (float64)
	// var suma      = 5 + 2.5        // ❌ ERROR: mezcla int + float64 sin conversión

	/* -----------------------------------
	   4. Uso de la función con múltiples retornos
	   ----------------------------------- */
	coc, res := dividir(17, 5) // coc=3, res=2

	/* -----------------------------------
	   5. Instancia de struct
	   ----------------------------------- */
	var p = Persona{nombre: "Valeria", edad: 30}

	/* -----------------------------------
	   Salida para ver en ejecución real
	   (tu analizador solo necesita parsear)
	   ----------------------------------- */
	fmt.Println("numero:", numero)
	fmt.Println("texto :", texto)
	fmt.Println("resultado (5.0+2.5):", resultado)
	fmt.Println("división 17/5 →", coc, "resto", res)
	fmt.Println("Persona:", p)

	return 0
}