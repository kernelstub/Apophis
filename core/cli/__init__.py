import sys
import warnings
from typing import Optional
from importlib.machinery import SourceFileLoader
import os

from core.loader import ExploitLoader
from modules.help import HelpCommand, Subcommands
from modules.search import SearchCommand
from data.banner import Display
from core.logger import Logger


class Log:
    @staticmethod
    def msg(status: str) -> None:
        Logger.log(status, "logs.vs", "./logs/")


def repl(loader: ExploitLoader, help_command: HelpCommand, search_command: SearchCommand) -> None:
    try:
        while True:
            user_input = input("(local) Apophis ~$ ").strip().split()
            command = user_input[0] if user_input else None

            match command:
                case "" | None:
                    pass
                case "help":
                    folder_name = user_input[1] if len(user_input) > 1 else None
                    help_command.execute(loader.exploits, folder_name)
                case "search":
                    term = user_input[1] if len(user_input) > 1 else None
                    if term:
                        search_command.execute(loader.exploits, term)
                    else:
                        Log.msg("Please provide a search term")
                case "exit":
                    Log.msg("Exiting Apophis...")
                    break
                case _:
                    # path-style execution: scripts/<folder>/<file>[.py]
                    if command and command.startswith("scripts/"):
                        path = command if command.endswith(".py") else f"{command}.py"
                        if os.path.isfile(path):
                            module = SourceFileLoader(os.path.basename(path)[:-3], path).load_module()
                            for _, obj in __import__('inspect').getmembers(module):
                                try:
                                    from core.modular import Module  # type: ignore
                                except Exception:
                                    Module = object  # type: ignore
                                if __import__('inspect').isclass(obj) and issubclass(obj, Module) and obj is not Module:
                                    instance = obj()
                                    print()
                                    instance.execute()
                                    print()
                                    break
                        else:
                            Log.msg(f"Script not found -> {path}")
                    else:
                        exploit = next((e for e in loader.exploits if e.name == command), None)
                        if exploit:
                            print()
                            exploit.execute()
                            print()
                        else:
                            help_command.execute_command(command)
    except KeyboardInterrupt:
        print()
        Log.msg("Exiting Apophis...")
        sys.exit()


def main(argv: Optional[list[str]] = None) -> None:
    argv = argv if argv is not None else sys.argv[1:]
    warnings.filterwarnings("ignore", message=".*pkg_resources is deprecated.*", category=UserWarning)
    Display.banner()
    help_command = HelpCommand()
    search_command = SearchCommand()

    if not argv or argv[0] == "repl":
        loader = ExploitLoader()
        loader.load()
        repl(loader, help_command, search_command)
        return

    cmd = argv[0]
    if cmd == "list":
        Subcommands.list_scripts()
    elif cmd == "help":
        folder = argv[1] if len(argv) > 1 else None
        if folder == "all":
            loader = ExploitLoader()
            loader.load()
            help_command.execute(loader.exploits, folder)
        elif folder:
            loader = ExploitLoader()
            loader.load()
            help_command.execute(loader.exploits, folder)
        else:
            help_command.execute([], None)
    elif cmd == "search" and len(argv) > 1:
        loader = ExploitLoader()
        loader.load()
        search_command.execute(loader.exploits, argv[1])
    elif cmd == "run" and len(argv) > 1:
        loader = ExploitLoader()
        loader.load()
        name = argv[1]
        exploit = next((e for e in loader.exploits if e.name == name), None)
        if exploit:
            exploit.execute()
        else:
            Log.msg(f"Exploit '{name}' not found")
    else:
        Log.msg("Unknown command. Use: repl | list | help [folder] | search <term> | run <name>")
