class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_last(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def get_length(self):
        cnt = 0
        itr = self.head
        while itr:
            cnt += 1
            itr = itr.next
        return cnt

    def insert_at_pos(self, pos, data):
        if pos > self.get_length() or pos < 0:
            print("out of range!")
            return
        elif pos == self.get_length():
            self.insert_at_last(data)
            return
        if pos == 0:
            self.insert_at_first(data)
            return

        cnt = -1
        itr = self.head
        prev = None
        while itr:
            cnt += 1
            if(cnt == pos):
                break
            prev = itr
            itr = itr.next
        node = Node(data)
        node.next = prev.next
        prev.next = node

    def delete_at(self, pos):
        if self.get_length() <= pos or pos < 0:
            print("out of range!")
            return
        if (pos == 0):
            itr = self.head
            if itr.next is None:
                self.head = None
            else:
                self.head = itr.next
            return
        cnt = -1
        itr = self.head
        prev = None
        while itr:
            cnt += 1
            if(cnt == pos):
                break
            prev = itr
            itr = itr.next
        prev.next = itr.next



    def display(self):
        if self.head == None:
            print("empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " -> "
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_first(4)
    ll.insert_at_first(34)
    ll.insert_at_last(99)
    ll.insert_at_pos(0, 4)
    ll.insert_at_pos(ll.get_length(), 999)
    print(ll.get_length())
    ll.display()
    ll.insert_at_pos(2, 343)
    ll.delete_at(0)
    ll.delete_at(ll.get_length() - 1)
    print(ll.get_length())
    ll.display()