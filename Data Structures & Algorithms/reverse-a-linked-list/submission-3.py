# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative
        prev = None
        curr = head

        # while curr exists
        while curr:
            tmp = curr.next # save the next node
            curr.next = prev # reverse the pointer
            prev = curr # move prev to curr
            curr = tmp # move curr to next (tmp)

        # prev is now the head of the linked list
        return prev


        
   







       


        