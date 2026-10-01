import os
import shutil


def copy_static_to_public(source, destination):
    os.makedirs(destination, exist_ok=True) # make dir, skip if already exists
    # Same behavior to this:
    # if not os.path.exists(target):
    #   os.mkdir(target)

    # Content
    source_contents = os.listdir(source) # list the contents of source
    for content in source_contents: # go through contents in the source
        origin_dir_path = os.path.join(source, content)
        target_dir_path = os.path.join(destination, content)  # get sub directory path for the destination
        print(f" * {origin_dir_path} -> {target_dir_path}")
        if os.path.isfile(origin_dir_path): # if content is a file, shutilcopy it to the destination
            shutil.copy(origin_dir_path, destination)
        else:
            copy_static_to_public(origin_dir_path, target_dir_path) # recursive call the func, toggle first pass to False
