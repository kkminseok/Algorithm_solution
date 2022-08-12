**python**

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #LCS
        row = len(nums1)+1
        col = len(nums2)+1
        DP = [0] * row
        res = 0 
        for i in range(row) : 
            DP[i] = [0] * col
        
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0 :
                    DP[i][j] = 0
                else: 
                    if nums1[i-1] == nums2[j-1] : 
                        DP[i][j] = DP[i-1][j-1] + 1
                    else : 
                        DP[i][j] = 0
                res = max(res,DP[i][j])
        return res 
```