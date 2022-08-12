```c++
class Solution {
public:
    void cal(vector<string>& result,string S,int index,string temp)
    {
        if(index==S.size())
        {
            //cout<<temp;
            result.push_back(temp);
            return;
        }
        else
        {
            //digit
            if(S[index]>=48 && S[index]<=57)
                cal(result,S,index+1,temp+=S[index]);
            else
            {
                cal(result,S,index+1,temp+=(tolower(S[index])));
                temp.resize(temp.size()-1);
                cal(result,S,index+1,temp+=(toupper(S[index])));
            }
        }
    }
    
    vector<string> letterCasePermutation(string S) {
        vector<string> result;
        string temp="";
        cal(result,S,0,temp);
        return result;
        
    }
};
``