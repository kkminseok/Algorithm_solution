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
    vector<vector<int>> result;
    vector<vector<int>> order(TreeNode* root,int count)
    {
        if(root!=nullptr)
        {
            if(count>result.size())
            {
                vector<int> temp;
                temp.push_back(root->val);
                result.push_back(temp);
            }
            else
                result[count-1].push_back(root->val);
            order(root->left,count+1);
            order(root->right,count+1);
        }
        
        return result;   
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        result = order(root,1);
        return result;
    }
};
```