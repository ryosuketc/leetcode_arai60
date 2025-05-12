# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_visited = set()
        cur = head
        while cur is not None:
            if cur in nodes_visited:
                return cur
            nodes_visited.add(cur)
            cur = cur.next
