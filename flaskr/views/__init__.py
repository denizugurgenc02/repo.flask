import importlib
import pkgutil

from flask import Blueprint, Flask


def register_blueprints(app: Flask):
    package_dir = __path__[0]

    for finder, module_name, is_pkg in pkgutil.iter_modules([package_dir]):

        if module_name == "__init__":
            continue

        module = importlib.import_module(f".{module_name}", __name__)

        if hasattr(module, "bp") and isinstance(module.bp, Blueprint):
            blueprint = module.bp

            app.register_blueprint(blueprint)

            print(f"Successfully created views: {module_name}")
