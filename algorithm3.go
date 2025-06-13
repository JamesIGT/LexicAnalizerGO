package main
import (
	"fmt"
)
type Tarea struct {
	Descripcion string
	Completada  bool
}
type GestorDeTareas struct {
	Lista []Tarea
}

func (g *GestorDeTareas) Agregar(descripcion string) {
	t := Tarea{Descripcion: descripcion, Completada: false}
	g.Lista = append(g.Lista, t)
}
func (g *GestorDeTareas) Completar(indice int) {
        if indice >= 0 && indice < len(g.Lista) {
		g.Lista[indice].Completada = true
	}
}
func (g *GestorDeTareas) Mostrar() {
	for i, t := range g.Lista {
		estado := "✗"
		if t.Completada {
			estado = "✓"
		}
		fmt.Printf("%d. [%s] %s\n", i, estado, t.Descripcion)
	}
}
// Esto es un comentario

func main() {
	gestor := GestorDeTareas{}
	gestor.Agregar("Estudiar Go")
	gestor.Agregar("Hacer ejercicio")
	gestor.Agregar("Leer un libro")
	gestor.Completar(1)
	fmt.Println("Lista de tareas:")
	gestor.Mostrar()
}
