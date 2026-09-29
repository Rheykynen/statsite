from enum import Enum

from htmlnode import ParentNode, HTMLNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, text_node_to_html_node, TextType

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

def determine_heading_type(block: str) -> int:
    heading = 0
    for letter in block:
        if letter == "#":
            heading += 1
        else:
            break
    if heading + 1 >= len(block):
        raise ValueError(f"invalid heading level: {heading}")
    return heading

def clean_block_string(block: str) -> str:
    return block.replace("\n", " ").strip()

def clean_heading(block: str, heading: int) -> str:
    return block[heading:].strip()

def clean_quote_string(block: str) -> str:
    return block[2:].strip()

def make_list_nodes(tag: str, block: str):
    ulist = block.split("\n")
    list_items = []
    for line in ulist:
        content = line[2:].strip()
        li_node = ParentNode("li", [])
        text_to_children(content, li_node)
        list_items.append(li_node)
    return ParentNode(tag, list_items)

def text_to_children(text: str, block_node) -> HTMLNode:
    text_node = text_to_textnodes(text)
    for node in text_node:
        block_node.children.append(
            text_node_to_html_node(node)
        )
    return block_node

def block_to_nodes(tag, block):
    block_node = ParentNode(tag, [])
    leafs = text_to_children(block, block_node)
    return leafs

def code_type_handler(block: str) -> ParentNode:
    cleaned = block[4:-3]
    code_text_node = TextNode(cleaned, TextType.TEXT)
    code_leaf = text_node_to_html_node(code_text_node)
    code_node = ParentNode("code", [code_leaf])
    return ParentNode("pre", [code_node])

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown) # mach aus Markdown blöcke
    html_node = ParentNode("div", [])
    for block in blocks:

        block_type = block_to_block_type(block) # ich bestimme den Block-Typ
        if block_type == BlockType.PARAGRAPH:
            text = clean_block_string(block)

            leafs = block_to_nodes(
                "p", text
            )
            html_node.children.append(leafs)

        if block_type == BlockType.HEADING:
            heading = determine_heading_type(block)
            text = clean_heading(block, heading)

            leafs = block_to_nodes(
                f"h{heading}", text
            )
            html_node.children.append(leafs)

        if block_type == BlockType.QUOTE:
            text = clean_quote_string(block)
            leafs = block_to_nodes(
                "blockquote", text
            )
            html_node.children.append(leafs)

        if block_type == BlockType.ULIST:
            ul_parent = make_list_nodes("ul", block)
            html_node.children.append(ul_parent)

        if block_type == BlockType.OLIST:
            ol_parent = make_list_nodes("ol", block)
            html_node.children.append(ol_parent)

        if block_type == BlockType.CODE:
            code_node = code_type_handler(block)
            html_node.children.append(code_node)

    return html_node
