import heapq


class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        """
        Time complexity: O(k + E)
            O(k + ElogV) -> O(k + E)
            k: text length
            V: vertex count = 26
            E: edges count = 26**2
        Auxiliary space complexity: O(E)
            O(E + 26**2)
        Tags:
            DS: heap, hash map, array
            A: greedy, Dijkstra with cache
            Model: graph
        """
        # direct costs only
        # {src: [(dst, cost), ], }
        adjs = {}
        for src, dst, c in zip(original, changed, cost):
            if src not in adjs:
                adjs[src] = []
            adjs[src].append((dst, c))

        def dijkstra(src: int, dst: int) -> int:
            if (src, dst) in cost_cache:
                return cost_cache[src, dst]

            base_src = src
            cost_heap = [(0, src)]
            path = [False] * 26

            while cost_heap:
                cost, src = heapq.heappop(cost_heap)

                if path[ord(src) - ord("a")]:
                    continue

                path[ord(src) - ord("a")] = True

                # cache all intermediate paths
                cost_cache[base_src, src] = cost

                if src == dst:
                    return cost

                if src not in adjs:
                    continue

                for adj_src, adj_cost in adjs[src]:
                    if not path[ord(adj_src) - ord("a")]:
                        heapq.heappush(cost_heap, (adj_cost + cost, adj_src))

            return -1

        total_cost = 0
        # direct and indirect costs cache
        # {src: [(dst, cost), ], }
        cost_cache = {}

        for src, dst in zip(source, target):
            if src == dst:
                continue

            cost = dijkstra(src, dst)
            total_cost += cost

            if cost == -1:
                return -1

        return total_cost


print(Solution().minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]) == 28)
print(Solution().minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]) == 12)
print(Solution().minimumCost("abcd", "abce", ["a"], ["e"], [10000]) == -1)
print(Solution().minimumCost("aadbddcabd", "bdcdccbada", ["d","a","a","b","d","b"], ["b","c","d","c","a","d"], [6,10,5,8,11,4]) == -1)
print(Solution().minimumCost("aabbddccbc", "abbbaabaca", ["a", "b", "c", "b", "a", "d"], ["d", "c", "b", "d", "b", "b"], [3, 8, 7, 6, 7, 10]) == -1)
print(Solution().minimumCost("bcaabaddac", "bdccbdaadc", ["c", "d", "a", "a", "c", "a", "d"], ["a", "a", "d", "b", "d", "c", "c"], [4, 3, 6, 3, 11, 6, 4]) == 40)
