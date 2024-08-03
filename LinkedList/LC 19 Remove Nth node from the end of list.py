# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pass solution
        '''
        prev = None
        current = headh 
        i = 1
        len = 0
        #calculate length of list
        while(current!= None):
            len += 1
            current = current.next
        #logic

        current = head
        while(current != None):
            if (i == len-n+1):
                #if only 1 element:
                if head.next == None:
                    return None
                if i==1:
                    nextnode = current.next
                    current.next = None
                    head = nextnode
                    return head
                    
                nextnode = current.next
                prev.next = nextnode
                return head
            prev = current
            current = current.next
            i += 1
        '''
        #One pass soln
        #keep slow at head, fast at head + n. keep moving both by 1. When fast reaches None, slow is at req position
        slow, fast = head, head
        prev = None
        i = 0
        #First make fast reach n places ahead
        while(i<n):
            fast = fast.next
            i += 1
        #fast is n places ahead now
        while(fast!= None):
            prev = slow  #prev required for node deletion logic
            slow = slow.next
            fast = fast.next
        # Prev at 3, slow at 4, fast at none
        #slow is at element which needs to be deleted -  for all test cases
    
        #Edge case1: #single element in list
        if prev is None and slow.next is None: #Edge case1
            return None

        #Edge case2 - If  firstoverall element is to be removed
        if slow ==head:
            #Update head to slow's next node
            head = slow.next
            slow.next = None #delete node at slow
            return head
        # Else for all other cases follow below - just delete node at slow
        prev.next = slow.next

        return head
        

        