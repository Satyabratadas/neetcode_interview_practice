
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        for key, value in count_map.items():
            freq[value].append(key)
        for i in range(len(freq)- 1, -1, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
