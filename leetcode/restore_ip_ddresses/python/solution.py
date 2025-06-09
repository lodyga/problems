class Solution:
    def restoreIpAddresses(self, numbers: str) -> list[str]:
        """
        Time complexity: O(1)
            The recursion tree is bounded by 3**4 and validation within each call is O(1).
        Auxiliary space complexity: O(1)
        Tags: backtracking
        """
        if (len(numbers) < 4 or
                len(numbers) > 12):
            return []

        ip = []
        ip_list = []

        def dfs(index):
            if index == len(numbers) and len(ip) == 4:
                ip_list.append(".".join(ip))
                return
            elif index == len(numbers) or len(ip) >= 4:
                return

            # one digit number
            ip.append(numbers[index])
            dfs(index + 1)
            ip.pop()

            # two digit number
            if index + 1 < len(numbers) and (numbers[index] > "0"):
                ip.append(numbers[index: index + 2])
                dfs(index + 2)
                ip.pop()

            # three digit number
            if (index + 2 < len(numbers) and
               ((numbers[index] == "1") or
                (numbers[index] == "2" and numbers[index + 1] < "5") or
                (numbers[index] == "2" and numbers[index + 1] == "5" and numbers[index + 2] <= "5")
            )):
                ip.append(numbers[index: index + 3])
                dfs(index + 3)
                ip.pop()

        dfs(0)
        return ip_list


print(Solution().restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"])
print(Solution().restoreIpAddresses("0000") == ["0.0.0.0"])
print(Solution().restoreIpAddresses("101023") == ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])
print(Solution().restoreIpAddresses("000256") == [])
print(Solution().restoreIpAddresses("02852") == ["0.2.8.52", "0.2.85.2", "0.28.5.2"])