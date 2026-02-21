import unittest

from htmlnode import HtmlNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = HtmlNode()
        node2 = HtmlNode()
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
