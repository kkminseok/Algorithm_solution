**python**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = head
        def solve(root):
            if root : 
                if root.next != None and root.val == root.next.val : 
                    root.next = root.next.next
                    solve(root)
                else:
                    solve(root.next)
        solve(head)
        return res
```