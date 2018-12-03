from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def append(self, value):
        new_node: Node = Node(value)

        if self.tail is None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        if self.head is None:
            self.head = new_node

    def remove(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next  # move head
            return

        # look through rest of the nodes
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next #  unlink the next node by skipping it
                return
            current_node = current_node.next

    def find(self, value):
        if self.head is None:
            return None

        if self.head.value == value:
            return self.head.value  # think about what this means. i.e we search for a given object byb its key?

        # look through rest of the nodes
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                return current_node.next
            current_node = current_node.next

    def print_nodes(self):
        if self.head is None:
            print("List is empty!")
            return

        current_node = self.head
        while current_node is not None:
            print(current_node)
            current_node = current_node.next
