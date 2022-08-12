**python**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        count = 1
        st = deque()
        lnode = head
        rnode =head
        while rnode : 
            if count == left : 
                lnode = rnode
                while rnode and count != right+1 :  
                    count+=1
                    st.append(rnode.val)
                    rnode = rnode.next
                break
            else : 
                rnode = rnode.next
                count+=1
            
        while st : 
            lnode.val = st.pop()
            lnode = lnode.next
        return head
        
```