import shutil
import os

from copystatic import copy_static_to_public
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
path_template = "./template.html"


def main():
    print("Deleting public directory...")
    # Check if dir exists and if first_pass is True
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_static_to_public(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, path_template, dir_path_public)


if __name__ == "__main__":
    main()
