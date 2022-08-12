**c++**

```c++
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        dp[0][0] = true;
        for (int i = 0; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 2] || (i && dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'));
                } else {
                    dp[i][j] = i && dp[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
                }
            }
        }
        
        return dp[m][n];
    }
};
```

-----  

**python**

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = []
        for j in range(m+1):
            dp.append([])
            for i in range(n+1):
                dp[j].append([])
        dp[0][0] = 1
        for i in range(0,m+1):
            for j in range(1,n+1):
                if(p[j-1]=='*'):
                    dp[i][j] = dp[i][j-2] or (i and dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j] = i and dp[i-1][j-1] and (s[i-1]== p[j-1] or p[j-1] == '.')
                    
        return dp[m][n]
        
```