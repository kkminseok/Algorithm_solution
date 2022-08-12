```c++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.size()==1)
            return nums[0]==target ? 0 : -1;
        
        
        int start =0;
        int end = nums.size()-1;
        int max = nums[end];
        //끝에서부터 탐색
        if(target<=nums[end])
        {
            while(end>start && nums[end]>target)
            {
                cout<<end<<'\n';
                --end;
            }
            if(nums[end]==target)
                return end;
            else
                return -1;
        }
        else
        {
            while(start<end &&nums[start]<target)
            {
                ++start;
            }
            if(nums[start]==target)
                return start;
            else
                return -1;
        }
        
        return -1;
    }
};
```

**python**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 : return -1 if nums[0] != target else 0
        #binary search
        left = 0
        right = len(nums)-1
        if nums[right] == target :
            return right
        
        if nums[right] > target :
            while right-1 >=0 and nums[right] >nums[right-1] : 
                if nums[right-1] == target : 
                    return right-1
                right-=1
        else : 
            if nums[left] == target : 
                return left
            while left+1 < len(nums) and nums[left] < nums[left+1] : 
                if nums[left+1] == target : 
                    return left+1
                left+=1
                    
        return -1
```