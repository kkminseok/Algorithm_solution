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
    ListNode* sortList(ListNode* head) {
        vector<int> temp;
        ListNode* result = head;
        while(result!=nullptr)
        {
            temp.push_back(result->val);
            result=result->next;
        }
        sort(temp.begin(),temp.end());
        result = head;
        for(size_t i =0;i<temp.size();++i)
        {
            result->val = temp[i];
            result = result->next;
        }
        
        return head;
    }
};
```