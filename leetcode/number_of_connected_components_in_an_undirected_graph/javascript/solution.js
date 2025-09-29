import { Queue } from "@datastructures-js/queue";

class DSU {
   constructor(nodeCount) {
      this.rank = Array(nodeCount).fill(1);
      this.parents = Array.from({ length: nodeCount }, (_, node) => node);
      this.size = nodeCount;
   }

   find(node) {
      while (node !== this.parents[node]) {
         this.parents[node] = this.parents[this.parents[node]];
         node = this.parents[node];
      }
      return node
   }

   union(u, v) {
      const pu = this.find(u);
      const pv = this.find(v);

      if (pu === pv)
         return
      else if (this.rank[pu] >= this.rank[pv]) {
         this.rank[pu] += this.rank[pv];
         this.parents[pv] = pu;
      } else {
         this.rank[pv] += this.rank[pu];
         this.parents[pu] = pv;
      }
      this.size -= 1
   }
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: dfs, recursion, graph, dsu
    * DSU
    * @param {number} nodeCount
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(nodeCount, edges) {
      const dsu = new DSU(nodeCount);
      for (const [u, v] of edges) {
         dsu.union(u, v)
      }
      return dsu.size
   };
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: dfs, recursion, graph, dsu
    * DFS
    * @param {number} nodeCount
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(nodeCount, edges) {
      const adjs = new Map();
      for (let node = 0; node < nodeCount; node++) {
         adjs.set(node, new Set());
      }
      for (const [u, v] of edges) {
         adjs.set(u, adjs.get(u).add(v));
         adjs.set(v, adjs.get(v).add(u));
      }

      const visited = new Set();
      let components = 0;

      const dfs = (node) => {
         if (visited.has(node))
            return

         visited.add(node);

         for (const adjNode of adjs.get(node))
            dfs(adjNode);
      };
      for (let node = 0; node < nodeCount; node++) {
         if (!visited.has(node)) {
            dfs(node)
            components++;
         }
      }
      return components
   };
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: dfs, recursion, graph, dsu
    * BFS
    * @param {number} nodeCount
    * @param {number[][]} edges
    * @return {}
    */
   countComponents(nodeCount, edges) {
      const adjs = new Map();
      for (let node = 0; node < nodeCount; node++) {
         adjs.set(node, new Set());
      }
      for (const [u, v] of edges) {
         adjs.set(u, adjs.get(u).add(v));
         adjs.set(v, adjs.get(v).add(u));
      }

      const visited = new Set();
      let components = 0;

      const bfs = (node) => {
         const queue = new Queue([node]);

         while (!queue.isEmpty()) {
            const node = queue.dequeue();
            visited.add(node);
            for (const adjNode of adjs.get(node))
               if (!visited.has(adjNode))
                  queue.enqueue(adjNode);
         }
      };
      for (let node = 0; node < nodeCount; node++) {
         if (!visited.has(node)) {
            bfs(node)
            components++;
         }
      }
      return components
   };
}
const countComponents = new Solution().countComponents;


console.log(new Solution().countComponents(3, [[0, 1], [0, 2]]) === 1)
console.log(new Solution().countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]) === 2)