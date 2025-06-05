# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Stack - memory limite exceeded!
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next

        if len(nodes) == 1:
            return nodes.pop()

        reversed_node = new_head = nodes.pop()
        previous = None
        while nodes:
            previous = nodes.pop()
            reversed_node.next = previous
            reversed_node = previous
        previous.next = None

        return new_head


# pointer
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = None
        node = head
        while node is not None:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            # or
            # node.next, prev, node = prev, node, node.next
        
        return prev
