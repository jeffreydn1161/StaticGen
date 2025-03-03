import unittest
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    node = HTMLNode("h1", "This is the paragraph text", None, {"href": "https://www.google.com","target": "_blank",})
    
    def test_to_html(self):
        node = HTMLNode(None, None, None, None)
        self.assertRaises(NotImplementedError, node.to_html)
    
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=https://www.google.com target=_blank")
        
        node.props = None
        self.assertEqual(node.props_to_html(), "No properties found.")

    def test_print(self):
        node = HTMLNode("h1", "This is the paragraph text", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(repr(node), "HTMLNode(h1, This is the paragraph text, None, {'href': 'https://www.google.com', 'target': '_blank'})")

        node = HTMLNode(None, None, None, None)
        self.assertEqual(repr(node), "HTMLNode(None, None, None, None)")

if __name__ == "__main__":
    unittest.main()