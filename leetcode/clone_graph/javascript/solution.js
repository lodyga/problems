/**
 * Definition for a _Node.
 */
class _Node {
   constructor(val, neighbors) {
      this.val = val === undefined ? null : val;
      this.neighbors = neighbors === undefined ? [] : neighbors;
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dfs, recursion, graph
    * @param {_Node} node
    * @return {_Node}
    */
   cloneGraph(node) {
      const originalToCopy = new Map();
      return node ? dfs(node) : null

      function dfs(node) {
         if (originalToCopy.has(node))
            return originalToCopy.get(node)

         const nodeCopy = new _Node(node.val);
         originalToCopy.set(node, nodeCopy);

         for (const neighbor of node.neighbors) {
            nodeCopy.neighbors.push(dfs(neighbor))
         }
         return nodeCopy
      }
   };

   buildGraph(nodeList) {
      if (nodeList.length === 0) {
         return null
      }
      const indexedNodes = new Map();
      return dfs(0)

      function dfs(index) {
         if (indexedNodes.has(index)) {
            return indexedNodes.get(index)
         }
         const node = new _Node(index + 1);
         indexedNodes.set(index, node);

         for (const value of nodeList[index]) {
            node.neighbors.push(dfs(value - 1));
         }
         return node
      }
   }

   areSame(node1, node2) {
      return node1 === node2
   }

   areEqual(node1, node2) {
      const isNodeEqual = new Map();
      return dfs(node1, node2)

      function dfs(node1, node2) {
         if (isNodeEqual.has(node1.val)) {
            return true
         } else if (node1.neighbors.length !== node2.neighbors.length) {
            return false
         }
         for (let index = 0; index < node1.neighbors.length; index++) {
            if (node1.neighbors[index].val !== node2.neighbors[index].val) {
               return false
            }
         }
         isNodeEqual.set(node1.val, true);

         return node1.neighbors.every((node1, index) => dfs(node1, node2.neighbors[index]))
      }
   }
}


console.log(new Solution().buildGraph([[2, 4], [1, 3], [2, 4], [1, 3]]))
console.log(new Solution().cloneGraph(new Solution().buildGraph([[2, 4], [1, 3], [2, 4], [1, 3]])))
console.log(new Solution().cloneGraph(new Solution().buildGraph([[]])))
console.log(new Solution().cloneGraph(new Solution().buildGraph([])))

const solution = new Solution();
const graph = solution.buildGraph([[2, 4], [1, 3], [2, 4], [1, 3]]);
const cloned_graph = solution.cloneGraph(graph);
console.log(solution.areSame(graph, graph));
console.log(solution.areSame(graph, cloned_graph));
console.log(solution.areEqual(graph, cloned_graph));