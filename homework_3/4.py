class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def insert(self, index, data):
        if index < 0:
            raise ValueError("Index cannot be negative.")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        count = 0

        while current_node and count < index - 1:
            current_node = current_node.next
            count += 1

        if current_node is None:
            raise IndexError("Index out of range.")

        new_node.next = current_node.next
        current_node.next = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def update(self, old_data, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == old_data:
                current_node.data = new_data
                return
            current_node = current_node.next

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def display(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next
        print("Linked List:", " -> ".join(map(str, nodes)))


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display()

linked_list.insert(1, 4)

linked_list.display()

linked_list.delete(2)

linked_list.display()

linked_list.update(4, 5)

linked_list.display()

print(linked_list.search(5))
print(linked_list.search(2))
