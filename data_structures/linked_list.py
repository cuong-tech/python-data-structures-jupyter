"""Module for Linked List implementation."""

class ListNode:
    """Class for Doubly-Linked List Node."""
    def __init__(self, val=None, is_head=False, is_tail=False):
        """Initialize here."""
        self.val = val
        self.next = None
        self.prev = None
        self.is_head = is_head
        self.is_tail = is_tail

    def __repr__(self):
        """Make print look more comprehensive."""
        if self.is_tail:
            return "Tail"

        if self.is_head:
            node = "Head"

        else:
            node = f"ListNode({self.val})"

        return f"{node} <-> {self.next}"


class DoublyLinkedList:
    """Class for a Doubly-Linked List."""
    def __init__(self):
        """Initialize here."""
        self.head = ListNode(is_head=True)
        self.tail = ListNode(is_tail=True)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if 0 <= index < self.length:
            dummy = self.head.next

            for _ in range(index):
                dummy = dummy.next

            return dummy.val

        return -1

    def add_at_head(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the
        first node of the linked list.
        """
        self.add_at_index(0, val)

    def add_at_tail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.add_at_index(self.length, val)

    def add_at_index(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        If index is negative, the node will be inserted at head.
        """

        if 0 <= index <= self.length:
            new_node = ListNode(val)
            dummy = self.head

            for _ in range(index):
                dummy = dummy.next

            next_node = dummy.next
            next_node.prev, new_node.next = new_node, next_node
            dummy.next, new_node.prev = new_node, dummy

            self.length += 1

        elif index < 0:
            self.add_at_index(0, val)

    def delete_at_index(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self.length:
            dummy = self.head.next

            for _ in range(index):
                dummy = dummy.next

            dummy.prev.next, dummy.next.prev = dummy.next, dummy.prev

            self.length -= 1

    def __repr__(self):
        return repr(self.head)
