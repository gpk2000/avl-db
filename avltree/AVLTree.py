from avltree.AVLNode import AVLNode

class KeyNotFoundError(Exception): pass


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

        balance = self._balance_factor(root)
        if balance > 1 and key < root.left.get_key():
            root = self._right_rotate(root)
        elif balance < -1 and key > root.right.get_key():
            root = self._left_rotate(root)
        elif balance > 1 and key > root.left.get_key():
            root.left = self._left_rotate(root.left)
            root = self._right_rotate(root)
        elif balance < -1 and key < root.right.get_key():
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

    def _delete(self, root, key):
        if not root:
            return root
        rkey = root.get_key()
        if key < rkey:
            root.left = self._delete(root.left, key)
        elif key > rkey:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._get_min_value_node(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self._delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self._height(root.left),
                              self._height(root.right))
        balance = self._balance_factor(root)

        if balance > 1 and self._balance_factor(root.left) >= 0:
            root = self._right_rotate(root)
        elif balance < -1 and self._balance_factor(root.right) <= 0:
            root = self._left_rotate(root)
        elif balance > 1 and self._balance_factor(root.left) < 0:
            root.left = self._left_rotate(root.left)
            root = self._right_rotate(root)
        elif balance < -1 and self._balance_factor(root.right) > 0:
            root.right = self._right_rotate(root.right)
            root = self._left_rotate(root)

        return root
    
    def _get_min_value_node(self, root):
        if not root and not root.left:
            return root
        return self._get_min_value_node(self, root.left)

    def delete_data(self, key):
        self.root = self._delete(self.root, key)

    def get_value(self, key):
        if not self.root:
            raise KeyNotFoundError
        val = self._get(self.root, key)
        if val: return val
        raise KeyNotFoundError
    
    def _get(self, root, key):
        if root.key == key:
            return root.value
        
        elif root.right and root.key < key:
            return self._get(root.right, key)
        elif root.left and root.key > key:
            return self._get(root.left, key)
    
    def is_empty(self):
        return not self.root
    
    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, root):
        while root.left:
            root = root.left
        return root
    
    def find_max(self):
        return self._find_max(self.root)
    
    def _find_max(self, root):
        while root.right:
            root = root.right
        return root
    
    def check_ordering(self):
        return self._check_ordering(self.root)
    

    def check_balanced(self):
        return self._check_balanced(self.root)
    
    def _check_balanced(self, root):
        if not root:
            return True
        
        lheight = self._height(root.left)
        rheight = self._height(root.right)

        lcheck = self._check_balanced(root.left)
        rcheck = self._check_balanced(root.right)
        currcheck = abs(lheight - rheight) < 2
        return lcheck and rcheck and currcheck