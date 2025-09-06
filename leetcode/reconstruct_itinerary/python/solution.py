from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        """
        Time complexity: O(ElogE)
        Auxiliary space complexity: O(E)
        Tags: Hierholzer alg
        """
        adj = defaultdict(list)
        tickets.sort(reverse=True)

        for src, dst in tickets:
            adj[src].append(dst)

        path = []

        def dfs(src):            
            while adj[src]:
                next_dest = adj[src].pop()
                dfs(next_dest)
            path.append(src)

        dfs("JFK")
        path.reverse()
        return path


print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"])
print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])
print(Solution().findItinerary([["JFK", "SFO"], ["SFO", "JFK"], ["JFK", "ATL"], ["Y2K", "ATL"], ["ATL", "Y2K"]]) == ["JFK", "SFO", "JFK", "ATL", "Y2K", "ATL"])