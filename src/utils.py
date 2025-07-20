from LeafNode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node: TextNode):
    tag = None
    value = None
    props = None
    if text_node.text_type == TextType.TEXT:
        value = text_node.text
    elif text_node.text_type == TextType.CODE:
        value = text_node.text
        tag = "code"
    elif text_node.text_type == TextType.BOLD:
        value = text_node.text
        tag = "b"
    elif text_node.text_type == TextType.ITALIC:
        value = text_node.text
        tag = "i"
    elif text_node.text_type == TextType.LINK:
        value = text_node.text
        tag = "a"
        props = {"href": text_node.url}
    elif text_node.text_type == TextType.IMAGE:
        value = ""
        tag = "img"
        props = {"src": text_node.url,
                 "alt_text":  text_node.text}
    return LeafNode(value, tag, props)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            final_list.append(old_node)
            continue
        text = old_node.text
        s = text.split(delimiter)

        if len(s) % 2 != 1:
            raise ValueError("Error when parsing")

        for i, b in enumerate(s):
            if i % 2 == 1:
                final_list.append(TextNode(b, text_type))
            else:
                final_list.append(TextNode(b, TextType.TEXT))

    return final_list



