# 리펙토링
# 불필요한 주석 정리
# position 논리 개선
# 경계 조건 검사
# Tail 삭제 예외 처리
# 삭제할 노드의 메모리 해제
# 불필요한 예외 처리 제거


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

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

        new_node.next = current.next
        current.next = new_node

    def delete(self, position):
        if position == 0:
            if self.head is None:
                raise ValueError("list is empty")
            self.head = self.head.next
            return

        current = self.head
        for i in range(position - 1):
            if current is None or current.next is None:
                raise ValueError("Index Error")
            current = current.next

        current.next = current.next.next


linkedList = LinkedList()
linkedList.append("연결")
linkedList.append("리스트")
linkedList.append("리스트")
linkedList.append("실습")
linkedList.insert("중임돠", 4)
linkedList.delete(2)
linkedList.print_list()