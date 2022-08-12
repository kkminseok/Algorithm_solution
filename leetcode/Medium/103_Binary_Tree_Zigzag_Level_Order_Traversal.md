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
    void DFS(TreeNode* root, int depth, vector<vector<int>>& res){
        if(root){
            if(res.size() < depth){
                vector<int> temp;
                temp.push_back(root->val);
                res.push_back(temp);
            }
            else
                res[depth-1].push_back(root->val);
            DFS(root->left,depth+1,res);
            DFS(root->right,depth+1,res);
        }
    }
    
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        DFS(root,1,res);
        for(int i = 0 ; i <res.size();++i){
            if(i%2==1) reverse(res[i].begin(),res[i].end());
        }
        return res;
    }
};
```