import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V)
    * Tags:
    *     DS: array (matrix), queue
    *     A: bfs, iteration
    * @param {number[][]} graph
    * @return {boolean}
    */
   isBipartite(graph) {
      const setA = new Set();
      const setB = new Set();

      const bfs = (node) => {
         if (setA.has(node) || setB.has(node)) {
            return true
         }

         let isSetA = true;
         const queue = new Queue([[node, isSetA]]);
         setA.add(node);

         while (queue.size()) {
            const [node, isSetA] = queue.dequeue();
            let currentSet;
            let oppositeSet;

            if (isSetA) {
               currentSet = setA;
               oppositeSet = setB;
            } else {
               currentSet = setB;
               oppositeSet = setA;
            }

            for (const adjNode of graph[node]) {
               if (currentSet.has(adjNode)) {
                  return false
               } else if (oppositeSet.has(adjNode)) {
                  continue
               }

               queue.enqueue([adjNode, !isSetA])
               oppositeSet.add(adjNode);
            }
         }
         return true
      }

      for (let node = 0; node < graph.length; node++) {
         if (bfs(node) === false) {
            return false
         }
      }

      return true
   };
}


const isBipartite = new Solution().isBipartite;
console.log(new Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) === false)
console.log(new Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) === true)
console.log(new Solution().isBipartite([[1], [0, 3], [3], [1, 2]]) === true)
console.log(new Solution().isBipartite([[4], [], [4], [4], [0, 2, 3]]) === true)
console.log(new Solution().isBipartite([[1], [0], [4], [4], [2, 3]]) === true)
console.log(new Solution().isBipartite([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]) === false)
