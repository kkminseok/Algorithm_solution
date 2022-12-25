```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary로 풀자 O(n)으로는 불가
        mid = 0
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid-1
            else:
                left = mid+1
            #print(mid,left,right)
        return left

```