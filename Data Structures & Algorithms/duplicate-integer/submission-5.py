class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {} # num, index
        for i, n in enumerate(nums):
            if prevMap.get(n) != None:
                return True
            if not prevMap.get(n): # if num not prev seen add it 
                prevMap[n] = i 
        return False
                
            

        '''i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    return True
                j += 1
            i += 1
        return False
    '''