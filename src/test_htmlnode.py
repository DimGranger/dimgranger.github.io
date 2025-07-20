import unittest

from src.HTMLNode import HTMLNode


class MyTestCase(unittest.TestCase):
    def test_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        html_node = HTMLNode(props=props)
        expected = ' href="https://www.google.com" target="_blank"'
        actual = html_node.props_to_html()
        self.assertEqual(actual, expected)

    def test_none_props(self):
        html_node = HTMLNode(props=None)
        expected = ""
        actual = html_node.props_to_html()
        self.assertEqual(actual, expected)

    def test_repr_with_children(self):
        html_node = HTMLNode("link", "a", [HTMLNode("text", "p")], {"href": "https://www.google.com", })
        expected = '<a href="https://www.google.com">\nlink\n\t<p>text</p>\n</a>'
        actual = html_node.get_rec_repr(0)
        print("\n")
        print(actual)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
