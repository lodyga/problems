from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: queue
            A: greedy
        """
        votes = deque(senate)
        r = 0
        
        while (
            len(votes) > abs(r)
        ):
            vote = votes.popleft()
            
            if vote == "R":
                if r >= 0:
                    votes.append("R")
                r += 1

            else:
                if r <= 0:
                    votes.append("D")
                r -= 1

        return "Radiant" if votes[0] == "R" else "Dire"
        

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: queue
            A: greedy
        """
        # (radiant index)
        radiant_votes = deque()
        # (dire index)
        dire_votes = deque()

        for index, vote in enumerate(senate):
            if vote == "R":
                radiant_votes.append(index)
            else:
                dire_votes.append(index)
            
        while radiant_votes and dire_votes:
            if radiant_votes[0] < dire_votes[0]:
                dire_votes.popleft()
                radiant_votes.append(radiant_votes.popleft() + len(senate))
            else:
                radiant_votes.popleft()
                dire_votes.append(dire_votes.popleft() + len(senate))
            
        return "Radiant" if radiant_votes else "Dire"


print(Solution().predictPartyVictory("RD") == "Radiant")
print(Solution().predictPartyVictory("DR") == "Dire")
print(Solution().predictPartyVictory("RDD") == "Dire")
print(Solution().predictPartyVictory("RDDR") == "Radiant")
print(Solution().predictPartyVictory("DRRD") == "Dire")
print(Solution().predictPartyVictory("DDDDRRDDDRDRDRRDDRDDDRDRRRRDRRRRRDRDDRDDRRDDRRRDDRRRDDDDRRRRRRRDDRRRDDRDDDRRRDRDDRDDDRRDRRDRRRDRDRDR") == "Dire")
