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
    string str = "";
    void check(ListNode* head)
    {
        if(head==nullptr)
            return ;
        str += std::to_string(head->val);
        check(head->next);
    }
    
    bool isPalindrome(ListNode* head) {
        check(head);
        string temp = str;
        reverse(str.begin(),str.end());
        if(temp==str)
            return true;
        return false;
    }
};
```

