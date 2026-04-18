

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq_count = [[] for i in range (len(nums) + 1)]
        result = []
        print(freq_count)
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)
        for num, freq in count_map.items():
            freq_count[freq].append(num)
        
        for i in range(len(freq_count) - 1, -1, -1):
            for n in freq_count[i]:
                result.append(n)
                if len(result) == k:
                    return result
