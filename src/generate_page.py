from markdown_blocks import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split("\n\n")
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

    with open(from_path, "r") as from_file:
        md_file = from_file.read()
        with open(template_path, "r") as temp_file:
            template_file = temp_file.read()

            html_node = markdown_to_html_node(md_file)
            html_str = html_node.to_html()
            page_title = extract_title(md_file)
            html_file = template_file.replace("{{ Title }}", page_title).replace("{{ Content }}", html_str)

            if not os.path.exists(dest_path):
                os.makedirs(dest_path, exist_ok=True)


            destination_path = os.path.join(dest_path, "index.html")
            print(f"Writing to {destination_path}")

            index_file = open(destination_path, "x")
            index_file.write(html_file)
            index_file.close()

