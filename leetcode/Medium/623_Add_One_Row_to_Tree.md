**python**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:                
    
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def order(root : TreeNode, v : int , curr : int, d :int) :
            if root != None : 
                if d-1 == curr:
                    if root.left != None  :
                        newNode = TreeNode(v)
                        newNode.left = root.left
                        root.left = newNode
                    else :
                        newNode = TreeNode(v)
                        root.left = newNode
                    if root.right != None : 
                        newNode = TreeNode(v)
                        newNode.right = root.right
                        root.right = newNode
                    else : 
                        newNode = TreeNode(v)
                        root.right = newNode
                order(root.left,v,curr+1,d)
                order(root.right,v,curr+1,d)
        if d == 1:
            newNode = TreeNode(v)
            newNode.left = root
            return newNode
        else :
             order(root,v,1,d)
        return root
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
    void order(TreeNode* root, int v,int cur,int d)
    {
        if(root!=nullptr)
        {
            if(d-1 ==cur)
            {
                if(root->left!=nullptr)
                {
                    TreeNode* newNode =new TreeNode(v);
                    newNode->left = root->left;
                    root->left = newNode;
                }
                else
                {
                    TreeNode* newNode= new TreeNode(v);
                    root->left = newNode;
                }
                if(root->right!=nullptr)
                {
                    TreeNode* newNode =new TreeNode(v);
                    newNode->right = root->right;
                    root->right = newNode;
                }
                else
                {
                    TreeNode* newNode = new TreeNode(v);
                    root->right = newNode;
                }
            }
            order(root->left,v,cur+1,d);
            order(root->right,v,cur+1,d);
        }
    }
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if(d==1)
        {
            TreeNode* newNode = new TreeNode(v);
            newNode ->left = root;
            return newNode;
        }
        else
            order(root,v,1,d);   
        return root;
    }
};

```