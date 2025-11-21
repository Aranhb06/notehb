"""
file logic internal 
"""

""" ------------ MODULOS ------------"""
import os
import json
import time

""" ------------ FUNCIONES GLOBALES ------------"""
# --- Funcion de configuracion inicial ---
def initial_config(config_dir, config_file, file_dir, file):
    
    # 2. LOGICA PRINCIPAL: Si el archivo de configuración ya existe, no hacemos nada.
    if os.path.exists(config_file):
        return  # Sale de la función inmediatamente

    # Variables de datos
    test_task_list = [{'name': 'test', 'description': 'test', 'date': '01/01/3000', 'status': False}]
    config = {
        'config_dir': config_dir,
        'config_file': config_file,
        'file_dir': file_dir,
        'default_list': file 
    } 

    # - Comprobar y crear el directorio base y subdirectorio
    try:
        os.makedirs(file_dir, exist_ok=True) 
        print(f"Directorio '{file_dir}' asegurado.")
    except OSError as e:
        print(f"Error al crear los directorios de configuración: {e}")
        return

    # - Crear el archivo default.json (Lista de tareas por defecto)
    if not os.path.exists(file):
        try:
            with open(file, 'w', encoding="utf-8") as fileconf:
                json.dump(test_task_list, fileconf, indent=4)
            print(f"Archivo de lista por defecto creado en: '{file}'")
        except IOError as e:
            print(f"Error al crear el archivo default.json: {e}")

    # - Crear el archivo config.json (Este es el que marca que ya se inició)
    try:
        with open(config_file, 'w', encoding="utf-8") as fileconf:
            json.dump(config, fileconf, indent=4)
        print(f"Archivo de configuración creado correctamente en: '{config_file}'")
    except IOError as e:
        print(f"Error al crear el archivo config.json: {e}")

# --- Funcion rutas relativas ---
def path_relative(file):
    file = os.path.expanduser(file)
    return file

# --- Funcion leer archivos ---
def files_read(file):
    # Varaibles
    data = []
    # Verificamos archivo
    if os.path.exists(file):

        # Leemos el archivo
        try:
            # Especificar 'r' y encoding="utf-8" para consistencia
            with open(file, 'r', encoding="utf-8") as file_data: 
                data = json.load(file_data)
        # Manejo de errores (Funcion file_data)
        except json.JSONDecodeError:
            print(f"Error: El archivo '{file}' no contiene un formato JSON válido.")
            
        except IOError as e:
            print(f"Error de E/S al leer archivo '{file}': {e}")
        except Exception as e:
             print(f"Error inesperado al leer archivo '{file}': {e}")
    return data

# --- Funcion escribir archivo ---
def files_save(file, data):
    try:
        with open(file, 'w', encoding="utf-8") as file_list:
            json.dump(data, file_list, indent=4) 
    except IOError as e:
        print(f"Error al escribir el archivo {file}: {e}")
    except Exception as e:
         print(f"Error inesperado al guardar archivo '{file}': {e}")


# --- Funcion mostrar tarea ---
def list_task_view(data):
    print('--- TAREAS ---')
    # 'data' en el bucle es el diccionario de la tarea individual
    for index,task in enumerate(data): 
        print(f"{index} - {task['name']}")
        
# --- Funcion añadir tareas ---
def add_task(file, list_task, data):
    # 1. Validar que la entrada 'data' no esté vacía
    if not data or not data.strip():
        print("Error: No se ha proporcionado un nombre para la tarea.")
        return

    # 2. Dividir la cadena 'data' en una lista de "partes"
    parts = data.split()
    num_parts = len(parts)
    
    # 3. Asignar las variables según el número de partes
    name = parts[0]
    description = ''
    date = ''

    if num_parts == 2:
        # Si hay dos partes, asumimos que es nombre y descripción/fecha
        description = parts[1]
    elif num_parts >= 3:
        # Si hay tres o más, el primero es el nombre, el último es la fecha
        # y todo lo del medio es la descripción.
        description = ' '.join(parts[1:-1])
        date = parts[-1]

    # 4. Crear el diccionario para la nueva tarea
    new_task = {
        'name': name,
        'description': description,
        'date': date,
        'status': False  # Añadir como no completada por defecto
    }
    
    # 5. Añadir la tarea a la 'list_task' y guardar en 'file'
    list_task.append(new_task)
    files_save(file, list_task)
    
    print(f"Tarea '{name}' añadida correctamente.")
