class min_heap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def print_heap(self):
        print("printing the current storage of the heap:")
        for i in range(0, self.size):
            print(f"{i} : {self.storage[i]}")

    def has_parent(self, index):
        if index > 0:
            return True
        return False

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_parent(self, index):
        return self.storage[self.get_parent_index(index)]

    def has_left(self, index):
        if self.get_left_index(index) < self.size:
            return True
        return False

    def get_left_index(self, index):
        return (2 * index) + 1

    def get_left_child(self, index):
        return self.storage[self.get_left_index(index)]

    def has_r8(self, index):
        if self.get_r8_index(index) < self.size:
            return True
        return False

    def get_r8_index(self, index):
        return (2 * index) + 2

    def get_r8_child(self, index):
        return self.storage[self.get_r8_index(index)]

    def is_full(self):
        if self.size == self.capacity:
            return True
        return False

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def insert(self, val):
        if self.is_full():
            raise Exception("Heap is full.")
        self.storage[self.size] = val
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_up(self, index):
        if self.has_parent(index) and self.get_parent(index) > self.storage[index]:
            self.swap(index, self.get_parent_index(index))
            self.heapify_up(self.get_parent_index(index))

    def poll(self):
        if self.size == 0:
            raise Exception("Heap is empty.")
        val = self.storage[0]
        self.swap(0, self.size - 1)
        self.size -= 1
        self.heapify_down(0)
        return val

    def heapify_down(self, index):

        if self.has_left(index):
            left_index = self.get_left_index(index)
            smaller_child_index = left_index

            if self.has_r8(index):
                r8_index = self.get_r8_index(index)
                if self.get_r8_child(index) < self.storage[smaller_child_index]:
                    smaller_child_index = r8_index

            if self.storage[index] > self.storage[smaller_child_index]:
                self.swap(index, smaller_child_index)
                index = smaller_child_index
                self.heapify_down(index)
            else:
                return


if __name__ == '__main__':
    myHeap = min_heap(7)
    myHeap.insert(5)
    myHeap.insert(20)
    myHeap.insert(10)
    myHeap.print_heap()
    myHeap.insert(0)
    myHeap.print_heap()
    myHeap.poll()
    myHeap.print_heap()
    myHeap.insert(30)
    myHeap.print_heap()
    print(myHeap.poll())
    myHeap.print_heap()
