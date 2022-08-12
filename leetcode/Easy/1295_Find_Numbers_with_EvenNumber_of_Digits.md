```c++
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        //정렬
        sort(nums.begin(),nums.end());
        int count=0;
        int division;
        int temp=nums[0];
        int init=0;
        while(temp!=0)
        {
            temp/=10;
            init++;
        }
        //맨처음 요소가 짝수이면 10, 1000,10000 등으로 맞추려고 함.
        if(init%2==0)
            --init;
        division = pow(10,init);
        
        for(size_t i=0;i<nums.size();)
        {
            //홀수라면 넘어감.
            if(division > nums[i])
            {
                ++i;
                continue;
            }
            else
            {
                division*=10;
                //짝수라면 그 범위내에서 카운트를 세줌. 10~99, 1000~9999 ...
                while(i<nums.size() && nums[i]<division&&nums[i]>=division/10)
                {
                    ++count;
                    ++i;
                }
                division*=10;
            }
        }
        return count;
    }
};
```
