from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    split_text = markdown.split("\n\n")
    filtered_blocks = []

    for text in split_text:
        if text == "":
            continue
        filtered_blocks.append(
            text.strip()
        )
    return filtered_blocks

def block_to_block_type(block: str):
    if "# " in block:
        count = 0
        for letter in block:
            if letter == "#":
                count += 1
                continue
        if count < 6:
            return BlockType.HEADING
        else:
            raise Exception("too many # in block")
    elif block.startswith("``` "):
        return BlockType.CODE
    elif block.startswith("> "):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif block.startswith(". "):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
