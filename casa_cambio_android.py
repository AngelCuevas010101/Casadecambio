# Instalar PyInstaller primero: pip install pyinstaller

# Comando para crear ejecutable:
# pyinstaller --onefile --windowed --name="CasaDeCambio" --icon=icon.ico main.py

# O usa este script:
import subprocess
import sys
import os

def crear_ejecutable():
    print("🚀 Creando ejecutable de Casa de Cambio...")
    
    # Comando PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",           # Un solo archivo
        "--windowed",          # Sin consola
        "--name=CasaDeCambio", # Nombre del ejecutable
        "--clean",             # Limpiar archivos temporales
        "main.py"
    ]
    
    try:
        # Ejecutar PyInstaller
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Ejecutable creado exitosamente!")
            print("📁 Encuentra tu ejecutable en la carpeta 'dist/'")
        else:
            print("❌ Error al crear ejecutable:")
            print(result.stderr)
            
    except FileNotFoundError:
        print("❌ PyInstaller no está instalado.")
        print("Instálalo con: pip install pyinstaller")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Verificar que existe main.py
    if not os.path.exists("main.py"):
        print("❌ No se encuentra main.py en el directorio actual")
        sys.exit(1)
    
    crear_ejecutable()