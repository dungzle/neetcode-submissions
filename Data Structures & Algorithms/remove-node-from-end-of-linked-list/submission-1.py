# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        if n == count:
            return head.next
        i = 0
        curr = head
        prev = head
        while i < count - n:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = curr.next
        return head
