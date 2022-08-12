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
    void calsize(ListNode* head, int& count)
    {
        if(head->next==nullptr)
            return;
        calsize(head->next,++count);
    }
    void swappointer(ListNode* head,int count, int k,ListNode*& first,ListNode*& second,int size)
    {
        if(head==nullptr)
            return ;
        if( k== count)
        {
            first = head;
        }
        if(size - k +1== count)
        {
            second = head;
            int temp = first->val;
            first->val = second->val;
            second->val= temp;
        }
        swappointer(head->next,++count,k,first,second,size);
    }
    ListNode* swapNodes(ListNode* head, int k) {
        //첫 번째 돌 때 전체의 갯수를 알게하자.
        ListNode* tempsize = head;
        int size = 1;
        calsize(tempsize,size);
        cout<<size;
        ListNode* first;
        ListNode* second;
        if(size/2 < k)
            k = size-k+1;
        swappointer(tempsize,1,k,first,second,size);
        return head;
    
    }
};
```