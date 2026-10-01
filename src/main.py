import shutil
import os

from copystatic import copy_static_to_public
from gencontent import generate_pages_recursive


path_static = "./static"
path_public = "./public"
path_content = "./content"
path_template = "./template.html"


def main():
    print("Deleting public directory...")
    # Check if dir exists and if first_pass is True
    if os.path.exists(path_public):
        shutil.rmtree(path_public)

    print("Copying static files to public directory...")
    copy_static_to_public(path_static, path_public)

    print("Generating html files...")
    generate_pages_recursive(path_content, path_template, path_public)


if __name__ == "__main__":
    main()
