**c++**

```c++
class Solution {
public:
    string intToRoman(int num) {
        string temp ="";
        while(num!=0)
        {
            if(num>=1000)
            {
                num-=1000;
                temp+='M';
            }
            else if(num>=900)
            {
                num-=900;
                temp+="CM";
            }
            else if(num>=500)
            {
                num-=500;
                temp+='D';
            }
            else if(num>=400)
            {
                num-=400;
                temp+="CD";
            }
            else if(num>=100)
            {
                num-=100;
                temp+='C';
            }
            else if(num>=90)
            {
                num-=90;
                temp+="XC";
            }
            else if(num>=50)
            {
                num-=50;
                temp+='L';
            }
            else if(num>=40)
            {
                num-=40;
                temp+="XL";
            }
            else if(num>=10)
            {
                num-=10;
                temp+='X';
            }
            else if(num>=9)
            {
                num-=9;
                temp+="IX";
            }
            else if(num>=5)
            {
                num-=5;
                temp+='V';
            }
            else if(num>=4)
            {
                num-=4;
                temp+="IV";
            }
            else if(num>0)
            {
                num-=1;
                temp+='I';
            }
        }
        

        
        return temp;
    }
};
```