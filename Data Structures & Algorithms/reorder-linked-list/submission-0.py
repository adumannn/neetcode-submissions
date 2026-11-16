# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = slow.next
        slow.next = None

        if prev:
            prev.next = None
            
        l2 = self.reverse(l2)

        while l1 and l2:
            nxt1 = l1.next
            nxt2 = l2.next

            l1.next = l2
            l2.next = nxt1

            l1 = nxt1
            l2 = nxt2

    def reverse(self, lis):

        prev = None
        curr = lis

        while curr:
            nxtNode = curr.next
            curr.next = prev
            prev = curr
            curr = nxtNode

        return prev

