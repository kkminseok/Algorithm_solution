**c++**

```c++
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry= 0;
        int size = digits.size()-1;
        while(size>=0 && digits[size]==9)
        {
            digits[size]=0;
            --size;
        }
        if(size==-1)
        {
            digits.push_back(1);
            reverse(digits.begin(),digits.end());
        }
        else
            digits[size]++;
        return digits;
    }
};
```