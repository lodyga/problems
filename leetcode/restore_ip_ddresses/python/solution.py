class Solution:
    def restoreIpAddresses(self, nums: str) -> list[str]:
        """
        Time complexity: O(1)
            O(3**4)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: list, string
            A: backtracking
        """
        if len(nums) < 4 or len(nums) > 12:
            return []
        
        ip = []
        ips = []

        def backtrack(index):
            if index == len(nums) and len(ip) == 4:
                ips.append(".".join(ip))
                return
            elif index == len(nums) or len(ip) == 4:
                return

            digit = nums[index]

            # one digit number
            ip.append(digit)
            backtrack(index + 1)
            ip.pop()

            # two digit number
            if index + 1 < len(nums) and digit > "0":
                ip.append(nums[index: index + 2])
                backtrack(index + 2)
                ip.pop()

            # three digit number
            if (
                index + 2 < len(nums) and
                (
                    digit == "1" or
                    (digit == "2" and nums[index + 1] <= "4") or
                    (digit == "2" and nums[index + 1] == "5" 
                     and nums[index + 2] <= "5")
                )
            ):
                ip.append(nums[index: index + 3])
                backtrack(index + 3)
                ip.pop()

        backtrack(0)
        return ips


print(sorted(Solution().restoreIpAddresses("25525511135")) == sorted(["255.255.11.135", "255.255.111.35"]))
print(sorted(Solution().restoreIpAddresses("0000")) == sorted(["0.0.0.0"]))
print(sorted(Solution().restoreIpAddresses("101023")) == sorted(["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]))
print(sorted(Solution().restoreIpAddresses("000256")) == sorted([]))
print(sorted(Solution().restoreIpAddresses("02852")) == (["0.2.8.52", "0.2.85.2", "0.28.5.2"]))
