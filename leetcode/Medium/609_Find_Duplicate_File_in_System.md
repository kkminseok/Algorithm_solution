**python**

```python
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        res = []
        for i in range(len(paths)):
            direction = paths[i].split()
            root = direction[0]
            for j in range(1,len(direction)) : 
                temp = direction[j]
                name = root +"/" + temp[:temp.find("(")]  
                content = temp[temp.find("(")+1 : temp.find(")")]
                if content not in dic :
                    tlist = []
                    tlist.append(name)
                    dic[content] = tlist
                else : 
                    dic[content].append(name)
        for i in dic : 
            if len(dic[i])>=2 :
                res.append(dic[i])
        return res
```