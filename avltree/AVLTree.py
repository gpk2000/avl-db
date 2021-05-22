from unittest.signals import removeResult
from AVLNode import AVLNode


class AVLTree(object):

    def __init__(self) -> None:
        super().__init__()
        self.root = None

    def _height(self, root) -> int:
        """Height of the AVL tree

        Args:
            root (AVLNode): root of the tree

        Returns:
            int: resulting height
        """
        if not root:
            return 0

        return root.height

    def get_height(self) -> int:
        return self._height(self.root)

    def _balance_factor(self, root) -> int:
        """Calculates the balance factor of the AVL Tree

        Args:
            root (AVLNode): the root of the tree

        Returns:
            int: resulting balance factor
        """
        if not root:
            return 0

        return self._height(root.left) - self._height(root.right)

    def get_balance_factor(self) -> int:
        return self._balance_factor(self.root)

    def get_all_data(self) -> list:
        """Gets all the data present in the AVL tree and stores
        it in a list. The data is ordered ascending according to
        the key

        Returns:
            list: resulting data
        """
        out = []

        def recurse(root) -> None:
            """standard inorder traversal of binary tree

            Args:
                root (AVLNode): the root of the tree
            """
            nonlocal out
            if not root:
                return

            recurse(root.left)
            key = root.get_key()
            value = root.get_value()
            out.append([key, value])
            recurse(root.right)

        recurse(self.root)
        return out

    def _insert(self, root, key, value) -> AVLNode:
        """Inserts the (key, value) pair in the AVL Tree and 
        self balances itself.

        Args:
            root (AVLNode): the root of the tree
            key (str): the key to be inserted
            value (str): the value to be mapped for key

        Returns:
            AVLNode: resulting root after self balancing itself
        """
        if not root:
            return AVLNode(key, value)

        rkey = root.get_key()

        if key == rkey:
            root.value = value
        elif key < rkey:
            root.left = self._insert(root.left, key, value)
        else:
            root.right = self._insert(root.right, key, value)

        root.height = 1 + max(self._height(root.left),
                              self._height(root.right))

        balance = self.get_balance_factor()
        if balance > 1 and key < root.left.get_key():
            root = self._right_rotate(root)
        elif balance < -1 and key > root.right.get_key():
            root = self._left_rotate(root)
        elif balance > 1 and key > root.left.get_key():
            root.left = self._left_rotate(root.left)
            root = self._right_rotate(root)
        elif balance < 1 and key < root.right.get_key():
            root.right = self._right_rotate(root.right)
            root = self._left_rotate(root)

        return root

    def insert_data(self, key, value) -> None:
        self.root = self._insert(self.root, key, value)

    def _left_rotate(self, root) -> AVLNode:
        """Left rotation of the tree

        Args:
            root (AVLNode): the node from which rotation should be done

        Returns:
            AVLNode: new root after rotation
        """
        rright = root.right
        rrleft = rright.left

        rright.left = root
        root.right = rrleft

        root.height = 1 + max(self._height(root.left),
                              self._height(root.right))
        rright.height = 1 + max(self._height(rright.left),
                                self._height(rright.right))

        return rright

    def _right_rotate(self, root) -> AVLNode:
        """right rotation of tree

        Args:
            root (AVLNode): the node from which rotation should be done

        Returns:
            AVLNode: new root after rotation
        """
        rleft = root.left
        rrright = rleft.right

        rleft.right = root
        root.left = rrright

        root.height = 1 + max(self._height(root.left),
                              self._height(root.right))
        rleft.height = 1 + max(self._height(rleft.left),
                               self._height(rleft.right))

        return rleft
