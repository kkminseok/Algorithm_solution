**c++**

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA == nullptr || headB == nullptr)
            return 0;
        
        ListNode* a = headA;
        ListNode* b = headB;
        
        while(a!=b)
        {
            a = a == nullptr ? headB : a->next;
            b = b == nullptr ? headA : b->next;
        }
        return a;
    }
};
```

-----  

**python**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None :
            return None
        
        a = headA
        b = headB
        while a != b:
            a = headB if a == None else a.next
            b = headA if b == None else b.next
        
        return a
```