import os
import shutil


def copy_static_to_public(source, destination):
    os.makedirs(destination, exist_ok=True) # make dir, skip if already exists
    # Same behavior to this:
    # if not os.path.exists(target):
    #   os.mkdir(target)

    # Content
    for content in os.listdir(source): # go through contents in the source
        origin_path = os.path.join(source, content)
        dest_path = os.path.join(destination, content)  # get sub directory path for the destination
        print(f" * {origin_path} -> {dest_path}")
        if os.path.isfile(origin_path): # if content is a file, shutilcopy it to the destination
            shutil.copy(origin_path, destination)
        else:
            copy_static_to_public(origin_path, dest_path) # recursive call the func, toggle first pass to False
