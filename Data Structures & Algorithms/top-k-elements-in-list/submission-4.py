from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # freq_arr = [[] for i in range(len(nums)+1)]
        # rev = []

        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        
        # for key, val in count.items():
        #     freq_arr[val].append(key)
        # for i in range(len(freq_arr) - 1, 0, -1):
        #     for num in freq_arr[i]:
        #         rev.append(num)
        #         if len(rev) == k:
        #             return rev

        count_ele = Counter(nums)
        top_ele = []

        top_k_element = count_ele.most_common(k)
        # print(top_k_element)

        for pair in top_k_element:
            element = pair[0]
            top_ele.append(element)
        return top_ele

