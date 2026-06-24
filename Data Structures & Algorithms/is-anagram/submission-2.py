from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occMapS = defaultdict(int)
        occMapT = defaultdict(int)
        for i in range(len(s)):
            occMapS[s[i]]+=1
        for j in range(len(t)):
            occMapT[t[j]]+=1
        return len(s)==len(t) and occMapS==occMapT
