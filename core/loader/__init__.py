import os
import inspect
from typing import List
from importlib.machinery import SourceFileLoader


class ExploitLoader:
    def __init__(self, base_dir: str | None = None) -> None:
        self.base_dir: str = base_dir or os.environ.get("APOPHIS_SCRIPTS_DIR", "scripts")
        self.exploits: List[object] = []

    def load(self) -> None:
        base_dirs: List[str] = [self.base_dir]
        if not os.path.isdir(self.base_dir):
            base_dirs.append("exploits")
        for base in base_dirs:
            if not os.path.isdir(base):
                continue
            for root, _, files in os.walk(base):
                for filename in files:
                    if not filename.endswith(".py") or filename == "__init__.py":
                        continue
                    full_path = os.path.join(root, filename)
                    try:
                        module = SourceFileLoader(filename[:-3], full_path).load_module()
                    except Exception:
                        continue
                    for _, obj in inspect.getmembers(module):
                        try:
                            from core.modular import Module  # type: ignore
                        except Exception:
                            Module = object  # type: ignore
                        if inspect.isclass(obj) and issubclass(obj, Module) and obj is not Module:
                            instance = obj()
                            instance.folder = os.path.relpath(root, base)
                            self.exploits.append(instance)
