```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answerHead = ListNode()
        answer = answerHead
        cnt = 0
        tmphead = head
        while tmphead != None:
            cnt+=1
            tmphead = tmphead.next
        cnt = cnt//2
        for i in range(cnt):
            head = head.next
        while head != None:
            answer.next = head
            head = head.next
            answer = answer.next

        return answerHead.next
```