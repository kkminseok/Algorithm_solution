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
    void save(ListNode* head,vector<int>& vec)
    {
        if(head!=nullptr)
        {

            vec.push_back(head->val);
            save(head->next,vec);
        }
        
    }
    //재귀
    void put(ListNode* node,vector<int>& vec,int count)
    {
        if(node!=nullptr)
        {
            node->val = vec[count--];
            put(node->next,vec,count);
        }
    }
    //for문
    void put2(ListNode* node,vector<int>& vec,int count)
    {
        for(;count>=0;--count)
        {
            node->val = vec[count];
            node=node->next;
        }
    }
    ListNode* reverseList(ListNode* head) {
        ListNode* savenode = head;
        vector<int> vec;
        save(savenode,vec);
        savenode= head;
        //put(head,vec,vec.size()-1);
        //put2(head,vec,vec.size()-1);
        //수정 구문
        ListNode* prev= nullptr;
        ListNode* next;
        while(savenode!=nullptr)
        {
            next = savenode->next;
            savenode->next = prev;
            prev = savenode;
            savenode=next;
        }
        
        return prev;
    }
};
```