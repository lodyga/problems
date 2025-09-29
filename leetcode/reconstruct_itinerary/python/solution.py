class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        """
        Time complexity: O(E2)
        Auxiliary space complexity: O(E)
        Tags: dfs, recursion, graph
        """
        tickets.sort()
        adjs = {}
        for source, destination in tickets:
            if source not in adjs:
                adjs[source] = []
            adjs[source].append(destination)

        flight_path = ["JFK"]

        def dfs(city):
            if len(flight_path) == len(tickets) + 1:
                return True
            elif not adjs[city]:
                return False

            # Create a copy of adjs to remove used tickets from orginal adjs.
            pruned_adjs = adjs[city].copy()
            for index, adj_city in enumerate(pruned_adjs):
                adjs[city].pop(index)
                flight_path.append(adj_city)
                if dfs(adj_city):
                    return True
                adjs[city].insert(index, adj_city)
                flight_path.pop()

            return False

        dfs("JFK")
        return flight_path


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
print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "JFK"], ["ATL", "AAA"], ["AAA", "ATL"], ["ATL", "BBB"], ["BBB", "ATL"], ["ATL", "CCC"], ["CCC", "ATL"], ["ATL", "DDD"], ["DDD", "ATL"], ["ATL", "EEE"], ["EEE", "ATL"], ["ATL", "FFF"], ["FFF", "ATL"], ["ATL", "GGG"], ["GGG", "ATL"], ["ATL", "HHH"], ["HHH", "ATL"], ["ATL", "III"], ["III", "ATL"], ["ATL", "JJJ"], ["JJJ", "ATL"], ["ATL", "KKK"], ["KKK", "ATL"], ["ATL", "LLL"], ["LLL", "ATL"], ["ATL", "MMM"], ["MMM", "ATL"], ["ATL", "NNN"], ["NNN", "ATL"]]) == ["JFK", "SFO", "JFK", "ATL", "AAA", "ATL", "BBB", "ATL", "CCC", "ATL", "DDD", "ATL", "EEE", "ATL", "FFF", "ATL", "GGG", "ATL", "HHH", "ATL", "III", "ATL", "JJJ", "ATL", "KKK", "ATL", "LLL", "ATL", "MMM", "ATL", "NNN", "ATL"])