from LeafNode import LeafNode
from textnode import TextNode, TextType
import re

def text_to_nodes(text):
    n = TextNode(text, TextType.TEXT)
    l = split_nodes_delimiter([n], "**", TextType.BOLD)
    l = split_nodes_delimiter(l, "_", TextType.ITALIC)
    l = split_nodes_delimiter(l, "```", TextType.CODE)
    l = split_nodes_link(l)
    l = split_nodes_image(l)
    return l

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

def split_nodes_image(old_nodes):
    final_list = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            final_list.append(node)
            continue
        text_to_split = node.text
        for (image_alt, image_link) in images:
            prefix, rest = text_to_split.split(f"![{image_alt}]({image_link})", 1)
            final_list.append(TextNode(prefix, TextType.TEXT))
            final_list.append(TextNode(image_alt, TextType.IMAGE, image_link))
            text_to_split = rest

        if text_to_split != "":
            final_list.append(TextNode(text_to_split, TextType.TEXT))

    return final_list

def split_nodes_link(old_nodes):
    final_list = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            final_list.append(node)
            continue
        text_to_split = node.text
        for (link_alt, url) in links:
            prefix, rest = text_to_split.split(f"[{link_alt}]({url})", 1)
            final_list.append(TextNode(prefix, TextType.TEXT))
            final_list.append(TextNode(link_alt, TextType.LINK, url))
            text_to_split = rest

        if text_to_split != "":
            final_list.append(TextNode(text_to_split, TextType.TEXT))

    return final_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)



