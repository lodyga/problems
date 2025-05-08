class Solution:
    def maxDepth(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        """
        depth = 0
        max_depth = 0

        for chr in text:
            if chr == "(":
                depth += 1
                max_depth = max(max_depth, depth)
            elif chr == ")":
                depth -= 1
            
        return max_depth


print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"), 3)
print(Solution().maxDepth("(1)+((2))+(((3)))"), 3)
print(Solution().maxDepth("()(())((()()))"), 3)