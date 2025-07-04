# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None, head)
        last_non_duplicate_node = dummy_head
        node = head

        while node is not None and node.next is not None:
            if node.val != node.next.val:
                node = node.next
                last_non_duplicate_node = last_non_duplicate_node.next
            else:
                while node.next is not None and node.val == node.next.val:
                    node = node.next
                last_non_duplicate_node.next = node.next
                node = node.next

        return dummy_head.next