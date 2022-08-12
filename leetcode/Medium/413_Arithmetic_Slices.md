```c++
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        if(A.size()<3)
            return 0;
        int count=1;
        int temp = A[1]-A[0];
        int result = 0;
        int* DP=new int[A.size()+1];

        for(int i = 0;i<A.size()+1;++i)
            DP[i]=0;
        
        for(size_t i = 2;i<A.size();++i)
        {
            if(A[i]-A[i-1]==temp)
            {
                ++count;
            }
            else
            {
                count=1;
                temp = A[i]-A[i-1];
            }
            if(count>=2)
            {
                DP[i] = DP[i-1] + (DP[i-1] -DP[i-2] + 1);
            }
        }
        for(size_t i=0;i<A.size();)
        {
            while(DP[i+1]!=0 && i<A.size())
            {
                ++i;
            }
            result+=DP[i];
            ++i;
        }
        
        return result;
    }
};
```