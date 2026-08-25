from pprint import pprint

from textnode import TextNode, TextType
import re


def split_nodes_delimiter(
        old_nodes: list[TextNode], delimiter: str, text_type: TextType
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


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        text_contents = old_node.text

        extracted = extract_markdown_images(text_contents) # List mit Tuplen der extrahierten Infos
        matches = len(extracted) # Wie viele alt / href Tuple ich habe

        for extract in extracted: # Das aktuelle alt / href tuple (image / https://something.com)
            current_match = extract
            image_alt = current_match[0] # image
            href = current_match[1] # https://something.com
            delimiter = f"![{image_alt}]({href})"
            section = text_contents.split(delimiter, 1)
            print(section)
            new_nodes.append(TextNode(section[0], TextType.TEXT))
            new_nodes.append(TextNode(extract[0], TextType.IMAGE, extract[1]))
            text_contents = text_contents.replace(f"{section[0]}{delimiter}", "")
            print(text_contents)
    print(new_nodes)
    return new_nodes



def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    pass

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((https:.*?)\)", text)  # r"!\[([^\[\]]*)\]\(([^\(\)]*)\)" bootdev
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((https.*?)\)", text) # r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)" bootdev
    return matches
    # /w+ funktioniert nicht, da es nur zusammenhängende Wörter akzeptiert. Da beim Beispiel nach 'Rick' ' Roll' kam,
    # hat der Regex bei space abgebrochen.
    # mit dem r"" braucht es kein backslash vor / und ebenso hat regex keine Funktion mit /, welche Backslash benötigen würde
