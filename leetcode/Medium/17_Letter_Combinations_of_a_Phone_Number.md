```c++
vector<string> alpha(10);
class Solution {
public:
    void getR(vector<string>& result,string digits,int count)
    {
        if(count==digits.size())
        {
            result.push_back(alpha[0]);   
        }
        else
        {
            for(int i=0;i<alpha[digits[count]-48].size();++i)
            {
                alpha[0]+=alpha[digits[count]-48][i];
                getR(result,digits,count+1);
                alpha[0].resize(size(alpha[0])-1);
            }
        }
    }
    vector<string> letterCombinations(string digits) {
        alpha[0]="";
        alpha[1]="";
        alpha[2]="abc";
        alpha[3]="def";
        alpha[4]="ghi";
        alpha[5]="jkl";
        alpha[6]="mno";
        alpha[7]="pqrs";
        alpha[8]="tuv";
        alpha[9]="wxyz";
        vector<string> result;
        if(digits.size()==0)
           return result;
        getR(result,digits,0);
        return result;
    }
};
```