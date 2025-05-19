# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Stack - memory limite exceeded!
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListHelper(node: Optional[ListNode]):
            if node is None:
                return None, None
            if node.next is None:
                return node, node
            node_next = node.next
            node.next = None
            head, tail = reverseListHelper(node_next)
            tail.next = node
            return head, node

        head, _ = reverseListHelper(head)
        return head
