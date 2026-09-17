# EASY — Create a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node = Node("Alice")
print(node.data)
print(node.next)

# MEDIUM — Connect Two Nodes
class Node1:
    def __init__(self, name):
        self.name = name
        self.next = None

node1 = Node1("Alice")
node2 = Node1("Bob")
node1.next = node2
print(node1.next.name)

# DIFFICULT — Traverse Three Nodes:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node("Alice")
node2 = Node("Bob")
node3 = Node("Charlie")

node1.next = node2
node2.next = node3

current = node1

while current is not None:
    print(current.data)
    current = current.next