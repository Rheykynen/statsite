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
            continue
        else:
            start_idx = None
            end_idx = None

            node_text = old_node.text
            for i in range(len(node_text)):
                if node_text[i] == delimiter and start_idx is None:
                    start_idx = i
                    continue
                if node_text[i] == delimiter and end_idx is None:
                    end_idx = i
            if end_idx is None:
                raise Exception("Invalid syntax, no closing delimiter in text.")

            left_side = node_text[:start_idx]
            delimited_text = node_text[start_idx + 1:end_idx]
            right_side = node_text[end_idx + 1:]

            if left_side:
                new_nodes.append(
                        TextNode(f"{left_side}", old_node.text_type),
                )
            new_nodes.append(TextNode(f"{delimited_text}", text_type))
            if right_side:
                new_nodes.append(TextNode(f"{right_side}", old_node.text_type))

            print(new_nodes)










    return new_nodes

"""    for old_node in old_nodes:
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
            deli_start = hits[0]
            deli_end = hits[1]
            delimited = character[deli_start + 1: deli_end]
            print(character.split(delimited))"""