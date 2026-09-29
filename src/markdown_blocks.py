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
            continue
        return heading


def clean_block_string(block: str) -> str:
    return block.replace("\n", " ").strip()

def clean_heading(block: str, heading: int) -> str:
    return block[heading:].strip()

def clean_quote_string(block: str) -> str:
    return block[2:].strip()

def clean_code_block(block: str) -> str:
    cleaned = block.replace("```", "").strip()
    return f"<code>{cleaned}\n</code>"

def make_list_strings(block: str):
    assert block.startswith("- ") or block.startswith("1. ")
    new = ""
    ulist = block.split("\n")
    for line in ulist:
        content = line[2:].strip()
        new += f"<li>{content}</li>"
    return new

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


def code_type_handler(block):
    block_node = ParentNode("pre", [])

    text = clean_code_block(block)

    code_node = TextNode(text, TextType.TEXT)

    leaf = text_node_to_html_node(code_node)
    block_node.children.append(leaf)
    return block_node

def markdown_to_html_node(markdown: str) -> HTMLNode:
    """
    - nehme den Markdowntext, splitte es in Blöcke
    - bestimme den Texttyp und erstelle daraus eine HTMLNode
    - doc ist ParentNode(div,...)
    - block ist ein ParentNode, manchmal nested bei ul oder li
    - Leaf Nodes sind die Inline Blocks, von text to children, -> raw TextNode > LeafNode via text_node_to_html_node
    """
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
            text = make_list_strings(block)
            leafs = block_to_nodes(
                "ul", text
            )
            html_node.children.append(leafs)

        if block_type == BlockType.OLIST:
            text = make_list_strings(block)
            leafs = block_to_nodes(
                "ol", text
            )
            html_node.children.append(leafs)

        if block_type == BlockType.CODE:
            code_node = code_type_handler(block)
            html_node.children.append(code_node)


    return html_node



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

""",
"""
## This is heading nummero 2

> this is a very fancy quote one needs to have a very high intelligence

this should be a normal paragraph

- oh
- a list
- how wonderful

1. How to get kicked in the balls
This is a guide how to fuck up a ordered list and subsequent _consequences_.
""",
"""
``` 
This is a code Markdown block.
it stretches over two rows
```

But this is a paragraph with `code` in the middle of it.
"""
    ]
    for thing in examples:
        markdown_to_html_node(thing)

if __name__ == "__main__":
    main()