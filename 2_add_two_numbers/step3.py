# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    _BASE_NUMBER = 10
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = l1, l2
        current_node = sentinel = ListNode()
        carry = 0

        while node1 is not None or node2 is not None or carry != 0:
            val1, val2 = self._get_val(node1), self._get_val(node2)
            total = val1 + val2 + carry
            new_val = total % self._BASE_NUMBER
            carry = total // self._BASE_NUMBER

            current_node.next = ListNode(new_val)
            
            current_node = current_node.next
            node1 = self._get_next(node1)
            node2 = self._get_next(node2)
        
        return sentinel.next

    def _get_val(self, node):
        return node.val if node is not None else 0
    
    def _get_next(self, node):
        return node.next if node is not None else None