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
    int sum=0;
    void order(TreeNode* pointer,int& sum){
        if(pointer!=nullptr)
        {
            order(pointer->right,sum);
            sum += pointer->val;
            pointer->val=sum;
            order(pointer->left,sum);
        }
        
    }

    TreeNode* convertBST(TreeNode* root) {
        order(root,sum);
        return root;
    }
};
```
