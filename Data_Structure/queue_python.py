class queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        if not self.q:
            return True
        return False

    # enqueue function
    def enq(self, item):
        self.q.append(item)

    # dequeue function
    def dq(self):
        if self.is_empty():
            print("queue is empty")
            return
        return self.q.pop(0)

    # front function
    def frnt(self):
        if self.is_empty():
            print("queue is empty")
            return
        return self.q[0]

    # rear function
    def rr(self):
        if self.is_empty():
            print("queue is empty")
            return
        l = len(self.q)
        return self.q[l - 1]

    # for print
    def display(self):
        for element in self.q:
            print(element, end=" ")
        print()


if __name__ == '__main__':
    qu = queue()
    print(qu.is_empty())

    qu.enq(2)
    qu.enq(34)
    qu.enq(343)
    qu.enq(99)

    qu.display()
    print(qu.dq())
    qu.display()

    print(f"first element: {qu.frnt()} and last element: {qu.rr()}")
