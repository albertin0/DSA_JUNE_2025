# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None    # type: ignore

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        first_iteration = True
        while fast and fast.next and (first_iteration or fast != slow):
        # while fast and fast.next and fast != slow: # type: ignore
            slow = slow.next # type: ignore
            fast = fast.next.next # type: ignore
            first_iteration = False
        
        if not fast or not fast.next:
            return False        
        
        return True
    
s = Solution()
# Example usage:
# Creating a linked list with a cycle for testing
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2 # type: ignore
node2.next = node3 # type: ignore
node3.next = node4 # type: ignore
node4.next = node2 # type: ignore
  # Creating a cycle here
print(s.hasCycle(node1))  # Output: True, since there is a cycle in the linked list

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2 # type: ignore
node2.next = None # type: ignore
print(s.hasCycle(node1))  # Output: False, since there is no cycle in the linked list
