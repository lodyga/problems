import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: queue, array, hash set
    *     A: multi-source BFS
    *     Model: graph
    * @param {number} n
    * @param {number[][]} edges
    * @return {number[]}
    */
   findMinHeightTrees(n, edges) {
      if (n === 1) {
         return [0]
      }

      const adjs = Array.from({ length: n }, () => []);
      for (const [u, v] of edges) {
         adjs[u].push(v);
         adjs[v].push(u);
      }

      const leaves = new Queue();
      const degree = adjs.map(value => value.length);
      for (let node = 0; node < adjs.length; node++) {
         const adjNodes = adjs[node];
         if (adjNodes.length === 1)
            leaves.push(node)
      }

      while (n > 2) {
         const len = leaves.size();
         
         for (let index = 0; index < len; index++) {
            const node = leaves.dequeue();
            n--;

            for (const adjNode of adjs[node]) {
               degree[adjNode]--;

               if (degree[adjNode] === 1)
                  leaves.enqueue(adjNode);
            }
         }
      }

      return leaves.toArray()
   };
}


const findMinHeightTrees = new Solution().findMinHeightTrees;
console.log(new Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]).toString() === [1].toString())
console.log(new Solution().findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]).toString() === [3, 4].toString())
console.log(new Solution().findMinHeightTrees(10, [[0, 1], [0, 2], [0, 3], [2, 4], [0, 5], [5, 6], [6, 7], [2, 8], [7, 9]]).toString() === [5].toString())
console.log(new Solution().findMinHeightTrees(1, []).toString() === [0].toString())
