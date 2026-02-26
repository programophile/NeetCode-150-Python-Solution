# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer=head
        fast_pointer=head
        while fast_pointer:
            try:
                slow_pointer=slow_pointer.next
                fast_pointer=fast_pointer.next.next
                if slow_pointer==fast_pointer:
                    return True
            except:
                return False
        return False
        
