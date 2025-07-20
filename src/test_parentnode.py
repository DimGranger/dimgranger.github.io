import unittest
from ParentNode import ParentNode
from LeafNode import LeafNode

class MyTestCase(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("child", "span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_several_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )
        self.assertEqual(
            node.to_html(),
            """<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>""",
        )

    def test_no_child(self):
        def empty_parent():
            return ParentNode("p", [])
        self.assertRaises(ValueError, empty_parent)
        child_node = LeafNode("child", "span")
        parent_node = ParentNode("div", [child_node])
        parent_node.children = []
        self.assertRaises(ValueError, parent_node.to_html)

    def test_no_tag(self):
        child_node = LeafNode("child", "span")
        def no_tag():
            return ParentNode("", [child_node])
        self.assertRaises(ValueError, no_tag)
        parent_node = ParentNode("div", [child_node])
        parent_node.tag = None
        self.assertRaises(ValueError, parent_node.to_html)


if __name__ == '__main__':
    unittest.main()
