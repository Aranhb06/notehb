import typer
from notehb.core import files_read, initial_config, list_task, files_save
app = typer.Typer()

config = files_read('~/.config/notehb/.config.json')
config_file_list = config[]
initial_config()

@app.command(name = 'list', help = 'chema')
def ls(ls: bool = False):
    if ls:
        list_list = os.system(f'ls {}')
    else:

@app.command(name = 'task', help = 'chema')
def list(ls: bool = False):
    if ls:
        
    else:

def add(name: str, add: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
