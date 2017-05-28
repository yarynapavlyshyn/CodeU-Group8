
class BinaryTree:
    def __init__(self, rootKey = None):
        """
        Tree initialization with the (optional) value of the root.
        :param rootKey: any
        :return: None
        """
        self.root = None
        self.size = 0
        self._leaves = [] #here leaves mean nodes without at least on of the children
        self._nodes = []
        if rootKey is not None:
            self.root = Node(rootKey)
            self.root.level = 1
            self.size = 1

    def set_root(self, key):
        """
        If there is no root adds a root node with the given value and set the previous root as a left child of the new one.
        :param key: any
        :return: None
        """
        if self.root is None:
            self.root = Node(key)
            self.root.level = 1
            self.size = 1
        else:
            raise KeyError("the root already exists")

    def nodes(self):
        """
        Find all Nodes while preorder traversal and save it to the self._nodes.
        :return: list(Node)        
        """
        self._nodes = []
        self.preorder(self.root)
        return self._nodes

    def preorder(self, node):
        """
        Recursive preorder traversal of the tree.
        :param node: Node
        :return: None
        """
        if node is None:
            return None
        self._nodes.append(node)
        self.preorder(node.left)
        self.preorder(node.right)

    def leaves(self):
        """
        Refresh the self._leaves.
        :return: list(Node)
        """
        self._leaves = []
        self.preorderForFindingLeaves(self.root)
        return self._leaves

    def preorderForFindingLeaves(self, node):
        """
        Save all the nodes that has not both children in self._leaves (however it`s not leaves).
        :param node: Node
        :return: None
        """
        if node is None:
            return None
        if node.left is None or node.right is None: self._leaves.append(node)
        self.preorderForFindingLeaves(node.left)
        self.preorderForFindingLeaves(node.right)

    def add(self, value, parent = None):
        """
        Add a Node with the given value as a right child of not none parent if not exists else as a left child.
        If parent is None find the best way to attach it (the highest node that has not both of children).
        :param value: any
        :return: None
        """
        if self.root is None:
            self.set_root(value)
            return
        if parent is None:
            parent = [leaf for leaf in self.leaves() if leaf.level == min([l.level for l in self.leaves()])][0]
            # we just add as a child to the first leaf with the lowest level and don`t have one or two of children
        if parent.left is None:
            parent.left = Node(value, parent)
        elif parent.right is None:
            parent.right = Node(value, parent)
        else:
            newN = Node(value, parent)

    def find(self, key):
        """
        Return the first Node in the tree with the given value while preorder traversal.
        :param key: any
        :return: Node
        """
        # result = [n for n in self.nodes() if n.key == key] # also we can return a list of all the Nodes with such a value
        result = None
        for n in self.nodes():
            if n.key == key:
                result = n
        return result

class Node:
    def __init__(self, key, parent = None, right = None, left = None): # key is obvious
        """
        Node initialization with key value
        :param key: any
        :param parent, right, left: Node
        :return: None
        """
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.level = None
        if parent is not None:
            self.level = parent.level + 1

    def __str__(self):
        """
        String representation of Node
        :return: str
        """
        return str(self.key)
