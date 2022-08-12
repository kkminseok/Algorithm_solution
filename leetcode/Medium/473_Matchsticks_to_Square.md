**python**

```python
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sumnum = sum(matchsticks)
        if sumnum%4 !=0:
            return False
        target = [sumnum//4] * 4
        matchsticks.sort(reverse = True)
        def bfs(num,depth,target) :
            if depth == len(num) : 
                return True
            for i in range(4):
                if target[i] >= num[depth] : 
                    target[i] -= num[depth]
                    if bfs(num,depth+1,target) : return True
                    target[i] += num[depth]
            return False
        return bfs(matchsticks,0,target)
```