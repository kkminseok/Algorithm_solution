# c++

```c++
class Solution {
public:
    bool isPalindrome(int x) {
        string temp = std::to_string(x);
        int left = 0;
        int right = temp.size()-1;
        while(left<=right)
        {
            if(temp[left++]!=temp[right--])
                return false;
        }
        return true;
    }
};
```

-----  

## python

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        left = 0
        right = len(temp)-1
        while(left<=right):
            if temp[left]!=temp[right]:
                return False
            left+=1
            right-=1
        
        return True
```
