# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        sentinel = current_node = ListNode(None, None)

        carry = 0
        while node1 is not None and node2 is not None:
            # 10 進数の繰り上がりなので 10.
            new_val = (node1.val + node2.val + carry) % 10
            carry = (node1.val + node2.val + carry) // 10

            current_node.next = ListNode(new_val, None)
            current_node = current_node.next
            node1 = node1.next
            node2 = node2.next
        
        while node1 is not None:
            new_val = (node1.val + carry) % 10
            carry = (node1.val + carry) // 10

            current_node.next = ListNode(new_val, None)
            current_node = current_node.next
            node1 = node1.next

        while node2 is not None:
            new_val = (node2.val + carry) % 10
            carry = (node2.val + carry) // 10

            current_node.next = ListNode(new_val, None)
            current_node = current_node.next
            node2 = node2.next
        
        if carry == 1:
            current_node.next = ListNode(1, None)

        return sentinel.next

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        sentinel = current_node = ListNode(None, None)

        carry = 0
        while node1 is not None and node2 is not None:
            # 10 進数の繰り上がりなので 10.
            new_val = (node1.val + node2.val + carry) % 10
            carry = (node1.val + node2.val + carry) // 10

            current_node.next = ListNode(new_val, None)
            current_node = current_node.next
            node1 = node1.next
            node2 = node2.next
        
        node = node1 or node2 # Either one of the nodes which still has nodes.
        while node is not None:
            new_val = (node.val + carry) % 10
            carry = (node.val + carry) // 10

            current_node.next = ListNode(new_val, None)
            current_node = current_node.next
            node = node.next

        if carry == 1:
            current_node.next = ListNode(1, None)

        return sentinel.next
