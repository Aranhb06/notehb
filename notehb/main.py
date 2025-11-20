import typer
import os
from .core import files_read, initial_config, list_task

app = typer.Typer()

config = files_read('~/.config/notehb/.config.json')
# config_file_list = config[]
file = '~/.config/notehb/hb_list/default.json'
initial_config()

@app.command()
def list(
        list: bool = typer.Option(
            False, 
            "-l", "--list", 
            help="Listar TODAS las tareas."
            )
        ):
    if list: 
        data = files_read(file)
        list_task(data)


# def add(name: str, add: bool = False):
#     if formal:
#         print(f"Goodbye Ms. {name}. Have a good day.")
#     else:
#         print(f"Bye {name}!")


if __name__ == "__main__":
    app()
