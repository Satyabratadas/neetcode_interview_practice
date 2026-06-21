
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_element = Counter(nums)
        top_k_element = count_element.most_common(k)
        res = []
        for i in range(len(top_k_element)):
            res.append(top_k_element[i][0])
        return res
        