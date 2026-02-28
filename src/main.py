import os
import time

from utils import *

def main():
    # Get checking interval
    try:
        check_interval = int(grab_env("CHECK_INTERVAL", 10))
    except TypeError:
        print("ERROR: CHECK_INTERVAL could not be converted to an integer.")
        hang()

    # Get config directory
    config_directory = grab_env("CONFIG_DIR", "/config/")
    
    if config_directory[-1] != "/":
        config_directory += "/"

    # Set theme
    theme = grab_env("THEME", "catppuccin-mocha")

    while True:
        files = os.listdir(config_directory)

        for file in files:
            if file.split(".")[-1] == "yaml":
                print(read_yaml(config_directory + file))

        print(f"DONE | sleeping for {check_interval} seconds")
        time.sleep(check_interval)


if __name__ == "__main__":
    main()
    