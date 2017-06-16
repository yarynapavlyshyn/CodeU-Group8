class BinaryTree:

    def __init__(self, rootKey = None):
        """
        Tree initialization with the (optional) value of the root. Allows the same values in different nodes.
        :param rootKey: any
        :return: None
        """
        self.root = None
        self.size = 0
        self._half_leaves = [] # the nodes with less than two children
        self._nodes = []
        if rootKey is not None:
            self.root = Node(rootKey)
            self.root.level = 1
            self.size = 1

    def set_root(self, key):
        """
        If there is no root adds a root node with the given value and set the previous root (if exists) as its left child.
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
        self._preorder(self.root)
        return self._nodes

    def _preorder(self, node):
        """
        Recursive preorder traversal of the tree. Save all the nodes in the tree in self._nodes list. Used to refresh the self._nodes list in nodes() method.
        :param node: Node
        :return: None
        """
        if node is None:
            return None
        self._nodes.append(node)
        self._preorder(node.left)
        self._preorder(node.right)

    def half_leaves(self):
        """
        Refresh the self._half_leaves.
        :return: list(Node)
        """
        self._half_leaves = []
        self._finding_half_leaves(self.root)
        return self._half_leaves

    def _finding_half_leaves(self, node):
        """
        Save all the nodes that has not both children in self._half_leaves. Used to refresh the self._nodes list in half_leaves method().
        :param node: Node
        :return: None
        """
        if node is None:
            return None
        if node.left is None or node.right is None: self._half_leaves.append(node)
        self._finding_half_leaves(node.left)
        self._finding_half_leaves(node.right)

    def add(self, value, parent = None):
        """
        Add a Node with the given value as a right child of not none parent if not exists else as a left child.
        If parent is None find the the highest node that has less than children.
        :param value: any
        :return: None
        """
        if self.root is None:
            self.set_root(value)
            return
        if parent is None:
            half_leaves = self.half_leaves()
            parent = [leaf for leaf in half_leaves if leaf.level == min([l.level for l in half_leaves])][0]
            # we just add as a child to the first node in self._half_leaves with the lowest level
        if parent.left is None:
            parent.left = Node(value, parent)
        elif parent.right is None:
            parent.right = Node(value, parent)

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

    def insert(self, key, parent_key):
        """
        Insert the new Node with the given value in the tree as a left child of the node with the parent_key value if exists. Returns KeyError otherwise.
        If the parent has already its left child we set this child as a left child of the inserted node.
        :param key: any
        :param parent_key: any
        :return: None
        """
        future_parent = self.find(parent_key)
        if future_parent is None:
            raise KeyError("the root already exists")
        # else
        newNode = Node(key, future_parent)
        newNode.left = future_parent.left

    def delete(self, key):
        """
        Delete the element in the tree with the given key and return deleted node.
        :param key: any
        :return: Node
        """
        node = self.find(key)
        if node is None:
            raise KeyError("there is no node with such a key")

        parent = node.parent

        if parent is not None:
            if parent.left is None or parent.right is None: # the parent has only one child - the node
                parent.left, parent.right = node.left, node.right
                node.left.parent, node.right.parent = parent, parent

            elif not (node.left and node.right): # if node has only one child
                branch_root = node.left or node.right # it will be left or right branch of node, one that exists
                branch_root.parent = parent
                if parent.left == node:
                    parent.left = branch_root
                else:
                    parent.right = branch_root

            # if both parent and node have two children
            elif parent.left == node:
                parent.left = node.left # insert tree as a left child
                parent.left.parent = parent
                self.add_tree(node.right) # add all other values separately

            else: # parent.right == node
                parent.right = node.right
                parent.right.parent = parent
                self.add_tree(node.left)
                
        self.size -= 1

        return node

    def add_tree(self, root):
        """
        Recursive function to add all the values in the give tree to self.
        :param tree: Tree
        :return: None
        """
        if root == None:
            return
        self.add(root.key)
        self.add_tree(root.left)
        self.add_tree(root.right)

    def if_exists(self, key):
        """
        Returns true if there is at least one element with such a key, false otherwise.
        :param key: any
        :return: bool
        """
        if self.find(key) is None:
            return False
        return True
    
    def __str__(self):
        """
        For simple string representation of Tree.
        :return: str
        """
        node = self.root
        str_to_return = self.__repr__(node)
        return str_to_return

    def __repr__(self, node):
        """
        Recursive helper function for __str__() method.
        :param node: Node
        :return: str
        """
        if node is None: return ""

        ret = "\t" * (node.level - 1) + str(node.key) + "\n"
        ret += self.__repr__(node.right)
        ret += self.__repr__(node.left)
        return ret

class Node:
    def __init__(self, key, parent = None, right = None, left = None): # key is obvious
        """
        Node initialization with obvious key value and optional parent, right, left Nodes.
        :param key: any
        :param parent, right, left: Node
        :return: None
        """
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.level = None
        if parent is not None and parent.level:
            self.level = parent.level + 1

    def __str__(self):
        """
        String representation of Node. Returns
        :return: str
        """
        return str(self.key)
