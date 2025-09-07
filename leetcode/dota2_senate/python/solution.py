from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: greedy
        """
        r_votes = deque()  # (index)
        d_votes = deque()  # (index)

        for index, vote in enumerate(senate):
            if vote == "R":
                r_votes.append(index)
            else:
                d_votes.append(index)
            
        while r_votes and d_votes:
            if r_votes[0] < d_votes[0]:
                d_votes.popleft()
                r_votes.append(r_votes.popleft() + len(senate))
            else:
                r_votes.popleft()
                d_votes.append(d_votes.popleft() + len(senate))
            
        return "Radiant" if r_votes else "Dire"


class Solution2:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: failed
        """
        # accumulated vote points
        points = 0  # R: +1, D: -1
        # right to block
        block = 0  # R: +1, D: -1
        # peack points to resolve draws
        max_points = min_points = 0
        
        for vote in senate:
            if vote == "R":
                if block < 0:
                    block += 1
                else:
                    points += 1
                    block += 1
                    max_points = max(max_points, points)
            if vote == "D":
                if block > 0:
                    block -= 1
                else:
                    points -= 1
                    block -= 1
                    min_points = min(min_points, points)
        if points > 0 or (points == 0 and block > 0) or (points == 0 and block == 0 and max_points > -min_points):
            return "Radiant"
        elif points < 0 or (points == 0 and block < 0) or (points == 0 and block == 0 and -min_points > max_points):
            return "Dire"
        else:
            return "Panik"
        # return (points, block, (max_points, min_points))


print(Solution().predictPartyVictory("RD") == "Radiant")
print(Solution().predictPartyVictory("DR") == "Dire")
print(Solution().predictPartyVictory("RDD") == "Dire")
print(Solution().predictPartyVictory("RDDDRR") == "Dire")
print(Solution().predictPartyVictory("RDDR") == "Radiant")
print(Solution().predictPartyVictory("DRRD") == "Dire")
print(Solution().predictPartyVictory("DDDDRRDDDRDRDRRDDRDDDRDRRRRDRRRRRDRDDRDDRRDDRRRDDRRRDDDDRRRRRRRDDRRRDDRDDDRRRDRDDRDDDRRDRRDRRRDRDRDR") == "Dire")