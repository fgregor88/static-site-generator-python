import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("text_1", TextType.TEXT)
        node2 = TextNode("text_1", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("text_1", TextType.TEXT)
        node2 = TextNode("text_2", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_link_eq(self):
        node1 = TextNode("text_1", TextType.TEXT, "www.website.com")
        node2 = TextNode("text_1", TextType.TEXT, "www.website.com")
        self.assertEqual(node1, node2)

    def test_link_not_eq(self):
        node1 = TextNode("text_1", TextType.TEXT, "www.website1.com")
        node2 = TextNode("text_1", TextType.TEXT, "www.website2.com")
        self.assertNotEqual(node1, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
