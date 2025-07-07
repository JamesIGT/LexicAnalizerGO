import tkinter as tk
from tkinter import scrolledtext, messagebox
import lexer
import parser  # Este es tu parser.py que ya importa el lexer

def analizar_codigo():
    codigo = input_area.get("1.0", tk.END)

    output_area.delete("1.0", tk.END)

    try:
        # Reiniciar tablas para nuevo análisis
        parser.symbol_table.clear()
        parser.function_table.clear()
        parser.context_stack.clear()

        result = parser.parser.parse(codigo, lexer=lexer.lexer)

        output_area.insert(tk.END, "✅ Análisis completado correctamente.\n")

    except Exception as e:
        output_area.insert(tk.END, f"[ERROR] {str(e)}\n")
        messagebox.showerror("Error", str(e))

# === GUI ===

root = tk.Tk()
root.title("Analizador Go - Jared G.")
root.geometry("900x500")
root.configure(bg="#f4f4f4")

# Título
tk.Label(root, text="Analizador Go", font=("Segoe UI", 16, "bold"), bg="#2563eb", fg="white").pack(fill=tk.X)

frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Entrada de código
input_area = scrolledtext.ScrolledText(frame, width=50, font=("Consolas", 11))
input_area.insert(tk.END, "// Escribe tu código Go aquí\n")
input_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Botón Run en el medio
button_frame = tk.Frame(frame, bg="#f4f4f4")
button_frame.pack(side=tk.LEFT, padx=10)
run_button = tk.Button(button_frame, text="▶️\nRun", command=analizar_codigo,
                       font=("Segoe UI", 12), bg="#22c55e", fg="white", width=5, height=2)
run_button.pack()

# Área de salida
output_area = scrolledtext.ScrolledText(frame, width=50, font=("Consolas", 11), bg="#1e1e2e", fg="#ffffff")
output_area.insert(tk.END, "Resultado o errores...\n")
output_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()
