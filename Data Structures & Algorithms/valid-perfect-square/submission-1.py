class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        h = num

        while l <= h:
            mid = l + (h - l) // 2
            square = mid * mid
            if square == num :
                return True
            elif square < num:
                l = mid + 1
            else:
                h = mid - 1
        return False