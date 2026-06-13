class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = {}
        res = len(students)

        for ch in students:
            if ch not in count:
                count[ch] = 0
            count[ch] += 1
        for s in sandwiches:
            if count.get(s, 0) > 0:
                res -= 1
                count[s] -= 1
            else:break
        return res