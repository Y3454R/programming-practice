class bt_node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self is None:
            self = bt_node(data)
            return
        if self.data is None:
            self.data = data
            return
        q = []
        q.append(self)
        while q:
            tmp = q[0]
            q.pop(0)

            if tmp.left:
                q.append(tmp.left)
            else:
                tmp.left = bt_node(data)
                # break
                return

            if tmp.right:
                q.append(tmp.right)
            else:
                tmp.right = bt_node(data)
                # break
                return

    def in_order(self):
        elements = []
        if self.left:
            elements += self.left.in_order()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order()
        return elements

    # def bfs(self):
    #     elements = []
    #     q = []
    #     vstd = []
    #     for


if __name__ == "__main__":
    input_list = [15, 7, 3, 1, 2]
    bt = bt_node()
    for inp in input_list:
        bt.add_child(inp)
    print(bt.in_order())
