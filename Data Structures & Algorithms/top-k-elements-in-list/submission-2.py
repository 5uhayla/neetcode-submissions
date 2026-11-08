class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {} # value, freq
        for i in nums:
            freqMap[i] = freqMap.get(i, 0) + 1
        
        sortMap = sorted(freqMap.items(), key=lambda item: item[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(sortMap[i][0]) 
        return result