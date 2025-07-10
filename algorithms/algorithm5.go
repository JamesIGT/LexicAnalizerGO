package main 
import "fmt"

type Persona struct {
  Nombre string Edad	int
}
func calcularPromedio(personas []Persona) float64 { 
  var suma int
  for _, p := range personas { suma += p.Edad
  }
  return float64(suma) / float64(len(personas))
}

func main() {
  grupo := []Persona{
    {"Ana", 25},
    {"Luis", 30},
    {"Carlos", 35},
  }
  
  promedio := calcularPromedio(grupo)
  fmt.Printf("El promedio de edades es: %.2f\n", promedio)
}
