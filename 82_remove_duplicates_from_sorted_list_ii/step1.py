# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = dummy

        while node is not None:
            next_node = node
            while next_node.next is not None and next_node.val == next_node.next.val:
                next_node = next_node.next
            node.next = next_node.next
            node = node.next
        
        return dummy.next


