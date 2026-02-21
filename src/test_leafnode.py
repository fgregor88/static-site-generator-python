import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode()
        node2 = LeafNode()
        self.assertEqual(node1, node2)

    def test_to_html(self):
        node_to_html = LeafNode("p", "This is some paragraph text.").to_html()
        output = "<p>This is some paragraph text.<\\p>"
        self.assertEqual(node_to_html, output)

if __name__ == "__main__":
    unittest.main()
