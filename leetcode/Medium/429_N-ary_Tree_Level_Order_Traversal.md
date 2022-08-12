**python**

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res =[]
        def solution(root,depth,res):
            if root : 
                if len(res) <= depth : 
                    res.append([])
                res[depth].append(root.val)
                for i in range(len(root.children)) : 
                    solution(root.children[i],depth+1,res)
        solution(root,0,res)
        return res
        
```