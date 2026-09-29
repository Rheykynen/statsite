from enum import Enum

from htmlnode import HTMLNode
from src.htmlnode import ParentNode, LeafNode
from src.inline_markdown import text_to_textnodes
from src.textnode import TextNode, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Splittet einen gesamten Markdowntext in einzelne Blöcke nach leeren Zeilen
    """
    split_text = markdown.split("\n\n")
    filtered_blocks = []

    for text in split_text:
        if text == "":
            continue
        filtered_blocks.append(
            text.strip()
        )
    return filtered_blocks

def block_to_block_type(block: str) -> BlockType:
    """
    bestimmt den Block-Type basierend auf den einzelnen Markdown-Blöcken
    """
    if block.startswith(
            ("#", "##", "###", "####", "#####", "######")
    ):
        return BlockType.HEADING

    lines = block.split("\n")

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
            return BlockType.QUOTE

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
            return BlockType.ULIST

    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST

    return BlockType.PARAGRAPH

def text_to_children(text: str):
    node = text_to_textnodes(text)
    print(node)
    return node

def determine_heading_type(block: str) -> str:
    heading = 0
    for letter in block:
        if letter == "#":
            heading += 1
            continue
        if heading > 6:
            break

    return str(heading)

def markdown_to_html_node(markdown: str) -> HTMLNode:
    """
    - nehme den Markdowntext, splitte es in Blöcke
    - bestimme den Texttyp und erstelle daraus eine HTMLNode
    - doc ist ParentNode(div,...)
    - block ist ein ParentNode, manchmal nested bei ul oder li
    - Leaf Nodes sind die Inline Blocks, von text to children, -> raw TextNode > LeafNode via text_node_to_html_node
    """
    blocks = markdown_to_blocks(markdown) # mach aus Markdown blöcke

    for block in blocks:
        block_type = block_to_block_type(block) # ich bestimme den Block-Typ
        if block_type == BlockType.PARAGRAPH:
            # Jetzt habe ich den Text-Block mit inline markdown. Heißt, ich muss das herausholen
            text_node = text_to_textnodes(block) # das sollte meine fertige Liste an Textnodes sein
            #print(text_node)
            for i, item in enumerate(text_node, start=1):
                print(f"{i}: {item}") #der kleinste Markdown Teil, eine Liste mit TextNodes
                print(f"{item.text_type}\n")
                stuff = text_node_to_html_node(item)
                #print(stuff)
                # Jetzt muss ich die einzelnen TextNodes in ein leafnode umwandeln und an einen Parent anheften.
                # also pro md Block einen Parent



        if block_type == BlockType.HEADING:
            heading = determine_heading_type(block)
            node = HTMLNode(f"h{heading}", block)

        if block_type == BlockType.CODE:
            node = HTMLNode("code", block)

        if block_type == BlockType.QUOTE:
            node = HTMLNode("quote", block)

        if block_type == BlockType.ULIST:
            node = HTMLNode("ul", block)


        if block_type == BlockType.OLIST:
            node = HTMLNode("ol", block)




def main():
    examples = [
"""
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

""",
"""
# This is **bolded** heading

This is a paragraph.
There is no Tag here.

## This is another paragraph with _italic_ text and `code` here

###### This is the smallest heading possible

1. A list
2. second item of a list
3. third item of a list
4. Lists are not fun

"""
    ]
    for thing in examples:
        markdown_to_html_node(thing)

if __name__ == "__main__":
    main()