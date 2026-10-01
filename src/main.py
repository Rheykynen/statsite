import shutil
import os


def copy_static_to_public(source, destination, first_pass=True):
    # Check if dir exists and if first_pass is True
    if os.path.exists(destination) and first_pass is True:
        shutil.rmtree(destination)

    os.makedirs(destination, exist_ok=True) # make dir, skip if already exists

    # Content
    source_contents = os.listdir(source) # list the contents of source
    for content in source_contents: # go through contents in the source
        content_path = os.path.join(source, content)
        if os.path.isfile(content_path): # if content is a file, shutilcopy it to the destination
            shutil.copy(os.path.join(source, content), destination)
        else: # if it is a directory
            sub_dir_path = os.path.join(destination, content) # get sub directory path for the destination
            os.makedirs(sub_dir_path, exist_ok=True) # make the directory in the destination
            copy_static_to_public(content_path, sub_dir_path, False) # recursive call the func, toggle first pass to False


def main():
    pass

if __name__ == "__main__":
    copy_static_to_public("static", "public")