# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_set = set()
        nodes_without_duplicates = []

        node = head
        while node is not None:
            if node.val not in nodes_set:
                nodes_without_duplicates.append(node)
            nodes_set.add(node.val)
            node = node.next

        for i in range(1, len(nodes_without_duplicates)):
            nodes_without_duplicates[i - 1].next = nodes_without_duplicates[i]
        if nodes_without_duplicates:
            nodes_without_duplicates[-1].next = None
        return head
