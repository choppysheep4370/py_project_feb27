'''
Ex02-Linked.py
연결 리스트(Linked List)
    저장된 각 데이터가 (데이터)+(다음 데이터의 포인터)로 이루어진 것으로
    한 방향으로만 탐색 가능한 구조
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def init(data):
        global node1
        node1 = node(data)

    def insert(data):
        global node1
        global last_node

        new_node = node(data)
        current = node1
        if current.next is None:
            current.next = new_node
            last_mode = new_node
        else:
            last_node.next = new_node
            last_node = new_node


''' 
       new_node = Node(data)

        current = node1
        while current.next != None: # 마지막 노드
            current = current.next

        current.next = new_node
'''



    def print_list(): # 연결 리스트의 데이터를 출력한다.
        global node1
        node = node1
        while node:
            print(node.data)
            node = node.next
        print()



node1 = Node(7)
node2 = Node(3)
node3 = Node(9)
node4 = Node(1)
node5 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(id(node1.next))
print(id(node2))

# 실행코드

init(7)
insert(3)
insert(9)
insert(1)
insert(6)

print_list()
'''

결과

'''