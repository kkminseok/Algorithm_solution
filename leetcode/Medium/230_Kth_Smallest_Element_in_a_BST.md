**c++**

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void findst(set<int>& st, TreeNode* root){
        if(root!=nullptr){
            st.insert(root->val);
            findst(st,root->left);
            findst(st,root->right);
        }
    }
    
    int kthSmallest(TreeNode* root, int k) {
        set<int> st;
        findst(st,root);
        int count = 1;
        for(auto it = st.begin();it!=st.end(); ++it,++count)
            if(count==k){
                return *it;
            }
        
        return 1;
        
    }
};
```