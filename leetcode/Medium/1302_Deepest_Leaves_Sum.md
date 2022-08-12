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
    int deepestLeavesSum(TreeNode* root) {
        int res = 0 ,i;
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty()){
            for(res = 0, i = q.size()-1; i>=0; --i){
                TreeNode* nd = q.front();
                q.pop();    
                res += nd->val;
                if(nd->left) q.push(nd->left);
                if(nd->right) q.push(nd->right);
            }
        }
        return res;
    }
};
```