**python**


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None : 
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
```

------  

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
    int cal(TreeNode* root)
    {
        if(root!=nullptr)
        {
            return max(cal(root->left),cal(root->right))+1;
        }
        return 0;
    }
    
    int maxDepth(TreeNode* root) {
        return cal(root);
    }
};
```
