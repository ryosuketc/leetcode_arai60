# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow, fast, = slow.next, fast.next.next
            if slow == fast:
                return True
        
        return False