class DSU:
    def __init__(self, n) -> None:
        self.parents = list(range(n))
        self.rank = [1] * n
    
    def find(self, u):
        while u != self.parents[u]:
            self.parents[u] = self.parents[self.parents[u]]
            u = self.parents[u]
        return u

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            pass
        elif self.rank[pu] >= self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parents[pv] = pu
        else:
            self.rank[pv] += self.rank[pu]
            self.parents[pu] = pv


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        """
        Time complexity: O(n2⋅m + ElogE)
        Auxiliary space complexity: O(n)
        Tags: 
        """
        n = len(accounts)
        emails = {node: set() for node in range(len(accounts))}
        names = {}
        dsu = DSU(n)

        # parse, name and emails
        for node, account in enumerate(accounts):
            names[node] = account[0]
            for email in range(1, len(account)):
                emails[node].add(account[email])
        
        # dsu, find parent (index) of every account
        for i in range(n):
            for j in range(n):
                if (
                    i > j and
                    names[i] == names[j] and
                    len(emails[i] | emails[j]) != len(emails[i]) + len(emails[j])
                ):
                    dsu.union(i, j)

        # group emails to appropriate parents
        email_group = {}
        for node in range(n):
            parent = dsu.find(node)
            email_group[parent] = email_group.get(parent, set()) | emails[node]
        
        # sort emails and append name
        output_list = []
        for node in email_group:
            emails = sorted(email_group[node])
            emails.insert(0, names[node])
            output_list.append(emails)
        return output_list


print(sorted(Solution().accountsMerge([["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])) == sorted([["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))
print(sorted(Solution().accountsMerge([["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"], ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]])) == sorted([["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"], ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"], ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"], ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"], ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]]))
print(sorted(Solution().accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]])) == sorted([["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]))
print(sorted(Solution().accountsMerge([["Lily","Lily4@m.co","Lily5@m.co"],["Lily","Lily8@m.co","Lily9@m.co"],["Lily","Lily15@m.co","Lily16@m.co"],["Lily","Lily19@m.co","Lily20@m.co"],["Lily","Lily6@m.co","Lily7@m.co"],["Lily","Lily10@m.co","Lily11@m.co"],["Lily","Lily5@m.co","Lily6@m.co"],["Lily","Lily13@m.co","Lily14@m.co"],["Lily","Lily9@m.co","Lily10@m.co"],["Lily","Lily1@m.co","Lily2@m.co"],["Lily","Lily3@m.co","Lily4@m.co"],["Lily","Lily2@m.co","Lily3@m.co"],["Lily","Lily11@m.co","Lily12@m.co"],["Lily","Lily7@m.co","Lily8@m.co"],["Lily","Lily12@m.co","Lily13@m.co"],["Lily","Lily18@m.co","Lily19@m.co"],["Lily","Lily17@m.co","Lily18@m.co"],["Lily","Lily16@m.co","Lily17@m.co"],["Lily","Lily14@m.co","Lily15@m.co"],["Lily","Lily0@m.co","Lily1@m.co"]])) == sorted([["Lily","Lily0@m.co","Lily10@m.co","Lily11@m.co","Lily12@m.co","Lily13@m.co","Lily14@m.co","Lily15@m.co","Lily16@m.co","Lily17@m.co","Lily18@m.co","Lily19@m.co","Lily1@m.co","Lily20@m.co","Lily2@m.co","Lily3@m.co","Lily4@m.co","Lily5@m.co","Lily6@m.co","Lily7@m.co","Lily8@m.co","Lily9@m.co"]]))
# print(Solution().accountsMerge([["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]), [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
# print(Solution().accountsMerge([["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"], ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]), [["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"], ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"], ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"], ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"], ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]])
# print(Solution().accountsMerge([["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"],["David","David1@m.co","David2@m.co"]]), [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]])
# print(Solution().accountsMerge([["Lily","Lily4@m.co","Lily5@m.co"],["Lily","Lily8@m.co","Lily9@m.co"],["Lily","Lily15@m.co","Lily16@m.co"],["Lily","Lily19@m.co","Lily20@m.co"],["Lily","Lily6@m.co","Lily7@m.co"],["Lily","Lily10@m.co","Lily11@m.co"],["Lily","Lily5@m.co","Lily6@m.co"],["Lily","Lily13@m.co","Lily14@m.co"],["Lily","Lily9@m.co","Lily10@m.co"],["Lily","Lily1@m.co","Lily2@m.co"],["Lily","Lily3@m.co","Lily4@m.co"],["Lily","Lily2@m.co","Lily3@m.co"],["Lily","Lily11@m.co","Lily12@m.co"],["Lily","Lily7@m.co","Lily8@m.co"],["Lily","Lily12@m.co","Lily13@m.co"],["Lily","Lily18@m.co","Lily19@m.co"],["Lily","Lily17@m.co","Lily18@m.co"],["Lily","Lily16@m.co","Lily17@m.co"],["Lily","Lily14@m.co","Lily15@m.co"],["Lily","Lily0@m.co","Lily1@m.co"]]), [["Lily","Lily0@m.co","Lily10@m.co","Lily11@m.co","Lily12@m.co","Lily13@m.co","Lily14@m.co","Lily15@m.co","Lily16@m.co","Lily17@m.co","Lily18@m.co","Lily19@m.co","Lily1@m.co","Lily20@m.co","Lily2@m.co","Lily3@m.co","Lily4@m.co","Lily5@m.co","Lily6@m.co","Lily7@m.co","Lily8@m.co","Lily9@m.co"]])