# 더블 링크드 리스트 실습


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            current.next.prev = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def print_prev(self, position):
        if position == 0:
            print("존재하지 않습니다.")
        else:
            current = self.head
            for i in range(position):
                current = current.next
                if current is None:
                    raise ValueError("Index Error")
                print(current.prev.data)
                return

    def insert(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Index Error")
            current = current.next

        if not current:
            raise ValueError("Index Error")
        if current.next is not None:
            new_node.next = current.next
            current.next.prev = new_node
        new_node.prev = current
        current.next = new_node

    def delete(self, position):
        if position == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        current = self.head
        for i in range(position - 1):
            current = current.next
            if current is None or current.next is None:
                raise ValueError("Index Error")

        if current.next and current.next.next is not None:
            current.next = current.next.next
            current.next.prev = current
        if current.next is None:
            current.next = None
            return
        elif current.next.next is None:
            current.next = None
            return


linkedList = LinkedList()
linkedList.append("연결")
linkedList.append("리스트")
linkedList.append("실습")
linkedList.print_prev(2)
linkedList.delete(2)
linkedList.print_list()