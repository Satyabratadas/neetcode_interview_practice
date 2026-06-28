class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        res = []
        for digit in digits:
            num = num * 10 + digit
        num += 1 

        if num == 0:
            return [0]

        while num:
            x = num % 10
            num //= 10
            res.append(x)
        return self.swap(res)

    def swap(self, arr):
        l = 0
        r = len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr