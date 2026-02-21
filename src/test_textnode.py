import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("text_1", TextType.PLAIN)
        node2 = TextNode("text_1", TextType.PLAIN)
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("text_1", TextType.PLAIN)
        node2 = TextNode("text_2", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_link_eq(self):
        node1 = TextNode("text_1", TextType.PLAIN, "www.website.com")
        node2 = TextNode("text_1", TextType.PLAIN, "www.website.com")
        self.assertEqual(node1, node2)

    def test_link_not_eq(self):
        node1 = TextNode("text_1", TextType.PLAIN, "www.website1.com")
        node2 = TextNode("text_1", TextType.PLAIN, "www.website2.com")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
