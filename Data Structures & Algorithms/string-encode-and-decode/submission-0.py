class Solution:

    def encode(self, strs: List[str]) -> str:
        stra = ""
        
        for s in strs:
            enc = str(len(s))+"#"+s
            stra+=enc
        return stra

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            j+=1
            res.append(s[j:j+length])

            i = j+length
        return res



