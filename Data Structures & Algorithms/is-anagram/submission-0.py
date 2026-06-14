class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        fre = {}
        fre2 = {}
        for i in s:
            fre[i] = fre.get(i,0)+1

        for j in t:
            fre2[j] = fre2.get(j,0)+1

        if fre == fre2:
            return True
        else:
            return False
