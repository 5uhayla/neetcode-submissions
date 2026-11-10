class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # anagram, words

        for w in strs:
            sortedw = "".join(sorted(w))
            res[sortedw].append(w)

        return list(res.values())

