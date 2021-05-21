import unittest
from AVLTree import AVLTree
from AVLNode import AVLNode


class TestAVLTree(unittest.TestCase):

    def test_avl_tree_insert_method(self):
        tree = AVLTree()
        
        tree.insert_data(1, 1)
        tree.insert_data(2, 2)
        tree.insert_data(3, 3)
        tree.insert_data(4, 4)
        out = tree.get_all_data()
        self.assertEqual(tree.root.get_key(), 2)
        

if __name__ == '__main__':
    unittest.main()
