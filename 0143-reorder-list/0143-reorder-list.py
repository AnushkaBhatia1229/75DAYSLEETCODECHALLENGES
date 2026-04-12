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
        if not head:
            return
        
        q = deque()
        node = head
        
        # Store all nodes except head into deque
        while True:
            node = node.next
            if not node:
                break
            q.append(node)
        
        node = head
        
        # Reorder using deque
        while q:
            node.next = q.pop()
            node = node.next
            
            if not q:
                break
            
            node.next = q.popleft()
            node = node.next
        
        node.next = None
        