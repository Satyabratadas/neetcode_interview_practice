class Solution:
    def isArmstrong(self, n: int) -> bool:
        if n == 0:
            return True
        
        original = n
        copy = n
        count = 0
        arm_check = 0
        while copy:
            count += 1
            copy //= 10
        while n:
            digit = n % 10
            arm_check += digit**count
            n //= 10
        if arm_check == original:
            return True
        return False