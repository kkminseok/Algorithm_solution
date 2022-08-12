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
    vector<int> result;
    bool depth[101];
    void order(TreeNode* root,int _depth)
    {
        if(root->right!=nullptr)
        {
            if(depth[_depth]==false)
            {
                result.push_back(root->right->val);
                depth[_depth]=true;
            }
            order(root->right,_depth+1);
        }
        if(root->left!=nullptr)
        {
            if(depth[_depth]==false)
            {
                result.push_back(root->left->val);
                depth[_depth]=true;
            }
            order(root->left,_depth+1);
        }
    }
    vector<int> rightSideView(TreeNode* root) {
        memset(depth,false,sizeof(depth));
        if(root!=nullptr)
        {
            result.push_back(root->val);
            depth[0]=true;
            order(root,1);
        }
        
        return result;
    }
};
```