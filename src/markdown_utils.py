from block_utils import markdown_to_blocks, block_to_block_type, BlockType
from node_utils import text_to_nodes, text_node_to_html_node
from HTMLNode import HTMLNode
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

    if block_type == BlockType.CODE:
        child = LeafNode(value=block[3:-3].strip(), tag="code")
        parent = ParentNode(tag="pre", children=[child])
        return parent

    if not "list" in block_type.value:
        block = block.replace("\n", " ")

    children_nodes = []
    nodes = text_to_nodes(block)
    for x in nodes:
        children_nodes.append(text_node_to_html_node(x))

    return ParentNode(tag, children=children_nodes)

def _block_type_to_tag(block_type, block):
    match block_type:
        case BlockType.PARAGRAPH: return "p"
        case BlockType.HEADING:
            level_of_heading = 0
            while block[level_of_heading] == "#" and level_of_heading <= min(6, len(block)):
                level_of_heading += 1
            return "h" + level_of_heading
        case BlockType.CODE: return "code"
        case BlockType.QUOTE: return "blockquote"
        case BlockType.ORDERED_LIST: return "ol"
        case BlockType.UNORDERED_LIST: return "ul"
    return None
