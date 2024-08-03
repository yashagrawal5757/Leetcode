# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #single element in list
        if (head.next  is None):
            return 

        # Find middle of list
        slow,fast = head, head
        while(fast!=None and fast.next!= None):
            breaknode = slow
            slow = slow.next
            fast = fast.next.next

        #To break linked list into two
        
        mid,current = slow,slow.next
        mid.next = None
        prev  = None
        #Reverse link list logic
        while(current!=None):
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode

        #merge two lists inplace
        first, second = head, prev
        while(first!=None and second!=None):
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        return first   
            
                