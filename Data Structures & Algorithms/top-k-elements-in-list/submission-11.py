
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, val in count.items():
            freq[val].append(key)

        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


