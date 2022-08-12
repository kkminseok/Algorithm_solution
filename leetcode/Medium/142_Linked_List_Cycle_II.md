**python**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head ==None or head.next ==None :
            return None
        onext = head
        dnext = head
        cycle = 0
        while onext != None and dnext!=None:
            if dnext.next == None :
                return None
            onext = onext.next
            dnext = dnext.next.next
            if onext == dnext:
                cycle = 1
                break
        if not cycle :
            return None
        onext = head
        while onext != dnext : 
            onext = onext.next
            dnext = dnext.next
        return onext

    
```

------  

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

    ListNode *detectCycle(ListNode *head) {
        if (head==nullptr || head->next==nullptr) return nullptr;
        
        ListNode* onext = head;
        ListNode* dnext = head;
        bool cycle = false;
        while(onext!=nullptr && dnext!=nullptr)
        {
            onext = onext->next;
            if(dnext->next ==nullptr) return nullptr;
            dnext = dnext->next->next;
            if(dnext == onext)
            {
                cycle = true;
                break;
            }
        }
        if(!cycle) return nullptr;
        
        onext = head;
        while(onext!=dnext)
        {
            onext = onext->next;
            dnext = dnext->next;
        }
        return onext;
        
    }
};
```