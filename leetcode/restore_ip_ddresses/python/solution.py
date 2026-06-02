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
        N = len(nums)

        if N < 4 or N > 12:
            return []

        ip_address = []
        res = []

        def backtrack(start, counter):
            if start == N and counter == 4:
                res.append(".".join(ip_address))
                return
            elif start == N or counter == 4:
                return

            for idx in range(start, min(start + 3, N)):
                num = nums[start: idx + 1]

                if (
                    (len(num) > 1 and num[0] == "0")
                    or int(num) > 255
                ):
                    continue

                ip_address.append(num)
                backtrack(idx + 1, counter + 1)
                ip_address.pop()

        backtrack(0, 0)
        return res


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
        N = len(nums)

        if N < 4 or N > 12:
            return []

        ip = []
        res = []

        def backtrack(idx):
            if idx == N and len(ip) == 4:
                res.append(".".join(ip))
                return
            elif idx == N or len(ip) == 4:
                return

            digit = nums[idx]

            # one digit number
            ip.append(digit)
            backtrack(idx + 1)
            ip.pop()

            # two digit number
            if idx + 1 < N and digit > "0":
                ip.append(nums[idx: idx + 2])
                backtrack(idx + 2)
                ip.pop()

            # three digit number
            if (
                idx + 2 < N
                and (
                    digit == "1"
                    or (digit == "2" and nums[idx + 1] <= "4")
                    or (digit == "2" and nums[idx + 1] == "5"
                        and nums[idx + 2] <= "5")
                )
            ):
                ip.append(nums[idx: idx + 3])
                backtrack(idx + 3)
                ip.pop()

        backtrack(0)
        return res


print(sorted(Solution().restoreIpAddresses("25525511135")) == sorted(["255.255.11.135", "255.255.111.35"]))
print(sorted(Solution().restoreIpAddresses("0000")) == sorted(["0.0.0.0"]))
print(sorted(Solution().restoreIpAddresses("101023")) == sorted(["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]))
print(sorted(Solution().restoreIpAddresses("000256")) == sorted([]))
print(sorted(Solution().restoreIpAddresses("02852")) == (["0.2.8.52", "0.2.85.2", "0.28.5.2"]))
