import re


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        clean_emails = set()
        
        for emial in emails:
            raw_local_name, domain = emial.split("@")
            clean_local_name = []
            
            for letter in raw_local_name:
                if letter == ".":
                    continue
                elif letter == "+":
                    break
                else:
                    clean_local_name.append(letter)
            
            clean_emails.add("".join(clean_local_name) + "@" + domain)

        return len(clean_emails)


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: regex
        """
        clean_emails = set()

        for emial in emails:
            name, domain = emial.split("@")

            # remove "." from the name
            clean_name = re.sub(r"\.", "", name)

            # remove all after "+" in the name
            clean_name = re.search(r"(\w+)(\+?)", clean_name).group(1)

            clean_emails.add(clean_name + "@" + domain)

        return len(clean_emails)


print(Solution().numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]), 2)
print(Solution().numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]), 3)