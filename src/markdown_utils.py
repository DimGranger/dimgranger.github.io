from block_utils import markdown_to_blocks, block_to_block_type, BlockType
from node_utils import text_to_nodes, text_node_to_html_node
from ParentNode import ParentNode
from LeafNode import LeafNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children_nodes = []

    for block in blocks:
        children_nodes.append(_get_html_node(block))

    return ParentNode(tag="div", children=children_nodes)

def _get_html_node(block):
    block_type = block_to_block_type(block)
    tag = _block_type_to_tag(block_type, block)
    children_nodes = []
    if block_type == BlockType.CODE:
        child = LeafNode(value=block[3:-3].strip(), tag="code")
        parent = ParentNode(tag="pre", children=[child])
        return parent

    elif block_type == BlockType.ORDERED_LIST or block_type == BlockType.UNORDERED_LIST:
        items = block.split("\n")
        for x in items:
            x = x[2:].strip()
            sub_nodes = []
            for y in text_to_nodes(x):
                sub_nodes.append(text_node_to_html_node(y))
            children_nodes.append(ParentNode("li", children=sub_nodes))

    else:
        nodes = text_to_nodes(_clean_text(block, block_type))
        for x in nodes:
            children_nodes.append(text_node_to_html_node(x))

    return ParentNode(tag, children=children_nodes)

def _block_type_to_tag(block_type, block):
    match block_type:
        case BlockType.PARAGRAPH: return "p"
        case BlockType.HEADING:
            return "h" + str(_get_heading_level(block))
        case BlockType.CODE: return "code"
        case BlockType.QUOTE: return "blockquote"
        case BlockType.ORDERED_LIST: return "ol"
        case BlockType.UNORDERED_LIST: return "ul"
    return None

def _get_heading_level(block):
    level_of_heading = 0
    while block[level_of_heading] == "#" and level_of_heading <= min(6, len(block)):
        level_of_heading += 1
    return level_of_heading

def _clean_text(block, block_type):
    match block_type:
        case BlockType.HEADING:
            heading_level = _get_heading_level(block)
            return block[heading_level + 1:]
        case BlockType.QUOTE: return block.replace("> ", "")
    return block
