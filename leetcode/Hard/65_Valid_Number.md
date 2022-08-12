**python**

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        numberS = False
        eS = False
        pointS = False
        numberAE = True
        
        for i in range(len(s)):
            if s[i]>="0" and s[i] <="9" : 
                numberS = True
                numberAE = True
            elif s[i] == ".":
                if eS or pointS :
                    return False
                pointS = True
            elif s[i] == "e" or s[i] == "E":
                if eS or not numberS : 
                    return False
                numberAE = False
                eS = True
            elif s[i] =="-" or s[i] =="+" :
                if i != 0 and s[i-1] !="e" : 
                    return False
            else:
                return False
        
        return numberS and numberAE
```

