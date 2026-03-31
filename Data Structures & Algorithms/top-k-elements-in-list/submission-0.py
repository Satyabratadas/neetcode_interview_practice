class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq = [[] for i in range (len(nums) + 1)]
        
        for n in nums:
            if n not in count_map:
                count_map[n] = 1
            else:
                count_map[n] += 1
        
        for element, count in count_map.items():
            freq[count].append(element)
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res