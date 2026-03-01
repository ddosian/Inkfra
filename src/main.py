import os
import time

from utils import *
from generators import *

def main():
    skeleton_template = read_file("/app/templates/skeleton.html")

    # Get debug output
    try:
        debug_output = bool(grab_env("DEBUG_OUTPUT", False))
    except TypeError:
        print("ERROR: DEBUG_OUTPUT could not be converted to an boolean.")
        hang()

    # Get checking interval
    try:
        check_interval = int(grab_env("CHECK_INTERVAL", 10))
    except TypeError:
        print("ERROR: CHECK_INTERVAL could not be converted to an integer.")
        hang()

    # Get export path
    export_path = grab_env("OUTPUT_DIR", "/output/")
    if export_path[-1] != "/":
        export_path += "/"

    # Get config directory
    config_directory = grab_env("CONFIG_DIR", "/config/")
    if config_directory[-1] != "/":
        config_directory += "/"

    # Set theme
    theme = grab_env("THEME", "catppuccin-mocha")

    if debug_output:
        print("Starting with the following env variables:")
        print(f" | DEBUG_OUTPUT: {debug_output}")
        print(f" | CHECK_INTERVAL: {check_interval}")
        print(f" | OUTPUT_DIR: {export_path}")
        print(f" | CONFIG_DIR: {config_directory}")
        print(f" | THEME: {theme}")

    while True:
        files = os.listdir(config_directory)
        if debug_output:
            print(f"files: {files}")

        for file in files:
            if debug_output:
                print(f"looping over {files}")
                print(f" | current file: {file}")
            if file.split(".")[-1] == "yaml":
                content = read_yaml(config_directory + file)
                if debug_output:
                    print(f"  | {file} is a yaml file")
                    print(f"  | Content: \n{content}")

                export_file_name = file.split(".")[0] + ".html"

                print(f"Generating new HTML from {file} in {export_path}{export_file_name}")

                html = skeleton_template.replace("TITLE_CAPS", content["title"].upper())
                html = html.replace("TITLE", content["title"])
                
                theme_variables = read_file(f"/app/themes/{content["theme"]}.css")
                main_css = read_file("/app/templates/main.css")
                theme_variables = theme_variables.replace("MAIN_CSS", main_css)
                html = html.replace("THEME_VARIABLES", theme_variables)

                if debug_output:
                    print(f"  | Generated HTML so far:\n{html}")

                body = generate_body(content, debug_output)

                html = html.replace("BODY", body)
                html = html.replace("TAGS", generate_tags(content, debug_output))
                if debug_output:
                    print(f"  | Generated HTML so far:\n{html}")

                write_file(export_path + export_file_name, html)



        print(f"DONE | sleeping for {check_interval} seconds")
        time.sleep(check_interval)


if __name__ == "__main__":
    main()
    