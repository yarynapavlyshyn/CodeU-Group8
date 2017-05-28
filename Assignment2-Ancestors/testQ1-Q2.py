import unittest
from Q1 import ancestors_by_keys
from Q2 import lowest_common_ancestor
from Tree import BinaryTree

class Test_Q1_and_Q2(unittest.TestCase):
    """
    Tests for ancestors_by_keys() function in Q1, find_ancestors() function
    will be tested automaticaly as a part of the first one
    """
    def test_ancestors_by_keys_empty_tree(self):
        t = BinaryTree()
        self.assertIsNone(ancestors_by_keys(t, 6))

    def test_ancestors_by_keys_if_not_exists(self):
        t = BinaryTree()
        values = [1, 2, 3, "o", "k"]
        for value in values:
            t.add(value)
        self.assertIsNone(ancestors_by_keys(t, 5))

    def test_ancestors_by_keys_if_exists_int(self):
        t = BinaryTree()
        values = [1, 2, 3, "o","k"]
        for value in values:
            t.add(value)
        self.assertEqual([1], ancestors_by_keys(t, 3))

    def test_ancestors_by_keys_if_exists_str(self):
        t = BinaryTree()
        values = [1, 2, 3, "o", "k"]
        for value in values:
            t.add(value)
        self.assertEqual([2, 1], ancestors_by_keys(t, "o"))

    """
    Tests for lowest_common_ancestor() function in Q2
    """
    def test_lowest_common_ancestor_empty_tree(self):
        t = BinaryTree()
        self.assertIsNone(lowest_common_ancestor(t, 8, 6))

    def test_ancestors_by_keys_if_not_exists(self):
        t = BinaryTree()
        values = [1, 2, 3, "o", "k"]
        for value in values:
            t.add(value)
        self.assertIsNone(lowest_common_ancestor(t, "o", "z"))

    def test_ancestors_by_keys_if_exists_but_root(self):
        t = BinaryTree()
        values = [1, 2, 3, "o","k"]
        for value in values:
            t.add(value)
        self.assertIsNone(lowest_common_ancestor(t, 1, 3))

    def test_ancestors_by_keys_if_exists_str(self):
        t = BinaryTree()
        values = [1, 2, 3, "o", "k"]
        for value in values:
            t.add(value)
        self.assertEqual(2, lowest_common_ancestor(t, "o", "k").key)

if __name__ == '__main__':
    unittest.main()