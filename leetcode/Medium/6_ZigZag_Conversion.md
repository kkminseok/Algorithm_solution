```c++
class Solution {
public:
    string convert(string s, int numRows) {
        int iter = (numRows-1)*2;
        if(numRows==1 || numRows > s.size())
            return s;
        string result="";
        for(int i = 0;i<numRows;++i)
        {
            result+=s[i];
            int right = iter-(i*2);
            int left = iter-right;
            int index = i;
            for(;index<s.size();)
            {
                if(s.size()<=index+right)
                    break;
                if(right!=0 && s[index+right]!=' ')
                    result+=s[index+right];
                index+=right;
                if(s.size()<=index+left)
                    break;
                if(left!=0 && s[index+left]!=' ')
                {
                    result+=s[index+left];
                }
                index+=left;
            }
        }
        return result;
    }
};
```