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
    bool check(TreeNode* root,vector<int>& voyage, int& count,vector<int>& result){
        if(root==nullptr) return true;
        if(root->val != voyage[count++]) return false;
        auto left = root->left;
        auto right = root->right;
        if(left!=nullptr && left->val != voyage[count]){
            result.push_back(root->val);
            swap(left,right);
        }
        return check(left,voyage,count,result) && check(right,voyage,count,result);
    }
    
    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        int count = 0;
        vector<int> result;
        if(check(root,voyage,count,result)){
            return result;
        }
        return vector<int>() = {-1};
            
        
    }
};

```