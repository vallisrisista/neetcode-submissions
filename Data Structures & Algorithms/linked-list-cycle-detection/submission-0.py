# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        links=set()
        while current is not None:
            print(current.val)
            if current.next not in links:
                links.add(current.next)
            else:
                return True
            current=current.next
        return False
        