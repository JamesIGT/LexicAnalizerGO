package main

import (
	"fmt"
	"strings"
	"unicode"
)

// Esta función cuenta vocales, consonantes y dígitos en un texto.
func analizarTexto(texto string) (int, int, int) {
	texto = strings.ToLower(texto)
	vocales, consonantes, digitos := 0, 0, 0

	for _, char := range texto {
		switch {
		case strings.ContainsRune("aeiou", char):
			vocales++
		case unicode.IsLetter(char):
			consonantes++
		case unicode.IsDigit(char):
			digitos++
		}
	}
	return vocales, consonantes, digitos
}

// Esta función verifica si una palabra es palíndromo.
func esPalindromo(palabra string) bool {
	limpia := strings.ToLower(strings.ReplaceAll(palabra, " ", ""))
	runes := []rune(limpia)
	n := len(runes)
	for i := 0; i < n/2; i++ {
		if runes[i] != runes[n-1-i] {
			return false
		}
	}
	return true
}

func main() {
	textos := []string{"Hola Mundo", "Anita lava la tina", "1234abcdEFG"}

	for _, texto := range textos {
		v, c, d := analizarTexto(texto)
		fmt.Printf("Texto: \"%s\"\n", texto)
		fmt.Printf("Vocales: %d, Consonantes: %d, Dígitos: %d\n", v, c, d)

		if esPalindromo(texto) {
			fmt.Println("=> Es un palíndromo.")
		} else {
			fmt.Println("=> No es un palíndromo.")
		}
		fmt.Println("---------------")
	}
}
