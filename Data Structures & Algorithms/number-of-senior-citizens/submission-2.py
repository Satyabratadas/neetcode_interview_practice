class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
            for i, ch in enumerate(passenger):
                current_age = ""
                if ord("A") <= ord(ch) <= ord("Z"):
                    for j in range(i+1, i +3):
                        current_age += passenger[j]
                    age = int(current_age)
                    print(age)
                    if int(current_age) > 60:
                        count += 1
        return count


        
        