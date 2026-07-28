class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l , r = max(weights), sum(weights)
        res = r

        def cap(capacity):
            ships, curCap = 1, capacity
            for w in weights:
                if curCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curCap = capacity
                curCap -= w
            return True
        while l <= r:
            mid = l + (r - l) // 2
            if cap(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
