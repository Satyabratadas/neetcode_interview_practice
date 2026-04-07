from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            ## create count array for ch a .. z (26 ch)
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        return list(res.values()) 

## Time complexity O(m * n)
