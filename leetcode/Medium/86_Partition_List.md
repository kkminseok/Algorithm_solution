**c++**

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
    void setless(ListNode*& less,ListNode* originless,int x){
        if(originless){
            if(originless->val <x ){
                ListNode* newNode = new ListNode(originless->val);
                less->next = newNode;
                less = less->next;
            }
            setless(less,originless->next,x);
        }
        return;
    }
    void setmore(ListNode* more,ListNode* originmore,int x){
        if(originmore){
            if(originmore->val >= x){
                ListNode* newNode = new ListNode(originmore->val);
                more->next = newNode;
                more = more->next;
            }
            setmore(more,originmore->next,x);
        }
        return ;
    }
    
    ListNode* partition(ListNode* head, int x) {
        ListNode* more = head;
        ListNode* less = head;
        ListNode* res = new ListNode();
        ListNode* temp = res;
        setless(temp,less,x);
        setmore(temp,more,x);
        return res->next;
    }
};
```