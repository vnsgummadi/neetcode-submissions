class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = [[] for i in range(len(nums)+1)]
        nn = {}

        for i in nums:
            if i in nn:
                nn[i] +=1
            else:
                nn[i] = 1
        for key, value in nn.items():
            fre[value].append(key)
        res = []
        for i in range(len(fre)-1,0,-1):
            for j in fre[i]:
                res.append(j)
                if len(res) == k:
                    return res
                
            
            



