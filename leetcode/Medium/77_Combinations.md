**python**

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        li = [x+1 for x in range(n)]
        li = list(combinations(li, k))
        return li
```