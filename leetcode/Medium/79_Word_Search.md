**python**

```python
class Solution:
    def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position    
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res
        
```

-----  

**c++**

```c++
int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};
bool v[200][200] ={0,};
class Solution {
public:
    bool DFS(int x,int y,vector<vector<char>>& board,int m,int n,string word,int depth)
    {
        if(depth == word.size()-1 )
        {
            if(board[x][y] == word[depth])
                return true;
            else
                return false;
        }   
        for(int k = 0;k<4;++k)
        {
            int newX = x + dx[k];
            int newY = y + dy[k];
            if(0<=newX && newX<m && 0<=newY && newY<n && board[newX][newY] == word[depth+1] && !v[newX][newY])
            {
                //cout<<newX<<newY<<board[newX][newY]<<" "<<depth<<'\n';
                v[newX][newY] = true;
                if(DFS(newX,newY,board,m,n,word,depth+1))
                    return true;
                v[newX][newY]=false;
            }
        }
        return false;
        
        
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        //DFS
        int row = board.size();
        int col = board[0].size();
        if(row * col < word.size())
            return false;
        for(size_t i = 0;i<row;++i)
        {
            for(size_t j = 0 ; j<col;++j)
            {
                memset(v,false,sizeof(v));
                if(board[i][j] == word[0])
                {
                    v[i][j]=true;
                    if(DFS(i,j,board,row,col,word,0))
                        return true;
                }
                
            }
        }
        return false;
        
        
    }
};
```