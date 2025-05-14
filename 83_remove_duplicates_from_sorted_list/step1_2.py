# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        node, next_node = head, head.next

        while node is not None and next_node is not None:
            if node.val == next_node.val:
                # Same node and thus skip.
                node.next = next_node.next
                next_node = next_node.next
                continue
            else:
                node = next_node
                next_node = next_node.next

        return head