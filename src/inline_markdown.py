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

def extract_markdown_links(text):
    matches = re.findall(r"!\[(.*?)\]\((https://.*?)\)", text)
    return matches
    # /w+ funktioniert nicht, da es nur zusammenhängende Wörter akzeptiert. Da beim Beispiel nach 'Rick' ' Roll' kam,
    # hat der Regex bei space abgebrochen.
    # mit dem r"" braucht es kein backslash vor / und ebenso hat regex keine Funktion mit /, welche Backslash benötigen würde

def extract_markdown_images(text):
    matches = re.findall(r"\[(.*?)\]\((https.*?)\)", text)
    return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    pass

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    pass

