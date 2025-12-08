import importlib
import pkgutil


def load_all_models():
    package_dir = __path__[0]

    for _, module_name, _ in pkgutil.iter_modules([package_dir]):

        if module_name == "__init__":
            continue

        importlib.import_module(f".{module_name}", __name__)
        print(f"Loaded model: {module_name}")
