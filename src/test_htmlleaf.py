import unittest
from LeafNode import LeafNode


class MyTestCase(unittest.TestCase):
    def test_tag_and_value(self):
        leaf_node = LeafNode("This is a paragraph of text.", "p")
        expected = "<p>This is a paragraph of text.</p>"
        actual = leaf_node.to_html()
        self.assertEqual(expected, actual)

    def test_tag_value_props(self):
        leaf_node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        expected = """<a href="https://www.google.com">Click me!</a>"""
        actual = leaf_node.to_html()
        self.assertEqual(expected, actual)

    def test_no_tag(self):
        leaf_node = LeafNode("a")
        expected = "a"
        actual = leaf_node.to_html()
        self.assertEqual(expected, actual)

    def test_no_value(self):
        def empty_leaf():
            return LeafNode(None)
        self.assertRaises(ValueError, empty_leaf)

        leaf_node = LeafNode("a")
        leaf_node.value = None
        self.assertRaises(ValueError, leaf_node.to_html)

if __name__ == '__main__':
    unittest.main()
