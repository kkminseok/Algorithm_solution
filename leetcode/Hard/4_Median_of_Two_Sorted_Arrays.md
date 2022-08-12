**c++**

```c++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        int mid = (n+m)/2;
        bool check = (n+m)%2;
        double result = 0;
        vector<int> vec;
        int i = 0;
        int j = 0;
        while(i<n && j<m)
        {
            if(vec.size()==mid+1)
                break;
            if(nums1[i] < nums2[j])
                vec.push_back(nums1[i++]);
            else
                vec.push_back(nums2[j++]);
        }
        int tmp = i > m ? j : i;
        while(i<n&& vec.size()!=mid+1)
        {
            vec.push_back(nums1[i++]);
        }
        while(j<m&&  vec.size()!=mid+1)
            vec.push_back(nums2[j++]);
        if(!check)
        {
            return (vec[mid] + vec[mid-1])/2.0;
        }
        return vec[mid];
    }
};
```

**python**

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if(n1== 0 and n2 ==0):
            return 0
        v = [0]* (n1+n2)
        i1=0
        i2=0
        k=0
        while i1 < n1 and i2 < n2 :
            if nums1[i1] < nums2[i2]:
                v[k] = nums1[i1]
                i1+=1
                k+=1
            else :
                v[k] = nums2[i2]
                i2+=1
                k+=1
        while i1 < n1 :
            v[k] = nums1[i1]
            i1+=1
            k+=1
        while i2 < n2 :
            v[k] = nums2[i2]
            i2+=1
            k+=1
        if (n1 + n2) %2 == 0 :
            i = (n1 + n2) // 2
            j = (n1 + n2)//2 - 1
            return (v[i] + v[j]) /2.0
        else :
            return v[(n1 + n2) //2]
       
```