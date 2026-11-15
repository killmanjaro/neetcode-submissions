# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        dummy = ListNode()
        tail = dummy
        

        
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                # attach smaller node to end of my linked list
                tail.next = ptr1
                # advance tail so it points to the newly added node
                tail = ptr1
                # advance pointer i took node from
                ptr1 = ptr1.next
            elif ptr2.val < ptr1.val:
                tail.next = ptr2
                tail = ptr2
                ptr2 = ptr2.next
        if ptr1:
            tail.next = ptr1
        else:
            tail.next = ptr2
        return dummy.next




                

        