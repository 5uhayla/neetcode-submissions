class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tp = 1
        zeroSpot = False
        for i in nums:
            tp = tp * i
        zerotp = 1
        for i in nums:
            if i == 0 and not zeroSpot: 
                zeroSpot = True
            else:
                zerotp = zerotp * i
        res = []
        for i in nums:
            if i != 0:
                res.append(tp//i)
            else: 
                res.append(zerotp)


        return res