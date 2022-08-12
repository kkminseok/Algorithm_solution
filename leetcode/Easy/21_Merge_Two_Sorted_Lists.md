```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode();
        ListNode* head = result;
        while(l1!=nullptr && l2!=nullptr)
        {
            if(l1->val >= l2->val)
            {
                result->next = l2;
                l2=l2->next;
            }
            else
            {
                result->next=l1;
                l1=l1->next;
            }
                result= result->next;
        }
        while(l1!=nullptr)
        {
            result->next=l1;
            result=result->next;
            l1=l1->next;
        }
        while(l2!=nullptr)
        {
            result->next=l2;
            result=result->next;
            l2=l2->next;
        }
        
        return head->next;
    }
};
```