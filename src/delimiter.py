from textnode import TextNode, TextType

def split_nodes_delimiter(
        old_nodes: list[TextNode],
        delimiter: str,
        text_type: TextType
) -> list[TextNode]:

    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type.TEXT:
            new_nodes.append(old_node)
        else:
            character = old_node.text
            hits = []
            for i in range(len(character)):
                if character[i] == delimiter:
                    hits.append(i)
            if len(hits) % 2 != 0:
                raise Exception(f"Invalid Syntax, no closing delimiter in Text")

            delimited = character[hits[0]+1: hits[1]]
            print(character.split(delimited))






    return new_nodes

