# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # first attempt
        '''
        ptr1 = list1
        ptr2 = list2
        dummy = ListNode() # to avoid edge case of inserting into empty list
        tail = dummy
        
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                # attach smaller node to end of my linked list
                tail.next = ptr1
                # advance tail so it points to the newly added node
                tail = ptr1
                # advance pointer i took node from
                ptr1 = ptr1.next
            else ptr2.val < ptr1.val:
                tail.next = ptr2
                tail = ptr2
                ptr2 = ptr2.next
        if ptr1:
            tail.next = ptr1
        else:
            tail.next = ptr2
        return dummy.next
        '''

        # solution
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next





                

        