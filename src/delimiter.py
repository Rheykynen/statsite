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

"""
            hits = []
            for i, char in enumerate(text_contents):
                if char == delimiter:
                    hits.append(i)

            if len(hits) % 2 != 0:
                raise Exception("Invalid syntax, no closing delimiter in text.")

            left = text_contents[:hits[0]]
            right = text_contents[hits[1] + 1:]
            delimited = text_contents[hits[0] + 1 : hits[1]]

            print(f"Left side: {left}")
            print(f"Delimited: {delimited}")
            print(f"Right side: {right}")

            current_node = [left, right, delimited]

            if left:
                new_nodes.append(
                    TextNode(f"{left}", old_node.text_type),
                )
            new_nodes.append(TextNode(f"{delimited}", text_type))
            if right:
                new_nodes.append(TextNode(f"{right}", old_node.text_type))

    print(new_nodes)

    return new_nodes


            current = ""
            left = ""
            right = ""
            delimited = ""
            for i in range(len(old_node.text)):
                while delimiter not in left and i < len(old_node.text):
                    current += old_node.text[i]
                    i += 1
                left = current[:-len(delimiter)]
                #i += len(delimiter)
                while delimiter not in current and i < len(old_node.text):
                    current += old_node.text[i]
                    i += 1
                delimited = current[i + len(delimiter):]
                #i += len(delimiter)
                while i < len(old_node.text):
                    right += old_node.text[i]

            print(f"Left: {left}")
            print(f"Right: {right}")
            print(f"Delimited: {delimited}")


            start_idx = None
            end_idx = None

            node_text = old_node.text
            print(delimiter[0])
            length_delimiter = 0 if len(delimiter) < 2 else 1
            print(length_delimiter)
            for i in range(len(node_text)):
                if node_text[i] == delimiter[0] and start_idx is None:
                    start_idx = i + length_delimiter
                    continue
                if node_text[i] == delimiter[0] and end_idx is None:
                    end_idx = i + length_delimiter
            if end_idx is None:
                raise Exception("Invalid syntax, no closing delimiter in text.")


            left_side = node_text[:start_idx]
            if length_delimiter == 0:
                length_delimiter = 1
            delimited_text = node_text[start_idx + length_delimiter:end_idx]
            right_side = node_text[end_idx + length_delimiter:]

            if left_side:
                new_nodes.append(
                        TextNode(f"{left_side}", old_node.text_type),
                )
            new_nodes.append(TextNode(f"{delimited_text}", text_type))
            if right_side:
                new_nodes.append(TextNode(f"{right_side}", old_node.text_type))

            print(new_nodes)










    return new_nodes

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
            deli_start = hits[0]
            deli_end = hits[1]
            delimited = character[deli_start + 1: deli_end]
            print(character.split(delimited))"""