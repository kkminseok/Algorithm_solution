**python**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def test(leftP : TreeNode, rightP : TreeNode) -> bool:
            if leftP == None and rightP == None : 
                return True
            elif leftP == None or rightP == None : 
                return False
            return (leftP.val == rightP.val) and test(leftP.left,rightP.right) and test(leftP.right,rightP.left)
        
        return test(root.left,root.right)
```
-----  



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
    bool test(TreeNode* leftP, TreeNode* rightP)
    {
        if(leftP==nullptr && rightP==nullptr)
            return true;
        else if(leftP==nullptr || rightP==nullptr)
            return false;
        return (leftP->val == rightP->val) &&test(leftP->left,rightP->right) && test(leftP->right,rightP->left);
    }
    bool isSymmetric(TreeNode* root) {
        return test(root->left,root->right);
    }
};
```