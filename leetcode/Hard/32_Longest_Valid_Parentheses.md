**python**


```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        stk.append(-1)
        ans = 0
        for i in range(len(s)):
            if s[i] == '(' : 
                stk.append(i)
            else:
                stk.pop()
                if len(stk)==0 : 
                    stk.append(i)
                else:
                    ans = max(ans,i - stk[-1])
        return ans
```
        
-----  

**c++** 


```c++
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stk;
        stk.push(-1);
        int ans = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                stk.push(i);
            } else {
                stk.pop();
                if (stk.empty()) {
                    stk.push(i);
                } else {
                    ans = max(ans, i - stk.top());
                }
            }
        }
        return ans;
    }
};
```