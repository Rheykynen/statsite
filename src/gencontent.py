from markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("#").strip(" ")
    raise Exception("no h1 header in markdown")


def generate_page(
        base_path,
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
        .replace('href="/', f'href="{base_path}')
        .replace('src="/', f'src="{base_path}')
    )

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(html_file)

def generate_pages_recursive(
        base_path: str,
        dir_path_content: str,
        template_path: str,
        dir_path_dest: str,
):
    for filename in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dir_path_dest, filename)

        if os.path.isfile(item_path):
            raw_filename = filename.split(".")
            dest_path = os.path.join(dir_path_dest, raw_filename[0] + ".html")
            generate_page(
                base_path=base_path,
                from_path=item_path,
                template_path=template_path,
                dest_path=dest_path,
            )
        else:
            generate_pages_recursive(base_path, item_path, template_path, dest_path)

