from HTMLNode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        if value is None:
            raise ValueError()
        super().__init__(value, tag, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError()
        has_tag = self.tag is not None
        if not has_tag:
            return self.value
        return "<" + self.tag + self.props_to_html() + ">" + self.value + "</" + self.tag + ">"
