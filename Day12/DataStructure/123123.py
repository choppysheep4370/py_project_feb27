class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.next
        self.next = new_node

    def print_list(self):
        node = self
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
node1 = Node(7)
node1.insert(3)
node1.insert(9)
node1.insert(1)
node1.insert(6)
node1.print_list()
