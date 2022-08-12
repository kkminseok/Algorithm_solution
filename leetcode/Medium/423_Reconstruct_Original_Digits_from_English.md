**c++**

```c++
class Solution {
public:
    string originalDigits(string s) {
        int count[10] = {0,};
        for(size_t i =0;i<s.size();++i)
        {
            char stri = s[i];
            if(stri == 'z') count[0]++;
            if (stri == 'w') count[2]++;
            if (stri == 'x') count[6]++;
            if (stri == 's') count[7]++; //7-6
            if (stri == 'g') count[8]++;
            if (stri == 'u') count[4]++; 
            if (stri == 'f') count[5]++; //5-4
            if (stri == 'h') count[3]++; //3-8
            if (stri == 'i') count[9]++; //9-8-5-6
            if (stri == 'o') count[1]++; //1-0-2-4
        }
        count[7]-=count[6];
        count[5] -= count[4];
        count[3] -=count[8];
        count[9] =  count[9] - count[8] - count[5]- count[6];
        count[1] = count[1] -count[0] - count[2]-count[4];
        string result = "";
        for(int i = 0;i<10;++i){
            for(int j =0;j<count[i];++j)
                result+=i+48;
        }
        
        return result;
    }
    
};
```