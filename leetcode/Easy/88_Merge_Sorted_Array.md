```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> num(nums1.size(),0);
        for(size_t i =0;i<nums1.size();++i)
        {
            num[i]=nums1[i];
        }
        int i=0,j=0,k=0;
        while(i<m && j<n)
        {
            if(num[i]<=nums2[j])
            {
                nums1[k++] = num[i++];
            }
            else
                nums1[k++] = nums2[j++];
        }
        int tmp = i > m ? j : i;
        while(i<m)
        {
            nums1[k++] = num[i++];
        }
        while(j<n)
            nums1[k++] = nums2[j++];

    }
};
```
