import { Deque } from "@datastructures-js/deque";


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, array
    *     A: DFS
    *     Model: graph
    * @param {number[]} edges
    * @param {number} node1
    * @param {number} node2
    * @return {number}
    */
   closestMeetingNode(edges, node1, node2) {
      if (node1 === node2) {
         return node1
      }

      const UPPER_BOUND = 10 ** 5;

      const dfs = (node, distMap, dist) => {
         if (
            distMap.has(node) ||
            node === -1
         ) {
            return
         }

         distMap.set(node, dist);
         dfs(edges[node], distMap, dist + 1);
         return distMap
      };

      const dists1 = dfs(node1, new Map(), 0);
      const dists2 = dfs(node2, new Map(), 0);
      let minDist = UPPER_BOUND;
      let res = -1;

      for (let node = 0; node < edges.length; node++) {
         let dist;

         if (dists1.has(node) && dists2.has(node)) {
            dist = Math.max(dists1.get(node), dists2.get(node))
         }

         if (dist < minDist) {
            minDist = dist;
            res = node;
         }
      }

      return res
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: deque, hash map, array
    *     A: BFS
    *     Model: graph
    * @param {number[]} edges
    * @param {number} node1
    * @param {number} node2
    * @return {number}
    */
   closestMeetingNode(edges, node1, node2) {
      if (node1 === node2) {
         return node1
      }

      const UPPER_BOUND = 10 ** 5;

      const bfs = (node) => {
         // {node index: distance from root}
         const distMap = new Map();
         const deq = new Deque([node]);
         let dist = 0;

         while (deq.size()) {
            const node = deq.popFront();
            distMap.set(node, dist);

            if (
               edges[node] !== -1 &&
               !distMap.has(edges[node])
            ) {
               deq.pushBack(edges[node])
            }
            dist++;
         }

         return distMap
      };

      const dists1 = bfs(node1);
      const dists2 = bfs(node2);
      let minDist = UPPER_BOUND;
      let res = -1;

      for (let node = 0; node < edges.length; node++) {
         let dist;

         if (dists1.has(node) && dists2.has(node)) {
            dist = Math.max(dists1.get(node), dists2.get(node))
         }

         if (dist < minDist) {
            minDist = dist;
            res = node;
         }
      }

      return res
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, array
    *     A: graph traversal
    *     Model: graph
    * @param {number[]} edges
    * @param {number} node1
    * @param {number} node2
    * @return {number}
    */
   closestMeetingNode(edges, node1, node2) {
      if (node1 === node2) {
         return node1
      }

      const UPPER_BOUND = 10 ** 5;

      const getDist = (node) => {
         // {node index: distance from root}
         const distMap = new Map();
         let dist = 0;

         while (
            node !== -1 &&
            !distMap.has(node)
         ) {
            distMap.set(node, dist);
            dist++;
            node = edges[node];
         }

         return distMap
      };

      const dists1 = getDist(node1);
      const dists2 = getDist(node2);
      let minDist = UPPER_BOUND;
      let res = -1;

      for (let node = 0; node < edges.length; node++) {
         let dist;

         if (dists1.has(node) && dists2.has(node)) {
            dist = Math.max(dists1.get(node), dists2.get(node))
         }

         if (dist < minDist) {
            minDist = dist;
            res = node;
         }
      }

      return res
   };
}


const closestMeetingNode = new Solution().closestMeetingNode;
console.log(new Solution().closestMeetingNode([2, 2, 3, -1], 0, 1) === 2)
console.log(new Solution().closestMeetingNode([1, 2, -1], 0, 2) === 2)
console.log(new Solution().closestMeetingNode([4, 4, 4, 5, 1, 2, 2], 1, 1) === 1)
console.log(new Solution().closestMeetingNode([9, 8, 7, 0, 5, 6, 1, 3, 2, 2], 1, 6) === 1)
console.log(new Solution().closestMeetingNode([4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6) === 1)
console.log(new Solution().closestMeetingNode([5, -1, 3, 4, 5, 6, -1, -1, 4, 3], 0, 0) === 0)
console.log(new Solution().closestMeetingNode([2, 0, 0], 2, 0) === 0)
