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
            tmp_node = q.pop(0)

            if tmp_node.left:
                q.append(tmp_node.left)
            else:
                tmp_node.left = bt_node(data)
                return

            if tmp_node.right:
                q.append(tmp_node.right)
            else:
                tmp_node.right = bt_node(data)
                return

    def bfs(self):
        elements = []
        q = []
        q.append(self)

        while q:
            tmp_node = q.pop(0)
            elements.append(tmp_node.data)

            if tmp_node.left:
                q.append(tmp_node.left)

            if tmp_node.right:
                q.append(tmp_node.right)

        return elements


if __name__ == "__main__":
    input_list = [15, 7, 3, 1, 2, 4, None, 5]
    bt = bt_node()
    for inp in input_list:
        bt.add_child(inp)
    print(bt.bfs())
