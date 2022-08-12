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
    int result = 0;
    int order(TreeNode* node)
    {
        if(node!=nullptr)
            return max(order(node->left),order(node->right) )+1;
        return 0;
    }
    
    int diameterOfBinaryTree(TreeNode* root) {
        if(root!=nullptr)
        {
            int leftdepth = order(root->left);
            int rightdepth = order(root->right);
            result = max(result,leftdepth+rightdepth);
            diameterOfBinaryTree(root->left);
            diameterOfBinaryTree(root->right);
        }
        return result;
    }
};
```