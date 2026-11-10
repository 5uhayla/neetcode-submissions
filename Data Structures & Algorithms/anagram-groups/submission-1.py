class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag_map = defaultdict(list) # anagram, indexes

        for i in range(len(strs)):
            anagram = "".join(sorted(strs[i]))
            ag_map[anagram].append(i)

        res = []
        for a in ag_map:
            sublist = []
            for i in ag_map.get(a):
                sublist.append(strs[i])
            res.append(sublist)

        return res

