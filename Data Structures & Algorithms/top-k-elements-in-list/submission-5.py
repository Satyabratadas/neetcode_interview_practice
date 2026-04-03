

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq = [[] for i in range(len(nums) + 1)]
        top_ele = []

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            
        for num, count in count_map.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                top_ele.append(n)
                if len(top_ele) == k:
                    return top_ele
