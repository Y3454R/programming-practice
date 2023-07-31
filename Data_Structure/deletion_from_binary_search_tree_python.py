class bst_node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data is None:
            self.data = data
        if self.data == data:
            return
        if self.data > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bst_node(data)
        if self.data < data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bst_node(data)

    def in_order(self):
        elements = []
        if self.left:
            elements += self.left.in_order()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order()
        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

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


if __name__ == "__main__":
    input_list = [15, 12, 7, 14, 27, 20, 23, 88]
    bst = bst_node()
    for inp in input_list:
        bst.add_child(inp)
    print(bst.in_order())
    # print(bst.find_min())
    while True:
        try:
            x = int(input())
            bst.erase(x)
            print(bst.in_order())
        except:
            print("invalid!")
            break
