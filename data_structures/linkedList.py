class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def root(self):
        return self.head.get_data()

    def insert(self, data):  # O(1)
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def size(self):  # O(1)
        return self.count

    def countAll(self):
        current = self.head  # O(n)
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):  # O(n)
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
            if current is None:
                #raise ValueError("Data not in list")
                return None
        return current

    def delete(self, data):  # O(n)
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            # raise ValueError("Data not in list") # pythonic
            return None
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return data


newList = LinkedList()
newList.insert('marty')
newList.insert('zach')
newList.insert('john')
newList.insert('joel')

print(newList.root())
print(newList.size())

newList.delete('john')

print(newList.size())

newList.delete('joel')

print(newList.size())


# binary and hash tables implementations
# unit tests
