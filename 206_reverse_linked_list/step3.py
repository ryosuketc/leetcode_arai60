# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Stack - memory limite exceeded!
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        node = head

        while node is not None:
            original_next_node = node.next
            node.next = previous
            previous = node
            node = original_next_node

        return previous
