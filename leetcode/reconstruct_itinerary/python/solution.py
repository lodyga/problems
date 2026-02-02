class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        """
        Time complexity: O(V*E)
        Auxiliary space complexity: O(V*E)
        Tags:
            DS: hash map, list
            A: backtracking, sorting
            Model: graph
        """
        N = len(tickets)
        tickets.sort(reverse=True)
        next_cities = {src: [] for src, _ in tickets}
        
        for src, dst in tickets:
            next_cities[src].append(dst)

        flight_path = ["JFK"]
        
        def backtrack(city):
            if len(flight_path) == N + 1:
                return True
            
            next_cities_copy = next_cities[city]
            for index in range(len(next_cities_copy) - 1, -1, -1):
                next_city = next_cities[city].pop(index)
                flight_path.append(next_city)

                if backtrack(next_city):
                    return True

                flight_path.pop()
                next_cities[city].insert(index, next_city)

        backtrack("JFK")
        return flight_path


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        """
        Time complexity: O(ElogE)
        Auxiliary space complexity: O(E)
        Tags:
            DS: hash map, list
            A: post-order dfs on edges, Hierholzer
            Model: graph
        """
        tickets.sort(reverse=True)
        next_cities = {}
        
        for src, dst in tickets:
            if src not in next_cities:
                next_cities[src] = []
            next_cities[src].append(dst)

        flight_path = []
        
        def dfs(city):
            while next_cities.get(city, None):
                next_city = next_cities[city].pop()
                dfs(next_city)
            
            flight_path.append(city)

        dfs("JFK")
        flight_path.reverse()
        return flight_path



print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"])
print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])
print(Solution().findItinerary([["JFK", "SFO"], ["SFO", "JFK"], ["JFK", "ATL"], ["Y2K", "ATL"], ["ATL", "Y2K"]]) == ["JFK", "SFO", "JFK", "ATL", "Y2K", "ATL"])
print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "JFK"], ["ATL", "AAA"], ["AAA", "ATL"], ["ATL", "BBB"], ["BBB", "ATL"], ["ATL", "CCC"], ["CCC", "ATL"], ["ATL", "DDD"], ["DDD", "ATL"], ["ATL", "EEE"], ["EEE", "ATL"], ["ATL", "FFF"], ["FFF", "ATL"], ["ATL", "GGG"], ["GGG", "ATL"], ["ATL", "HHH"], ["HHH", "ATL"], ["ATL", "III"], ["III", "ATL"], ["ATL", "JJJ"], ["JJJ", "ATL"], ["ATL", "KKK"], ["KKK", "ATL"], ["ATL", "LLL"], ["LLL", "ATL"], ["ATL", "MMM"], ["MMM", "ATL"], ["ATL", "NNN"], ["NNN", "ATL"]]) == ["JFK", "SFO", "JFK", "ATL", "AAA", "ATL", "BBB", "ATL", "CCC", "ATL", "DDD", "ATL", "EEE", "ATL", "FFF", "ATL", "GGG", "ATL", "HHH", "ATL", "III", "ATL", "JJJ", "ATL", "KKK", "ATL", "LLL", "ATL", "MMM", "ATL", "NNN", "ATL"])
