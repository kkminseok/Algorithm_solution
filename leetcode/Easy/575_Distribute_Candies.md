**c++**



```c++
class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        sort(candyType.begin(),candyType.end());
        int num = candyType.size()/2;
        int count = 1;
        for(size_t i =0;i<candyType.size()-1;++i)
        {
            if(candyType[i] != candyType[i+1])
                ++count;
        }
        return count > num ? num : count;
    }
};
```


**python**

```python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
            candyType.sort()
            num = int(len(candyType)/2)
            count = 1
            for i in range(len(candyType)-1):
                if candyType[i] != candyType[i+1]:
                    count+=1
            return num if count> num  else count
```