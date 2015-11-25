import os
from importlib import import_module

def get_modules(modules_dir):
    dirs = []

    # we accept a list of directories:
    if isinstance(modules_dir, list):
        for d in modules_dir:
            dirs = dirs + get_modules(d)

    # we're dealing with a single directory:
    else:
        for f in os.listdir(modules_dir):
            path = os.path.join(modules_dir, f)
            if os.path.isdir(path):
                dirs.append(path.replace('/', '.'))

    return dirs

def get_imported(modules_dir):
    mods = []
    for m in get_modules(modules_dir):
        mods.append(import_module(m))
    return mods