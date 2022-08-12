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
    TreeNode* trimBST(TreeNode* root, int low, int high) {
        if(root!=nullptr)
        {
            if(root->val >=low && root->val<=high)
            {
                //왼쪽을 검사
                root->left = trimBST(root->left,low,high);
                //오른쪽을 검사
                root->right = trimBST(root->right,low,high);
                //잘 마무리되면 root return
                return root;
            }
            //값이 작은데 오른쪽 자식이 있다면 검사를 한 뒤 리턴
            if(root->val<low)
                return trimBST(root->right,low,high);
            //값이 작은데 왼쪽 자식이 있다면 검사를 한 뒤 리턴
            return trimBST(root->left,low,high);
        }
        return root;
    }
};
```