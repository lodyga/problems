class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        Time complexity: O(n*m)
            n: emails len
            m: avg email len
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: hash set
            A: iteration
        """
        email_set = set()

        for email in emails:
            local_name, host_name = email.split("@")
            local_prefix = []

            for char in local_name:
                if char in "+":
                    break
                elif char != ".":
                    local_prefix.append(char)

            email_set.add((tuple(local_prefix), host_name))

        return len(email_set)


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        Time complexity: O(n*m)
            n: emails len
            m: avg email len
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: hash set
            A: iteration
        """
        email_set = set()

        for emial in emails:
            local = []
            index = 0

            while True:
                char = emial[index]
                if char == ".":
                    index += 1
                    continue
                elif char == "@":
                    domain = emial[index + 1: ]
                    break
                elif char == "+":
                    while emial[index + 1] != "@":
                        if char not in ".+":
                            local.append(char)
                        index += 1
                else:
                    local.append(char)
                index += 1

            email_set.add((tuple(local), domain))

        return len(email_set)


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        Time complexity: O(n*m)
            n: emails len
            m: avg email len
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: hash set
            A: iteration
        """
        email_set = set()

        for emial in emails:
            local = []
            index = 0

            while emial[index] not in "@+":
                if emial[index] != ".":
                    local.append(emial[index])
                index += 1

            while emial[index] != "@":
                index += 1

            domain = emial[index + 1:]
            email_set.add((tuple(local), domain))

        return len(email_set)


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        Time complexity: O(n*m)
            n: emails len
            m: avg email len
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: hash set
            A: iteration
        """
        email_set = set()

        for emial in emails:
            local_name, domain = emial.split("@")
            local_prefix = []

            for letter in local_name:
                if letter == ".":
                    continue
                elif letter == "+":
                    break
                else:
                    local_prefix.append(letter)

            email_set.add("".join(local_prefix) + "@" + domain)

        return len(email_set)


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        Time complexity: O(n*m)
            n: emails len
            m: avg email len
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: hash set
            A: iteration, regex
        """
        import re
        email_set = set()

        for emial in emails:
            name, domain = emial.split("@")

            # remove "." from the name
            clean_name = re.sub(r"\.", "", name)

            # remove all after "+" in the name
            clean_name = re.search(r"(\w+)(\+?)", clean_name).group(1)

            email_set.add(clean_name + "@" + domain)

        return len(email_set)


print(Solution().numUniqueEmails(["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]) == 2)
print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]) == 2)
print(Solution().numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]) == 3)
