class DSU:
    def __init__(self, N) -> None:
        self.size = [1] * N
        self.parent = list(range(N))

    def find(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return
        elif self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        """
        Time complexity: O(m⋅log(m))
        Auxiliary space complexity: O(n + m)
        Tags:
            n: accounts size
            m: emial total count
        """
        N = len(accounts)
        # {email: owner id, }
        email_owner = {}
        dsu = DSU(N)

        # Parse name and emails.
        for user_id, account in enumerate(accounts):
            for email_index in range(1, len(account)):
                email = account[email_index]

                if email in email_owner:
                    prev_user_id = email_owner[email]
                    dsu.union(prev_user_id, user_id)
                else:
                    email_owner[email] = user_id

        # Group emails to appropriate parents.
        email_group = {}
        for email, user_id in email_owner.items():
            parent = dsu.find(user_id)

            if parent not in email_group:
                email_group[parent] = []

            email_group[parent].append(email)

        # Sort emails and prepend name.
        res = []
        for user_id, emails in email_group.items():
            name = accounts[user_id][0]
            res.append([name] + sorted(emails))
        return res


print(sorted(Solution().accountsMerge([["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])) == sorted([["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))
print(sorted(Solution().accountsMerge([["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"], ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]])) == sorted([["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"], ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"], ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"], ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"], ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]]))
print(sorted(Solution().accountsMerge([["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"], ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"], ["David", "David1@m.co", "David2@m.co"]])) == sorted([["David", "David0@m.co", "David1@m.co", "David2@m.co", "David3@m.co", "David4@m.co", "David5@m.co"]]))
print(sorted(Solution().accountsMerge([["Lily", "Lily4@m.co", "Lily5@m.co"], ["Lily", "Lily8@m.co", "Lily9@m.co"], ["Lily", "Lily15@m.co", "Lily16@m.co"], ["Lily", "Lily19@m.co", "Lily20@m.co"], ["Lily", "Lily6@m.co", "Lily7@m.co"], ["Lily", "Lily10@m.co", "Lily11@m.co"], ["Lily", "Lily5@m.co", "Lily6@m.co"], ["Lily", "Lily13@m.co", "Lily14@m.co"], ["Lily", "Lily9@m.co", "Lily10@m.co"], ["Lily", "Lily1@m.co", "Lily2@m.co"], ["Lily", "Lily3@m.co", "Lily4@m.co"], ["Lily", "Lily2@m.co", "Lily3@m.co"], ["Lily", "Lily11@m.co", "Lily12@m.co"], ["Lily", "Lily7@m.co", "Lily8@m.co"], ["Lily", "Lily12@m.co", "Lily13@m.co"], ["Lily", "Lily18@m.co", "Lily19@m.co"], ["Lily", "Lily17@m.co", "Lily18@m.co"], ["Lily", "Lily16@m.co", "Lily17@m.co"], ["Lily", "Lily14@m.co", "Lily15@m.co"], ["Lily", "Lily0@m.co", "Lily1@m.co"]])) == sorted([["Lily", "Lily0@m.co", "Lily10@m.co", "Lily11@m.co", "Lily12@m.co", "Lily13@m.co", "Lily14@m.co", "Lily15@m.co", "Lily16@m.co", "Lily17@m.co", "Lily18@m.co", "Lily19@m.co", "Lily1@m.co", "Lily20@m.co", "Lily2@m.co", "Lily3@m.co", "Lily4@m.co", "Lily5@m.co", "Lily6@m.co", "Lily7@m.co", "Lily8@m.co", "Lily9@m.co"]]))
