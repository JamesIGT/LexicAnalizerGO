# Analizador Sintáctico y Semántico para Go

Este proyecto es un analizador sintáctico y semántico para código fuente en lenguaje Go, desarrollado en Python usando la biblioteca PLY (Python Lex-Yacc) para el análisis léxico y sintáctico, y una interfaz gráfica con Tkinter para facilitar la prueba y visualización de errores.
Características

## Análisis sintáctico y semántico de código Go, incluyendo:

- Declaración y uso de variables, arrays, slices, mapas y structs.

  - Verificación de tipos en asignaciones y expresiones.
  - Soporte para funciones, métodos, y control de flujo (if, for, switch).
  - Validación de retorno de funciones según tipo declarado.

- Interfaz gráfica sencilla para ingresar código, ejecutar el análisis y mostrar resultados o errores.
- Registro detallado de errores semánticos y sintácticos en consola y GUI.

# Requisitos

Para ejecutar y probar el proyecto necesitas tener instalado:
- Python 3.8+
- PLY (Python Lex-Yacc)
- Tkinter (viene preinstalado en la mayoría de distribuciones Python)
- Pillow (para mostrar imagenes en la GUI, opcional)

# Instalación de dependencias

Para instalar las librerías necesarias usa pip:
```
pip install ply
pip install pillow
```

- Nota: Tkinter generalmente viene instalado con Python.
- En Debian/Ubuntu puedes instalarlo con:
```
   sudo apt install python3-tk
```

# Archivos principales

- lexer.py: Define el lexer con tokens para Go.

- parser.py: Define el parser con reglas gramaticales y análisis semántico.

- gui.py: Interfaz gráfica para ingresar código y mostrar resultados.

# Uso

Ejecuta la interfaz gráfica con:
```
python gui.py
```

- Escribe o pega código Go en el área de entrada.

- Haz clic en Run para analizar el código.

- Los errores o el resultado del análisis aparecerán en el área de salida.

# Notas
- El proyecto está pensado como una herramienta educativa para entender análisis sintáctico y semántico.
- La implementación actual no ejecuta código Go, solo lo analiza y valida.

