import heapq


class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        """
        Time complexity: O(k + E)
            O(k + ElogV) -> O(k + E)
            k: text length
            V: vertex count = 26
            E: edges count = 26**2
        Auxiliary space complexity: O(V + E)
        Tags: bfs, iteration, heap, graph
        Dijkstra's alg
        """
        # only direct costs
        initial_costs = {}  # {src: set((cost, dst), ), }
        for src, dst, cst in zip(original, changed, cost):
            if src not in initial_costs:
                initial_costs[src] = set([(0, src)])
            initial_costs[src].add((cst, dst))

        def bfs(letter, target):
            if (letter, target) in cost_cache:
                return cost_cache[(letter, target)]
            
            path = set()
            source_letter = letter
            path_heap = [(0, letter)]
            
            while path_heap:
                cost, letter = heapq.heappop(path_heap)
                if letter == target:
                    # cache current request path
                    cost_cache[source_letter, letter] = cost
                    return cost
                elif letter in path:
                    continue
                elif letter not in initial_costs:
                    continue
                
                # cache all intermediate paths
                cost_cache[source_letter, letter] = cost
                path.add(letter)

                for next_cost, next_letter in initial_costs[letter]:
                    if next_letter not in path:
                        heapq.heappush(path_heap, (cost + next_cost, next_letter))
            
            return -1
        
        total_cost = 0
        # direct and all indirect costs map
        cost_cache = {}  # {(src, trg): cost}
        for s, t in zip(source, target):
            cost = bfs(s, t)
            total_cost += cost

            if cost == -1:
                return -1
            
        return total_cost


print(Solution().minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]) == 28)
print(Solution().minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]) == 12)
print(Solution().minimumCost("abcd", "abce", ["a"], ["e"], [10000]) == -1)
print(Solution().minimumCost("aadbddcabd", "bdcdccbada", ["d","a","a","b","d","b"], ["b","c","d","c","a","d"], [6,10,5,8,11,4]) == -1)