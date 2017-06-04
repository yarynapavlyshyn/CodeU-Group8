from Q1 import find_ancestors, ancestors_by_keys
from Tree import BinaryTree, Node

def lowest_common_ancestor(tree, key1, key2):
    """
    Returns the lowest common ancestor of  two nodes with given keys. Return None
    in case of any invalid situation (if at least one of the nodes doesn`t exists).
    :param tree: Tree
    :param key1: any
    :param key2: any
    :return: Node
    """
    ancestors1 = find_ancestors(tree, key1)
    ancestors2 = find_ancestors(tree, key2)
    if ancestors1 is None or ancestors2 is None: return None
    return last_common_element(ancestors1, ancestors2)

def last_common_element(list1, list2):
    """
    Find the last from the end common element in two lists. In our case it`s lists of nodes.
    :param list1: list(*)
    :param list2: list(*)
    :return: *
    """
    # Here is fixed first version just not to live it wrong, but the new one below is simpler
    """
    max_i = min(len(list1), len(list2))
    if not max_i:return
    for i in range(max_i):
        if list1[-i-1] != list2[-i-1]:
            return list1[-i]
    return list1[- max_i]
    """
    
    max_i = min(len(list1), len(list2))
    if not max_i: return   
    i = 1
    while list1[-i] == list2[-i] and i < max_i:
        i += 1
    return list1[-i]

def process_and_print_out_LCA():
    elements_for_tree = input("Print the values separated by the TWO whitespaces: ").split("  ")
    T = BinaryTree()
    element1, element2 = input("two elements you want to consider separated by the TWO whitespaces: ").split("  ")
    for e in elements_for_tree:
        T.add(e)
    print(lowest_common_ancestor(T, element1, element2))
