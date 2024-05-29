# Linked List 실습


# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 링크드 리스트 클래스 정의
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                # current.next 가 존재하지 않을 때 까지 next
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert(self, data, position):   # 새로운 노드를 리스트의 특정 위치에 삽입
        new_node = Node(data)   # 새 노드 생성
        if position == 0:   # 맨 앞에 삽입하는 경우
            new_node.next = self.head   # 새 노드의 다음 노드를 현재의 head 노드로 지정
            self.head = new_node    # 새 노드를 head 노드로 지정
        else:
            current = self.head
            for _ in range(position - 1):    # 삽입할 위치의 앞 노드를 찾는 루프
                if current:
                    current = current.next
                else:
                    raise IndexError("Index error")    # 인덱스 에러
            if current is None:
                raise IndexError("Index Error")
            new_node.next = current.next    # 새 노드의 다음 노드를 삽입 위치의 노드로 지정
            current.next = new_node    # 삽입 위치의 앞 노드의 다음 노드를 새 노드로 지정

    def delete(self, data):  # 주어진 값을 가진 노드를 리스트에서 삭제
        if self.head and self.head.data == data:     # 삭제할 노드가 head 노드인 경우
            self.head = self.head.next   # head 노드를 다음 노드로 지정
        else:
            current = self.head
            while current and current.next.data != data:     # 삭제할 노드를 찾는 루프
                current = current.next
            if current and current.next:     # 삭제할 노드를 찾은 경우
                current.next = current.next.next     # 삭제할 노드 앞의 노드의 다음 노드를 삭제할 노드의 다음 노드로 지정
            else:
                raise ValueError("삭제할 노드를 찾을 수 없음")


# 링크드 리스트 객체 생생 및 데이터추가
linked_list = LinkedList()
linked_list.append("I")
linked_list.append("M")
linked_list.append("E")
linked_list.append("U")

# 링크드 리스트 데이터 출력 I, M, E, U
linked_list.print_list()

linked_list.insert("K", 0)
linked_list.print_list()    # K, I, M, E, U

linked_list.insert("N", 2)
linked_list.print_list()    # K, I, N, M, E, U

linked_list.delete("N")
linked_list.print_list()    # K, I, M, E, U

linked_list.delete("E")
linked_list.print_list()    # K, I, M, U
