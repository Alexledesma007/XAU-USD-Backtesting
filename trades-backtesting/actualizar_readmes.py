import os
import glob

# Ruta base donde están las carpetas de trades (ajusta según sea necesario)
base_path = '.'  # Usa el directorio actual, o puedes especificar como 'ruta/a/tus/trades'

# Patrón para encontrar todos los archivos README.md dentro de las carpetas Trade_*
readme_files = glob.glob(os.path.join(base_path, 'Trade_*/README.md'))

# Texto a buscar y reemplazar
old_text = "Nasdaq 100 (NQ)"
new_text = "XAU/USD"

# Contador para registrar cambios
updated_count = 0

for file_path in readme_files:
    try:
        # Leer el contenido actual del archivo
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Realizar el reemplazo si se encuentra el texto antiguo
        if old_text in content:
            new_content = content.replace(old_text, new_text)
            
            # Guardar los cambios
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            
            print(f"Actualizado: {file_path}")
            updated_count += 1
        else:
            print(f"Sin cambios: {file_path} (texto no encontrado)")
    
    except Exception as e:
        print(f"Error procesando {file_path}: {str(e)}")

print(f"\nProceso completado. Archivos actualizados: {updated_count}/{len(readme_files)}")