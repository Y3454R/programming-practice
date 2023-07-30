class bst_node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):

        if self.data is None:
            self.data = data
            return

        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bst_node(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bst_node(data)


    def in_order_traversal(self):

        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

if __name__ == '__main__':

    number_of_input = int(input("Enter the number of elements: "))
    input_list = list(map(int, input("Enter the elements: ").split()))

    bst = bst_node()

    for inp in input_list:
        bst.add_child(inp)

    print(bst.in_order_traversal())