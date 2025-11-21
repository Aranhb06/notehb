import typer
import os
from .core import files_read, initial_config, list_task_view, path_relative, add_task

app = typer.Typer()


# Configuracion  inicial
config_dir = path_relative('~/.config/notehb')
config_file= config_dir + '/config.json'
file_dir = config_dir + '/hb_list/'
file = file_dir + '/defaul.json' 

# config_file_list = config[]
initial_config(config_dir,config_file,file_dir,file)

list_task = files_read(file)

@app.command()
def list(
        list: bool = typer.Option(
            False, 
            "-l", "--list", 
            help="Listar todas las tareas."
            )
        ):
    if list: 
        data = files_read(file)
        list_task_view(data)

@app.command
def add(
    texto_tarea: str = typer.Argument(
        ...,
        "-a", "--add",
        help="El nombre de la tarea, seguido opcionalmente por la descripción y la fecha."
    )
):
    """
    Añade una nueva tarea a la lista.
    """
    # 1. Une la lista de palabras (texto_tarea) que Typer recoge del
    #    usuario en la única cadena de texto que tu función espera.
    data = " ".join(texto_tarea)

    # 2. Llama a tu función original 'add_task' con las variables exactas
    #    que necesita: las globales 'file' y 'list_task', y la variable
    #    local 'data' que acabamos de crear.
    add_task(file, list_task, data)


# def add(name: str, add: bool = False):
#     if formal:
#         print(f"Goodbye Ms. {name}. Have a good day.")
#     else:
#         print(f"Bye {name}!")


if __name__ == "__main__":
    app()
