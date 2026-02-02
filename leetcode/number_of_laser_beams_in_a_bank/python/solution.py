class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        """
        Time complexity: O(n*m)
            n: bank row count
            m: bank col count
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        beams = 0
        prev_devices = 0

        for row in bank:
            devices = row.count("1")
            
            if devices:
                beams += prev_devices * devices
                prev_devices = devices

        return beams


print(Solution().numberOfBeams(["11", "11"]) == 4)
print(Solution().numberOfBeams(["000", "111", "000"]) == 0)
print(Solution().numberOfBeams(["011001", "000000", "010100", "001000"]) == 8)
