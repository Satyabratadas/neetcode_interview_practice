class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        result = right
        while left <= right:
            m = left + (right - left) // 2
            if self.cap(m, weights, days):
                result = min(result, m)
                right = m - 1
            else:
                left = m + 1
        return result

    
    def cap(self, capacity, weights, days):
        ships, current = 1, capacity
        for w in weights:
            if current - w < 0:
                ships += 1
                if ships > days:
                    return False
                current = capacity
            current -= w
        return True 
