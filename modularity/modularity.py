def get_modules(modules_dir):
    dirs = []
    for f in os.listdir(modules_dir):
        path = os.path.join(modules_dir, f)
        if os.path.isdir(path):
            dirs.append(path.replace('/', '.'))
    return dirs