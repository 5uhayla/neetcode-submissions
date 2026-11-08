class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevSet = set()
        for n in nums:
            if n in prevSet:
                return True
            else: # if num not prev seen add it 
                prevSet.add(n)
        return False