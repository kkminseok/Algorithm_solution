**c++**

```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> preorder(Node* root) {
        deque<Node*> q;
        vector<int> res;
        if(!root) return res;
        q.push_front(root);
        while(!q.empty()){
            Node* frontnode = q.front();
            q.pop_front();
            res.push_back(frontnode->val);
            for(int i = frontnode->children.size()-1 ; i >=0; --i){
                q.push_front(frontnode->children[i]);
            }
        }
        return res;
    }
};
```