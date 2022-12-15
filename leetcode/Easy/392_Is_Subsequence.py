class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        i=0
        while i < len(s) and j < len(t):
            while(j < len(t) and s[i] != t[j]):
                j+=1
            if(j < len(t) and s[i] == t[j]):
                i+=1
                j+=1
        return True if i == len(s) else False