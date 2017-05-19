class LinkedList:

    def __init__(self, el = None):
        """
        Linked List implementation with the value of head Node (optional)
        :param el: any type
        :return: None
        """
        self.head = Node(el) if el is not None else None
        self.size = 0 if el is None else 1

    def add(self, el):
        """
        Add a Node to the list as the first element.
        """
        newNode = Node(el, self.head)
        if self.head is None:
            self.head = newNode
            self.size = 1
        else:
            self.head = newNode
            self.size += 1

    def get(self, i):
        """
        Return the Node by the index i (starting from 0) or None if i is out of bounds
        :param valueToFind: any type
        :return: Node
        """
        if i > self.size: raise IndexError
        else:
            node = self.head
        for cursor in range(i):
            if node is None: return None
            node = node.next
        return node

    def delete(self, valueToDelete):
        """
        Delete the first Node with given value and return its index or -1 if not exists
        :param valueToDelete: any type
        :return: int, index if exists, -1 otherwise
        """
        return self.deleteByIndex(self.index(valueToDelete))

    def deleteByIndex(self, i):
        """
        Delete the first Node with given value and return its index or -1 if not exists
        :param valueToDelete: any type
        :return: int, index if exists, -1 otherwise
        """

        if i < 0 or i > self.size: #error
            raise IndexError

        elif i == 0 and self.size > 0: # delete the head that exists
            self.head = self.head.next

        else:
            nodeBefore = self.get(i-1)
            nodeBefore.next = nodeBefore.next.next if nodeBefore.next is not None else None

        self.size -= 1
        return i

    def index(self, valueToFind):
        """
        Return an index of the first element with the given value if exists, -1 otherwise
        :param valueToFind: any type
        :return: int
        """
        node = self.head
        i = 0
        while node is not None and node.value != valueToFind:
            i += 1
            node = node.next
        if node: return i
        return -1

    def find(self, valueToFind):
        """
        Return the first node with the given value if exists, None otherwise
        :param valueToFind: any type
        :return: Node
        """
        node = self.head
        while node is not None and node.value != valueToFind:
            node = node.next
        return node

    def __len__(self):
        return self.size

    def __str__(self):
        """
        String representation of LinkedList
        :return: str
        """
        strr = str(self.head)
        iterEls = self.head.next
        while iterEls is not None:
            strr += " --> " + str(iterEls)
            iterEls = iterEls.next
        return strr

class Node:

    def __init__(self, value, nextN = None):
        """ Node initialization with value and previous Node - nextN (optional)
        :param value: str
        :param nextN: Node
        :return: None
        """
        self.value = value
        self.next = nextN

    def __str__(self):
        """
        The string representation of the Node like "(<value>)".
        :return: str
        """
        return "(" + str(self.value) + ")"





def Q1(str1, str2):
    """
    Return True if the strings are permutations of each other. False otherwise.
    :param str1: str
    :param str2: str
    :return: boolean
    """
    if type(str1) == type(str2) == str and str1 and str2:
        return sorted(list(str1)) == sorted(list(str2))

def Q1_proccess():
    """
    Proccesses the Q1 function after asking for two strings and print the result
    :return: None
    """
    twoStr = []
    while len(twoStr) != 2:
        twoStr = input("Type two words separated by the empty space: ").split()
    s1, s2 = twoStr
    print("ARE PERMUTATIONS: " + str(Q1(s1,s2)))



def Q2(llist, k):
    """
    Find the k-th to last element of the given linked list
    :param llist: LinkedList
    :param k: int
    :return: Node
    """
    node = llist.head
    indexOfNessesaryEl = len(llist)-k-1
    for cursor in range(indexOfNessesaryEl): # because we start from the head
        if node is None: return None
        node = node.next
    return node

    # or we can just use the method of the LinkedList class
    # return llist.get(indexOfNessesaryEl)

def Q2_proccess():
    """
    Proccesses the Q2 function after asking to print elements from which list will be formed,
    then ask for the number k and print the k-th to last element.
    :return: None
    """
    lilist = LinkedList()
    elements = input("Elements of list separated by the empty space: ").split()
    for ele in elements:
        lilist.add(ele)
    print(lilist)

    k = int(input("k: "))
    while k >= len(lilist):
        k = int(input("k: "))
    print("The {}-th Node to the last: ".format(k), Q2(lilist,k))

Q1_proccess()
print()
Q2_proccess()