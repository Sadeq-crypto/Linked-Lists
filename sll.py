class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)


    def get_data(self):
        """
        Return the self.data attribute
        """
        return self.data

    def set_data(self, new_data):
        """
        Replace the existing self.data attribute with new.data parameter
        """
        self.data = new_data

    def get_next(self):
        """
        Return the self.next attribute
        """
        return self.next

    def set_next(self, new_next):
        """
        Replace the existing self.next attribute with new.next parameter
        """
        self.next = new_next

class SLL:
    def __init__(self):
        self.head = None

    def __repr(self):
        return "SLL object = head{}".format(self.head)

    def is_empty(self):
        """
        it return True if the list is empty. otherwise, it return False
        """
        return self.head is None

    def add_front(self, new_data):
        """
        add a data whose node is the new data argument to the front of the
        linked list
        """
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp



    def size(self):
        """
        Traverses  the linked list and returns an integer value representing
        the number of nodes in the linked list.

        the Time complexity is O(n) becuase every node in the linked list must
        be visited in order to calculate the size.
        """
        size = 0
        if self.head is None:
            return 0
        current = self.head
        while current is not None: #While there are still Nodes to count
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """
        Traverses the linked list and returns True if the data searched for is
        present in one of the nodes. otherwise it returns False

        the time complexity is O(n)
        """
        if self.head is None:
            return "Linked list is empty, no nodes were found"

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()

        return False

    def remove(self, data):
        """
        Removes the first occurence of a node that contains the data argument as
        its self.data variable. Returns nothing.

        Time complexity is O(n). becuase in the worst case we have to visit
        every node before we find the one we need to remove.
        """
        if self.head is None:
            return "Linked list is empty. No nodes to remove"

        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "A node with that data value is not present"
                else:
                    previous = current
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
