class Solution:
    def insertAtEnd(self, head, x):
        new_node = Node(x)
        if head is None:
            return new_node
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        return head
