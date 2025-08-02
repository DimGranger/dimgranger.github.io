from HTMLNode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not (tag and children):
            raise ValueError()
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("A tag is needed for ParentNodes")
        if not self.children:
            raise ValueError("Children are needed for ParentNodes")

        s = "<" + self.tag + self.props_to_html() + ">"
        for x in self.children:
            s += x.to_html()
        s += "</" + self.tag + ">"

        return s


