# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # itertative approach
        #'''
        curr = head
        prev = None

        while curr: 
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
        #'''


        # recursive solution 
        '''
        # base case
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head # reversing link between next node and head
        head.next = None

        return newHead
        '''








       


        