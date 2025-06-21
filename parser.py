import ply.yacc as yacc
from lexer import tokens, reserved # Importa tus tokens desde lexer.py
import os
import logging
from datetime import datetime

usuario_git = "jamesigt"  # Cambia esto por tu usuario de GitHub
os.makedirs("logs", exist_ok=True)
now = datetime.now()
nombre_log = f"sintactico-{usuario_git}-{now.day:02d}-{now.month:02d}-{now.year}-{now.hour:02d}h{now.minute:02d}.txt"
ruta_log = os.path.join("logs", nombre_log)

logging.basicConfig(
    filename=ruta_log,
    filemode='w',
    format='%(message)s',
    level=logging.INFO,
    encoding='utf-8'
)

# === REGLAS SINTÁCTICAS ===

if __name__ == "__main__":
    try:
        with open("algorithms/algorithm2.go", "r", encoding="utf-8") as f:
            data = f.read()
        result = parser.parse(data)
        if result is None:
            logging.info("✅ Análisis sintáctico completado correctamente.")
            print(f"\n✅ Análisis sintáctico completado. Log guardado en: {ruta_log}")
    except Exception as e:
        logging.error(f"[ERROR GENERAL] {str(e)}")
        print(f"[ERROR] {str(e)}")
