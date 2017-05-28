from Tree import BinaryTree

def find_ancestors(tree, key):
    """
    Find ancestors of the first node with the given value while preorder traversal and save the Nodes in a list that return.
    :param tree: Tree
    :param key: any
    :return: list(Nodes)
    """
    node = tree.find(key)
    if node:
        parent = node.parent
        if parent is None:
            return []
        ancestors = [parent]
        while parent.parent is not None:
            ancestors.append(parent.parent)
            parent = parent.parent
        return ancestors

def ancestors_by_keys(tree, key):
    """
    Advansed version of find_ancestors function that instead of Nodes in list contains their keys.
    :param tree: Tree
    :param key: Key
    :return: list(*)
    * - any type
    """
    ancestors = find_ancestors(tree, key)
    if ancestors:
        return [n.key for n in ancestors]

def process():
    """
    The function to process the ancestors_by_keys function.
    Asks for the input in consile to form a list and then the value to find ancestors for.
    :return:
    """
    elements_for_tree = input("Print the values separated by the TWO whitespaces: ").split("  ")
    T = BinaryTree()
    for e in elements_for_tree:
        T.add(e)
    element = input("an element you want to get ancestors of: ")
    print(ancestors_by_keys(T, element))
