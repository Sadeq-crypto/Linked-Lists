class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)


    def get_data(self):
        """Return the self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """Replace the existing self.data attribute with new.data parameter"""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing self.next attribute with new.next parameter"""
        self.next = new_next

    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing self.previous attribute with new.previous parameter"""
        self.previous = new_previous


class DLL():
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<DLL object: head=>".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Traverses  the linked list and returns an integer value representing
        the number of nodes in the linked list.

        the Time complexity is O(n) becuase every node in the linked list must
        be visited in order to calculate the size.
        """
        size = 0
        if self.head == 0:
            return 0
        current = self.head
        while current is not None:
            size += 1
            current = currnt.get_next()
        return size

    def search(self, data):
        """
        Traverses the linked list and returns True if the data searched for is
        present in one of the nodes. otherwise it returns False

        the time complexity is O(n)
        """
        if self.head is None:
            return "The Linked List is empty. No nodes to find"
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False


    def add_front(self, data):
        """
        add a data whose node is the new data argument to the front of the
        linked list
        """
        temp = DLLNode(data)
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(temp)
        self.head = temp


    def remove(self, data):
        """
        Removes the first occurence of a node that contains the data argument as
        its self.data attribute. Returns Nothing.

        The time complexity is O(n) because in the worst case, we have to visit
        every node before finding the one we wamt to remove.
        """
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "A Node with that data value is not present"
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())
