package main

import (
	"fmt"
)

type Producto struct {
	Nombre  string
	Precio  float64
	Cantidad int
}

type Carrito struct {
	Items []Producto
}

func (c *Carrito) Agregar(p Producto) {
	c.Items = append(c.Items, p)
}

func (c *Carrito) Total() float64 {
	total := 0.0
	for _, item := range c.Items {
		total += item.Precio * float64(item.Cantidad)
	}
	return total
}

func main() {
	carrito := Carrito{}

	carrito.Agregar(Producto{"Manzanas", 0.5, 4})
	carrito.Agregar(Producto{"Pan", 1.25, 2})
	carrito.Agregar(Producto{"Leche", 0.9, 1})

	fmt.Println("Resumen del carrito:")
	for _, item := range carrito.Items {
		fmt.Printf("- %s x%d: $%.2f\n", item.Nombre, item.Cantidad, item.Precio)
	}

	fmt.Printf("Total a pagar: $%.2f\n", carrito.Total())
}
