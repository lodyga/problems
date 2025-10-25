class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: greedy, two pointers, sorting
        """
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        score = 0
        max_score = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                max_score = max(max_score, score)
                left += 1
            elif score == 0:
                break
            else:
                score -= 1
                power += tokens[right]
                right -= 1
        
        return max_score


print(Solution().bagOfTokensScore([100], 50) == 0)
print(Solution().bagOfTokensScore([200, 100], 150) == 1)
print(Solution().bagOfTokensScore([100, 200, 300, 400], 200) == 2)