
class HTMLNode:
    def __init__(self, value=None, tag=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        s = ""
        if self.props is not None:
            for k, v in self.props.items():
                s += " " + k + "=" + '"' + v + '"'
        return s

    def get_rec_repr(self, depth):
        s = ""
        has_children = self.children is not None
        tabs = ("\t" * depth)

        if self.tag is not None:
            s += tabs +  "<" + self.tag + self.props_to_html() + ">"

        if has_children:
            s += "\n"
            s += (tabs +  self.value + "\n") if self.value is not None else ""
            for x in self.children:
                s += x.get_rec_repr(depth + 1)  + "\n"
            if self.tag is not None:
                s += tabs +  "</" + self.tag + ">"
            return s

        else:
            s += (self.value if self.value is not None else "") +  "</" + self.tag + ">"

        return s

    def __repr__(self):
        return self.get_rec_repr(0)







