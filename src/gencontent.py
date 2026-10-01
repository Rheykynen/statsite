from markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("#").strip(" ")
    raise Exception("no h1 header in markdown")


def generate_page(
        from_path,
        template_path,
        dest_path
):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        md_file = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(md_file)
    html_str = html_node.to_html()

    page_title = extract_title(md_file)
    html_file = (
        template
        .replace("{{ Title }}", page_title)
        .replace("{{ Content }}", html_str)
    )

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(html_file)


def generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_dest,
):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dir_path_dest, "index.html")

        if os.path.isfile(item_path):
            generate_page(
                item_path,
                template_path,
                dest_path
            )
        else:
            dest_path_dir = os.path.join(dir_path_dest, item)
            generate_pages_recursive(item_path, template_path, dest_path_dir)

