```c++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int result = 0;
        int left = 0;
        int right = height.size()-1;
        while(left<=right)
        {
            cout<<left<<" "<<right<<" ";
            int line = min(height[left],height[right]);
            int area = line * (right-left);
            cout<<area<<'\n';
            result = max(area,result);
            if(height[left]<height[right])
                ++left;
            else
                --right;
        }
        
        return result;
    }
};
```