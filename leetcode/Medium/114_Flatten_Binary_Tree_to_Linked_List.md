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
    void Preorder(TreeNode* Node,TreeNode*& temp)
    {
        if(Node==nullptr)
            return ;
        
        Preorder(Node->right,temp);
        Preorder(Node->left,temp);
        Node->right = temp;
        Node->left=nullptr;
        temp = Node;

    }
    void flatten(TreeNode* root) {
        TreeNode* temp=nullptr;
        Preorder(root,temp);
    }
};
```