class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        """
        Time complexity: O(n * m)
            n: bank rows
            m: bank cols
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        lasers = 0
        prev_row_lasers = bank[0].count("1")
        for index in range(1, len(bank)):
            row_lasers = bank[index].count("1")
            if row_lasers:
                lasers += prev_row_lasers * row_lasers
                prev_row_lasers = row_lasers
                
        return lasers


print(Solution().numberOfBeams(["11", "11"]) == 4)
print(Solution().numberOfBeams(["011001", "000000", "010100", "001000"]) == 8)
print(Solution().numberOfBeams(["000", "111", "000"]) == 0)