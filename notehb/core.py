"""
file logic internal 
"""

""" ------------ MODULOS ------------"""
import os
import json
import time

""" ------------ FUNCIONES GLOBALES ------------"""
# --- Funcion de configuracion inicial ---
def initial_config():
    # 1. Definir las rutas clave primero
    config_base_dir = os.path.expanduser('~/.config/notehb')
    default_config_file_path = os.path.join(config_base_dir, '.config.json')

    # 2. LOGICA PRINCIPAL: Si el archivo de configuración ya existe, no hacemos nada.
    if os.path.exists(default_config_file_path):
        return  # Sale de la función inmediatamente

    # ---------------------------------------------------------
    # Si llegamos aquí, es porque el archivo NO existe.
    # Ejecutamos todo el proceso de creación.
    # ---------------------------------------------------------

    # Definir el resto de ruta
    hb_list_dir = os.path.join(config_base_dir, 'hb_list')
    default_list_file_path = os.path.join(hb_list_dir, 'default.json')

    # Variables de datos
    test_task_list = [{'name': 'test', 'description': 'test', 'date': '01/01/3000', 'status': False}]

    config = {
        'config_dir': config_base_dir,
        'file': default_list_file_path
    } 

    # - Comprobar y crear el directorio base y subdirectorio
    try:
        os.makedirs(hb_list_dir, exist_ok=True) 
    except OSError as e:
        print(f"Error al crear los directorios de configuración: {e}")
        return

    # - Crear el archivo default.json (Lista de tareas por defecto
    if not os.path.exists(default_list_file_path):
        try:
            with open(default_list_file_path, 'w', encoding="utf-8") as fileconf:
                json.dump(test_task_list, fileconf, indent=4)
        except IOError as e:
            print(f"Error al crear el archivo default.json: {e}")

    # - Crear el archivo config.json (Este es el que marca que ya se inició)
    # Nota: No hace falta verificar if exists aquí porque ya lo hicimos al principio de la función.
    try:
        with open(default_config_file_path, 'w', encoding="utf-8") as fileconf:
            json.dump(config, fileconf, indent=4)
        print("Configuración inicial creada correctamente.")
    except IOError as e:
        print(f"Error al crear el archivo config.json: {e}")   

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

# --- Funcion escribir archivo listas ---
def files_save(file, data):
    # NOTA: No es necesario verificar si el archivo existe si la intención es crearlo o sobrescribirlo.
    # Si la intención es solo *actualizar* un archivo existente, la verificación es correcta.
    if os.path.exists(file):

        # Escribimos el archivo
        try:
            with open(file, 'w', encoding="utf-8") as file_list:
                # ERROR CORREGIDO: Los argumentos de json.dump estaban invertidos.
                # Debe ser (obj, fp), es decir: (data, file_list)
                json.dump(data, file_list, indent=4) 
        except IOError as e:
            print(f"Error al escribir el archivo {file}: {e}")
        except Exception as e:
             print(f"Error inesperado al guardar archivo '{file}': {e}")
    else:
        print(f"Advertencia: El archivo '{file}' no existe. No se guardó la información.")


# --- Funcion mostrar tarea ---
def list_task(data):
    print('--- TAREAS ---')
    # 'data' en el bucle es el diccionario de la tarea individual
    for index, task in enumerate(data): 
        # ERROR CORREGIDO: Se intentaba acceder a la clave 'name' con una variable 'name' no definida.
        # Debe usarse la cadena literal 'name' como clave del diccionario 'task'.
        print(f"{index} - {task['name']}")
