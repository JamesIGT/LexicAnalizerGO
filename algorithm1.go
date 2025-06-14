package main
import (
 "fmt"
 "strings"
)
func contarVocales(texto string) int {
 texto = strings.ToLower(texto)
 contador := 0
 for _, letra := range texto {
 if strings.ContainsRune("aeiou", letra) {
 contador++
 }
 }
 return contador
}
func main() {
 cadena := "Hola Mundo"
 fmt.Printf("La cadena '%s' tiene %d vocales\n", cadena, contarVocales(cadena))
}
