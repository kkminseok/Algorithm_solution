**c++**

```c++
class Solution {
public:
    int removePalindromeSub(string s) {
        if(s.size()==0)
            return 0;
        string reverseS = s;
        std::reverse(reverseS.begin(),reverseS.end());
        if(s == reverseS)
            return 1;   
        return 2;
    }
};
```

-----  

**python**

```python
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if(len(s)==0):
            return 0
        reverseS = s[::-1]
        if(reverseS == s):
            return 1
        else :
            return 2
```