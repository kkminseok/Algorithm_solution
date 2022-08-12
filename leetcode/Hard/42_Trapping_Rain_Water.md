**python**

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxleft = 0
        maxright = 0
        result = 0
        
        while left <= right:
            if height[left] <= height[right] :
                if maxleft <= height[left] : 
                    maxleft = height[left]
                else:
                    result += maxleft - height[left]
                left+=1
            else :
                if maxright <= height[right] : 
                    maxright = height[right]
                else:
                    result += maxright - height[right]
                right-=1
        return result
```

-----

**c++**

```c++
class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int result = 0;
        int maxleft = 0;
        int maxright = 0;
        
        while(left<=right)
        {
            if(height[left]<=height[right])
            {
                if(height[left]>=maxleft) maxleft = height[left];
                else
                    result += maxleft - height[left];
                ++left;
            }
            else
            {
                if(height[right]>=maxright) maxright = height[right];
                else
                    result += maxright - height[right];
                --right;
            }
        }
        return result;
    }
};
```