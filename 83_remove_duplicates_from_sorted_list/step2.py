# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        node = head
        node_next = head.next

        while node is not None and node_next is not None:
            if node.val != node_next.val:
                node = node.next
            
            node_next = node_next.next    
            node.next = node_next
        return head