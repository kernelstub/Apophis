import os
import inspect
from importlib.machinery import SourceFileLoader
from core.logger import Logger
from core.modular import Module


class Log:
    def msg(status: str) -> None:
        Logger.log(status, "logs.vs", "./logs/")


class HelpCommand:
    def __init__(self) -> None:
        self.commands = {
            "help": None,
            "exit": None,
            "clear": lambda: os.system("cls" if os.name == "nt" else "clear"),
            "scripts": Subcommands.list_scripts,
            "search": None,
        }
        self.command_meta = [
            {"name": "help", "author": "oromos", "date": "16-11-2023", "description": "Display the help menu."},
            {"name": "exit", "author": "oromos", "date": "16-11-2023", "description": "Exit the program."},
            {"name": "clear", "author": "oromos", "date": "16-11-2023", "description": "Clear the screen."},
            {"name": "scripts", "author": "oromos", "date": "28-11-2025", "description": "Display available script categories."},
            {"name": "search", "author": "oromos", "date": "16-11-2023", "description": "Search for scripts by term."},
        ]

    def load_help_commands(self) -> dict:
        return {}

    def execute(self, exploits: list, folder_name: str | None = None) -> None:
        if folder_name:
            base = os.path.join("scripts", folder_name)
            if os.path.isdir(base):
                files = [f for f in os.listdir(base) if f.endswith(".py") and f != "__init__.py"]
                print("""
    Help Menu
    =========

    #   Name                                    Author         Date          Description
    -   ----                                    ------         ----          -----------""")
                for i, f in enumerate(files, 1):
                    name = os.path.splitext(f)[0]
                    path_str = f"scripts/{folder_name}/{name}"
                    author = "-"
                    date = "-"
                    desc = "-"
                    full_path = os.path.join(base, f)
                    try:
                        mod = SourceFileLoader(name, full_path).load_module()
                        for _, obj in inspect.getmembers(mod):
                            if inspect.isclass(obj) and issubclass(obj, Module) and obj is not Module:
                                inst = obj()
                                author = getattr(inst, "author", author)
                                date = getattr(inst, "creation_date", date)
                                desc = getattr(inst, "description", desc)
                                break
                    except Exception:
                        pass
                    print(f"    {i:<4}{path_str:<40}{author:<15}{date:<14}{desc}")
                print("")
            else:
                Log.msg(f"No scripts folder found -> {folder_name}")
        else:
            print("""
    Help Menu
    =========

    #   Name                                   Author         Date           Description
    -   ----                                   ------         ----           -----------""")
            for i, command in enumerate(self.command_meta, 1):
                print(f"    {i:<4}{command['name']:<40}{command['author']:<15}{command['date']:<14}{command['description']}")
            print("")

    def execute_command(self, command: str, *args) -> None:
        if command in self.commands:
            self.commands[command](*args)
        else:
            Log.msg(f"Command '{command}' not found in available commands.")


class Subcommands:
    @staticmethod
    def list_scripts() -> None:
        scripts_path = "scripts/"
        folders = [f for f in os.listdir(scripts_path) if os.path.isdir(os.path.join(scripts_path, f))] if os.path.isdir(scripts_path) else []
        print("""
    Scripts
    =========

    #   Name
    -   ----""")
        for i, folder in enumerate(folders, 1):
            print(f"    {i: <4}{folder}")
        print("\nSyntax: help <folder-name>\n")
