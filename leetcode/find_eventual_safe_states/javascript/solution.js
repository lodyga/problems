class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: DFS with memoization, cycle detection
    *     Model: graph
    * @param {number[][]} graph
    * @return {number[]}
    */
   eventualSafeNodes(graph) {
      // None: not visited, True: safe/terminal node, False: unsafe/visiting stack node
      const isNodeSafe = Array(graph.length);

      const dfs = (node) => {
         if (isNodeSafe[node] !== undefined)
            return isNodeSafe[node]

         isNodeSafe[node] = false;

         for (const nextNode of graph[node])
            if (!dfs(nextNode))
               return 0

         isNodeSafe[node] = true;
         return true
      }
      const res = [];
      for (let node = 0; node < graph.length; node++)
         if (dfs(node))
            res.push(node)

      return res
   };
}


const eventualSafeNodes = new Solution().eventualSafeNodes;
console.log(new Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]).toString() === [2, 4, 5, 6].toString())
console.log(new Solution().eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]).toString() === [4].toString())
console.log(new Solution().eventualSafeNodes([[1, 3, 4, 5], [], [], [], [], [2, 4]]).toString() === [0, 1, 2, 3, 4, 5].toString())
