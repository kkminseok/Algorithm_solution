**python**

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        #150은 아스키코드 갯수.
        check = [False] * 150
        for i in range(len(s)):
            if s[i] not in dic :
                if check[ord(t[i])] == True:
                    return False
                dic[s[i]] = t[i]
                check[ord(t[i])] = True
            else : 
                if dic[s[i]] != t[i]:
                    return False
        return True
        
```