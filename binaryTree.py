class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def get_val(self):
        return self.val

    def traverse_tree(self):
        # print from left to right
        if self.left: # get to the left
            self.left.traverse_tree()
        print(self.val) # print data
        if self.right: # then get to the right
            self.right.traverse_tree()

    def _has_children(self):
        return self.left and self.right

    def _has_child(self):
        return self.left or self.right

    def _get_child(self):
        if self.left:
            return self.left
        else:
            return self.right

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add_node(self.root, data)

    def _add_node(self, currentNode, data):
        if currentNode.val > data:
            if currentNode.left is None:
                currentNode.left = Node(data)
            else:
                self._add_node(currentNode.left, data)
        elif currentNode.val < data:
            if currentNode.right is None:
                currentNode.right = Node(data)
            else:
                self._add_node(currentNode.right, data)

    def get_root_val(self):
        return self.root.val

    def traverse_tree(self):
        return self.root.traverse_tree()

    def get_min(self):
        minNode = self._get_left_node(self.root)
        return minNode.val

    def get_max(self):
        maxNode = self._get_right_node(self.root)
        return maxNode.val

    def _get_left_node(self, currentNode):
        while currentNode.left:
            return self._get_left_node(currentNode.left)
        return currentNode

    def _get_left_node_parent(self, currentNode, parentNode):
        while currentNode.left:
            return self._get_left_node_parent(currentNode.left, currentNode)
        return parentNode

    def _get_right_node(self, currentNode):
        while currentNode.right:
            return self._get_right_node(currentNode.right)
        return currentNode

    # def searchBreadth(self, data):
    #     if self.data == data:
    #         return self

    def search_depth(self, data):
        return self._find_data(self.root, data)

    def _find_data(self, currentNode, data):
        if currentNode is None:
            return 'Not found'
        if currentNode.val == data:
            return currentNode
        elif currentNode.val > data:
            return self._find_data(currentNode.left, data)
        elif currentNode.val < data:
            return self._find_data(currentNode.right, data)

    def _find_parent(self, currentNode, data):
        if currentNode.left is None and currentNode.right is None:
            return None

        if hasattr(currentNode.left, 'val'):
            if currentNode.left.val == data:
                return currentNode
        if hasattr(currentNode.right, 'val'):
            if currentNode.right.val == data:
                return currentNode

        if currentNode.val > data:
            return self._find_parent(currentNode.left, data)
        elif currentNode.val < data:
            return self._find_parent(currentNode.right, data)


    # if no children, remove reference
    # if single child, replace child reference with grandchild reference
    # if two children, replace child value with right trees smallest grandchild value
    def _do_delete(self, node, parentNode):
        found = True

        if node._has_children():
            print(node.val, 'has grand children')
            smallNodeParent = self._get_left_node_parent(node.right, node)
            value = None
            if smallNodeParent.left is None and smallNodeParent.right is None:
                value = smallNodeParent.val
                # remove reference to the smallNode
                print('parent value', parentNode.val)
            elif smallNodeParent.left is None:
                print('smallest node in right tree', smallNodeParent.right.val)
                value = smallNodeParent.right.val
                smallNodeParent.right = None
            else:
                print('smallest node in right tree', smallNodeParent.left.val)
                value = smallNodeParent.left.val
                smallNodeParent.left = None
            node.val = value
        elif node._has_child():
            print('has single grandchild')
            grandChild = node._get_child()
            node = grandChild
        else:
            node = None

    def delete_data(self, data):
        parentNode = self._find_parent(self.root, data)
        found = False
        if parentNode is None:
            return '{} not found'.format(data)

        if hasattr(parentNode.left, 'val'):
            if parentNode.left.val == data:
                found = True
                self._do_delete(parentNode.left, parentNode)

        if hasattr(parentNode.right, 'val'):
            if parentNode.right.val == data:
                found = True
                self._do_delete(parentNode.right, parentNode)

        if found:
            return parentNode
        else:
            return None

tree = BinaryTree(20)

tree.insert(11)
tree.insert(25)
tree.insert(10)
tree.insert(30)
tree.insert(18)
tree.insert(19)
tree.insert(16)
tree.insert(15)
tree.insert(17)
tree.insert(5)
tree.insert(6)
tree.insert(27)

# print('root', tree.get_root_val())
# print('min', tree.get_min())
# print('max', tree.get_max())
# print('search', tree.search_depth(19).val)
# print('search', tree.search_depth(17))

# tree.traverse_tree()
# print('delete', tree.delete_data(30).val)
# print('delete', tree.delete_data(10).val)
print('delete child of', tree.delete_data(18).val)
tree.traverse_tree()

#### TREE STRUCTURE
#          20
#        /    \
#      11      25
#     /   \      \
#    10    18     30
#   /     /  \    /
#  5     16  19  27
#   \   /  \
#    6 15   17
