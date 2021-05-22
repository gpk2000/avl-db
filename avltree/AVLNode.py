class NoNodeData(Exception):
    pass


class AVLNode(object):

    def __init__(self, key=None, value=None) -> None:
        """Initializes the AVL Node.

        Args:
            data (dict, optional): {Key:Value} pair. Defaults to None.
        """
        super().__init__()
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self) -> str:
        """Prints single AVL Node to stdout

        Raises:
            NoNodeData: If no data is present in the node

        Returns:
            str: output string
        """
        if self.key:
            out = "data: {0}\nleft: {1}\nright: {2}\n".format(
                (self.key, self.value), self.left.__str__(), self.right.__str__())
            return out
        raise NoNodeData

    def get_key(self) -> str:
        """returns the key of the node

        Returns:
            str: the key in (key, value) pair
        """
        return self.key

    def get_value(self) -> str:
        """returns the value of the key

        Returns:
            str: the value in (key, value) pair
        """
        return self.value
