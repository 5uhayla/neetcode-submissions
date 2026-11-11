class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = []
        for i in range(len(nums)):
            res.append(pre)
            pre = pre * nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * post
            post = post * nums[i]     
        return res