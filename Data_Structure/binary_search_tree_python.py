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

    def bst_search(self, search_value):

        if self.data == search_value:
            return True

        if search_value < self.data:
            if self.left:
                return self.left.bst_search(search_value)
            else:
                return False

        if search_value > self.data:
            if self.right:
                return self.right.bst_search(search_value)
            else:
                return False

        return False

if __name__ == '__main__':

    number_of_input = int(input("Enter the number of elements: "))
    input_list = list(map(int, input("Enter the elements: ").split()))

    bst = bst_node()

    for inp in input_list:
        bst.add_child(inp)

    print(f"Sorted tree: {bst.in_order_traversal()}")
    # print(bst.data)

    while(1):
        try:
            to_find = int(input("Search for: "))
            print(bst.bst_search(to_find))
        except ValueError:
            print("invalid input!")
            break