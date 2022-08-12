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
    void solution(ListNode*& first,ListNode*& tempnode,ListNode*& head,int count,int n)
    {
        if(first->next!=nullptr)
        {
            if(count==n)
            {
                tempnode=tempnode->next;
            }
            else
                ++count;
            solution(first->next,tempnode,head,count,n);
        }
        else
        {
            if(count!=n)
            {
                head= head->next;
            }
            else
                tempnode->next=tempnode->next->next;
        }
    }
    
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* first = head;
        ListNode* tempnode = head;
        solution(first,tempnode,head,0,n);
        return head; 
    }
};
```