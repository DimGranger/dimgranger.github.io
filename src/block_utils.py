from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    l = markdown.split("\n\n")
    final_list = []
    for b in l:
        b = b.strip()
        if b:
            final_list.append(b)
    return final_list

def block_to_block_type(block):
    if _check_is_heading(block):
        return BlockType.HEADING
    if _check_is_code(block):
        return BlockType.CODE
    if _check_is_quote(block):
        return BlockType.QUOTE
    if _check_is_ordered_list(block):
        return BlockType.ORDERED_LIST
    if _check_is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    return BlockType.PARAGRAPH

def _check_is_heading(block):
    leading = 0
    c = ""
    for c in block:
        if c == "#":
            leading += 1
        else:
            break
    return leading < 7 and c == " "

def _check_is_code(block):
    return len(block) >= 6 and block[0:3] == "```" and block[-3:] == "```" and block.count("`") == 6

def _check_is_quote(block):
    lines = block.split("\n")
    is_quote = True
    for l in lines:
        is_quote &= l[0] == ">"
    return is_quote

def _check_is_unordered_list(block):
    lines = block.split("\n")
    is_unordered_list = True
    for l in lines:
        is_unordered_list &= (len(l) >= 2 and l[:2] == "- ")
    return is_unordered_list

def _check_is_ordered_list(block):
    lines = block.split("\n")
    is_ordered_list = True
    n = 1
    for l in lines:
        is_ordered_list &= (len(l) >= 3 and l[0].isdigit() and int(l[0]) == n and l[1] == "." and l[2] == " ")
        n += 1
    return is_ordered_list
