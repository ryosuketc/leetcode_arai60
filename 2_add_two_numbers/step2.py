# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    BASE_NUMBER = 10
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = l1, l2
        sentinel = current_node = ListNode(None, None)

        carry = 0
        while node1 is not None and node2 is not None:
            new_val = (node1.val + node2.val + carry) % self.BASE_NUMBER
            carry = (node1.val + node2.val + carry) // self.BASE_NUMBER

            current_node.next = ListNode(new_val, None)
            current_node = current_node.next
            node1, node2 = node1.next, node2.next
        
        remaining_node = node1 or node2
        while remaining_node is not None:
            new_val = (remaining_node.val + carry) % self.BASE_NUMBER
            carry = (remaining_node.val + carry) // self.BASE_NUMBER

            current_node.next = ListNode(new_val, None)
            current_node = current_node.next
            remaining_node = remaining_node.next
        
        if carry == 1:
            current_node.next = ListNode(1, None)
        
        return sentinel.next