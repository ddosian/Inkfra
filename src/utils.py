import os
import yaml

def hang():
    while True:
        continue

def grab_env(label, default):
    value = os.getenv(label)
    if value == None:
        print(f"WARNING: {label} is not defined.")
        print(f" | Using default value ({default})")
        return default
    else:
        return value

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def read_yaml(path):
    return yaml.safe_load(read_file(path))

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)