class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        people.sort()
        boat_count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boat_count += 1
        return boat_count
