# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False # One node without any cycle.
        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow, fast = slow.next, fast.next.next
        return True
