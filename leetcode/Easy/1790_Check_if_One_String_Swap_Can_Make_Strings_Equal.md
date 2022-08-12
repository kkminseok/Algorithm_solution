**python**

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        check = 0
        for i in range(len(s1)):
            if s1[i] != s2[i] :
                if check >=2 :
                    return False
                else : 
                    if s2.find(s1[i]) != -1:
                        check+=1
                    else : 
                        return False
        return True if check %2 == 0 else False
                
```