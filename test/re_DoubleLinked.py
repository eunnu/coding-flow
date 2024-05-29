# 더블 링크드 리스트 리팩토링
# delete 간소화
# print_prev 메소드 구현


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

    def print_prev_of(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    print(current.prev.data)
                else:
                    print("이전 노드가 없슴돠")
                return
            current = current.next
        print("데이터를 찾을 수 없습니다.")

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
            if not self.head:
                raise ValueError("List is empty")
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        current = self.head
        for i in range(position - 1):
            current = current.next
            if current is None:
                raise ValueError("Index Error")

        if not current.next:
            raise ValueError("불가능합니다.")
        elif current.next.next:
            current.next = current.next.next
            current.next.prev = current
        else:
            current.next = None


linkedList = LinkedList()
linkedList.append("연결")
linkedList.append("리스트")
linkedList.append("실습")
linkedList.print_prev_of("리스트")
linkedList.print_list()