from textnode import TextNode, TextType
import re


def split_nodes_delimiter(
        old_nodes: list[TextNode],
        delimiter: str,
        text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type.TEXT:
            new_nodes.append(old_node)
            continue
        text_contents = old_node.text

        splits = text_contents.split(delimiter)
        number_of_splits = len(splits)
        if number_of_splits % 2 == 0:
            raise Exception("Invalid syntax, no closing delimiter in text.")

        for i in range(number_of_splits):
            if i % 2 == 0 and splits[i]:
                new_nodes.append(TextNode(splits[i], old_node.text_type))
            elif i % 2 != 0 and splits[i]:
                new_nodes.append(TextNode(splits[i], text_type))

    return new_nodes


# Funktioniert nicht, weil es nur https: URLs zulässt, lokal oder http werden ignoriert
#    image_matches = re.findall(r"!\[(.*?)\]\((https:.*?)\)", text)
#    link_matches = re.findall(r"\[(.*?)\]\((https.*?)\)", text)
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text) # bootdev
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)" , text)
    return matches
    # /w+ funktioniert nicht, da es nur zusammenhängende Wörter akzeptiert. Da beim Beispiel nach 'Rick' ' Roll' kam,
    # hat der Regex bei space abgebrochen.
    # mit dem r"" braucht es kein backslash vor / und ebenso hat regex keine Funktion mit /, welche Backslash benötigen würde


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text_contents = old_node.text

        extracted = extract_markdown_images(text_contents) # List mit Tuplen der extrahierten Infos
        if not extracted:
            new_nodes.append(old_node)
            continue

        for image in extracted: # Das aktuelle alt / href tuple (image / https://something.com)
            image_alt, href = image # alt-Text und href des extrahierten Matches

            img_delimiter = f"![{image_alt}]({href})" # der Delimiter, nach dem ich den Text splitte

            sections = text_contents.split(img_delimiter, 1) # erster Splice, mit
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            before, after = sections
            if before != "":
                new_nodes.append(
                    TextNode(before, TextType.TEXT)
                )

            new_nodes.append(
                TextNode(
                    image_alt,
                    TextType.IMAGE,
                    href
                )
            )

            text_contents = after

        if len(text_contents) > 0: # oder wieder eine != "" zum Check nach nicht empty string
            new_nodes.append(TextNode(text_contents, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text_contents = old_node.text

        extracted = extract_markdown_links(text_contents)  # List mit Tuplen der extrahierten Infos
        if not extracted:
            new_nodes.append(old_node)
            continue

        for image in extracted:  # Das aktuelle alt / href tuple (image / https://something.com)
            target, href = image  # alt-Text und href des extrahierten Matches

            img_delimiter = f"[{target}]({href})"  # der Delimiter, nach dem ich den Text splite

            sections = text_contents.split(img_delimiter, 1)  # erster Splice, mit
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            before, after = sections
            if before != "":
                new_nodes.append(
                    TextNode(before, TextType.TEXT)
                )

            new_nodes.append(
                TextNode(
                    target,
                    TextType.LINK,
                    href
                )
            )

            text_contents = after

        if len(text_contents) > 0:  # oder wieder eine != "" zum Check nach nicht empty string
            new_nodes.append(TextNode(text_contents, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    new_nodes = [
        TextNode(text, TextType.TEXT)
    ]
    delimiter_mapping = {
        "_": TextType.ITALIC, # andere Reihenfolge für Bsp., dass ordering in dict wichtig ist für Error oder nicht.
        "**": TextType.BOLD,
        "`": TextType.CODE,
    }
    for delimiter, text_type in delimiter_mapping.items():
        new_nodes = split_nodes_delimiter(
                new_nodes,
                delimiter,
                text_type,
            )
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

