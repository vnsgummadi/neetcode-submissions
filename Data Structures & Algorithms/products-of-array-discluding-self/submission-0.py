class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ssum = []
        psum = []
        for i in range(len(nums)-1):
            j = i+1
            mul = 1
            while j<len(nums):
                mul = mul*nums[j]
                j+=1
            ssum.append(mul)
        ssum.append(1)

        for i in range(len(nums)-1, 0, -1):
            j = i-1
            mul = 1
            while j>-1:
                mul = mul*nums[j]
                j-=1
            psum.append(mul)
        psum.append(1)

        res = []
        for i in range(len(nums)):
            res.append(ssum[i]*psum[len(nums) - 1-i])
        return res


            
            

