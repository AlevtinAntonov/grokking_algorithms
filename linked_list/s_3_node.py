class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None
        # self.previousNode = None

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None

    def find_node(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next_node
        return None

    def add_to_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def add_to_node(self, value, previous_node):
        new_node = Node(value)
        previous_node = self.find_node(previous_node)
        if previous_node is None:
            self.add_to_end(value)
            return
        last_node = previous_node.next_node
        previous_node.next_node = new_node
        new_node.next_node = last_node

    def print_linked_list(self):
        node = self.head
        if node is None:
            return "LinkedList is Empty"
        result = ""
        while node:
            result += f"{node.__str__()}" + " "
            node = node.next_node
        return result

    def del_head(self):
        if self.head:
            self.head = self.head.next_node
        # elif self.head.next_node
        else:
            raise Exception("LinkedList is Empty")

    def del_end(self):
        node = self.head
        if node is None or node.next_node is None:
            self.head = None
            return
        old_node = None
        while node.next_node:
            old_node = node
            node = node.next_node
        old_node.next_node = None

    def reverse_lst(self, head):

        current = head
        new_head = None

        while current:
            node = Node(current.value)

            # Assign the new head to node's next
            node.next_node = new_head

            # Assign the node to new head
            new_head = node
            current = current.next_node

        return new_head


a = LinkedList()
a.add_to_end(12)
a.add_to_end(24)
a.add_to_end(36)
print(a.print_linked_list())
# a.reverse_lst()
print(a.reverse_lst(a.head))
# a.add_to_node(26, 24)
# print(a.print_linked_list())
# a.del_end()
# print(a.print_linked_list())
# a.del_end()
# print(a.print_linked_list())
# a.del_end()
# print(a.print_linked_list())
# a.del_end()
# print(a.print_linked_list())
# a.del_end()
# print(a.print_linked_list())
# print(a.print_linked_list())
# a.del_head()
# print(a.print_linked_list())
# a.del_head()
# print(a.print_linked_list())
