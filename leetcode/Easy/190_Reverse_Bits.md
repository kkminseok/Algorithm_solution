**c++**

```c++
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        bitset<32> bs;
        int count = 0 ;
        while(n!=0)
        {
            bs.set(count,n%2);
            n/=2;
            ++count;
        }
        string result = bs.to_string();
        reverse(result.begin(),result.end());
        bitset<32> resultbs(result);
        uint32_t find = resultbs.to_ulong();
        
        return find;
    }
};
```