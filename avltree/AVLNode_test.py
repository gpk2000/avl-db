from AVLNode import NoNodeData, AVLNode
import unittest


class TestAVLNode(unittest.TestCase):

    def test_print_on_dummy_data(self):
        temp_node = AVLNode("name", "abc")
        try:
            print(temp_node)
        except NoNodeData:
            self.fail("Can't print the Node")

    def test_print_on_no_data(self):
        temp_node = AVLNode()
        self.assertRaises(NoNodeData, print, temp_node)

    def test_print_on_multiple_data(self):
        tdata = [
            ["name", "abc"],
            ["age", 10],
            ["alive", "no"],
        ]

        for data in tdata:
            temp_node = AVLNode(data[0], data[1])
            try:
                print(temp_node)
            except NoNodeData:
                self.fail("Can't print the Node")

    def test_avl_node_get_key_func(self):
        temp_node = AVLNode("name", "abc")
        self.assertEqual("name", temp_node.get_key())

    def test_avl_node_get_value_func(self):
        temp_node = AVLNode("name", "abc")
        self.assertEqual("abc", temp_node.get_value())


if __name__ == '__main__':
    unittest.main()
