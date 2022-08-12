**python**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        queue = deque([root])
        
        while queue:
            sumnum = 0.0
            sizenum = len(queue)
            for i in range (0,sizenum) :
                numb = queue.popleft()
                sumnum +=numb.val
                if (numb.left !=None):
                    queue.append(numb.left)
                if (numb.right !=None) :
                    queue.append(numb.right)
            result.append(sumnum/sizenum)
        return result
```

-----  

**c++**


        
```c++
/*
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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> result;
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty())
        {
            int x = q.size();
            double sum = 0.0;
            for(int i = 0; i<x;++i)
            {
                TreeNode* numb = q.front();
                q.pop();
                sum += (numb->val);
                if(numb->left!=nullptr) q.push(numb->left);
                if(numb->right!=nullptr) q.push(numb->right);
            }
            result.push_back(sum/x);
        }
        return result;
        
    }
};
```