**c++**

```c++
class Solution {
public:
    
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size()-1;
        
        while(left<=right){
            while(left< s.size() && !isd(s[left]) && !ise(s[left])){
                ++left;
            }
            while(right> 0 && !isd(s[right]) && !ise(s[right])){  
                --right;
            }
            if(left>right)
                return true;
            if(ise(s[left]) && ise(s[right]) ){
                s[left] = tolower(s[left]);
                s[right] = tolower(s[right]);
            }
            if(s[left] != s[right])
                return false;
            //cout<<s[left]<<" "<<s[right]<<'\n';
            ++left;
            --right;
            
        }
        return true;
    }
    bool isd(char c){
        return isdigit(c);
    }
    bool ise(char c){
        return isalpha(c);
    }
};
```