from AVLTree import KeyNotFoundError
import unittest
from AVLTree import AVLTree
from AVLNode import AVLNode


class TestAVLTree(unittest.TestCase):

    def test_avl_tree_insert_method(self):
        tree = AVLTree()
        for el in [16, 24, 36, 19, 44, 28, 61, 74, 83, 64, 52, 65, 86, 93, 88]:
            tree.insert_data(el, el)

        tmin = tree.find_min()
        tmax = tree.find_max()
        self.assertTrue(tmin.key == 16 and tmin.value == 16)
        self.assertTrue(tmax.key == 93 and tmax.value == 93)

        self.assertTrue(tree.check_balanced())

        tree.delete_data(88)
        self.assertTrue(tree.check_balanced())
        self.assertRaises(KeyNotFoundError, tree.get_value, 88)

        tree.delete_data(19)
        self.assertTrue(tree.check_balanced())
        self.assertRaises(KeyNotFoundError, tree.get_value, 19)

        tree.delete_data(16)
        self.assertTrue(tree.check_balanced())
        self.assertRaises(KeyNotFoundError, tree.get_value, 16)

        tree.delete_data(28)
        self.assertTrue(tree.check_balanced())
        self.assertRaises(KeyNotFoundError, tree.get_value, 28)

        tree.delete_data(24)
        self.assertTrue(tree.check_balanced())
        self.assertRaises(KeyNotFoundError, tree.get_value, 24)

        tree.delete_data(36)
        self.assertTrue(tree.check_balanced())
        self.assertRaises(KeyNotFoundError, tree.get_value, 36)

        tree.delete_data(52)
        self.assertTrue(tree.check_balanced())
        self.assertRaises(KeyNotFoundError, tree.get_value, 52)

        tree.delete_data(93)
        self.assertTrue(tree.check_balanced())
        self.assertRaises(KeyNotFoundError, tree.get_value, 93)

        tree.delete_data(86)
        self.assertTrue(tree.check_balanced())
        self.assertRaises(KeyNotFoundError, tree.get_value, 86)

        tree.delete_data(83)
        self.assertTrue(tree.check_balanced())
        self.assertRaises(KeyNotFoundError, tree.get_value, 83)


if __name__ == '__main__':
    unittest.main()
