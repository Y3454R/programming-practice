class bst_node:
    def __init__(self, data=None):
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

    def pre_order_traversal(self):

        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):

        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

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

    def calculate_sum(self):
        sum = 0

        if self.left:
            sum += self.left.calculate_sum()

        sum += self.data

        if self.right:
            sum += self.right.calculate_sum()

        return sum

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def erase(self, val):
        if val > self.data:
            if self.right:
                self.right = self.right.erase(val)
            else:
                print("Not found!")
        elif val < self.data:
            if self.left:
                self.left = self.left.erase(val)
            else:
                print("Not found!")
        else:
            if (self.left is None and self.right is None):
                return None
            elif (self.left is None):
                return self.right
            elif (self.right is None):
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.erase(min_val)
        return self


if __name__ == '__main__':

    number_of_input = int(input("Enter the number of elements: "))
    input_list = list(map(int, input("Enter the elements: ").split()))

    # input_list = [15, 12, 7, 14, 27, 20, 23, 88]

    bst = bst_node()

    for inp in input_list:
        bst.add_child(inp)

    print(f"In-order: {bst.in_order_traversal()}")
    print(f"Pre-order: {bst.pre_order_traversal()}")
    print(f"Post-order: {bst.post_order_traversal()}")

    print(
        f"Minimum element is {bst.find_min()} and maximum element is {bst.find_max()}\nThe sum is {bst.calculate_sum()}")

    # print(bst.data)

    while (True):
        try:
            to_find = int(input("Search for: "))
            found = bst.bst_search(to_find)
            print(found)
            if found == True:
                str_input = str(input(f"to delete {to_find}, enter \"y\": "))
                if str_input == "y":
                    bst.erase(to_find)
                print(f"In-order: {bst.in_order_traversal()}")
        except ValueError:
            print("invalid input!")
            break

    # n = 8
    # input list: 15 12 7 14 27 20 23 88
    # post-order: 7, 14, 12, 23, 20, 88, 27, 15
    # pre-order: 15, 12, 7, 14, 27, 20, 23, 88
