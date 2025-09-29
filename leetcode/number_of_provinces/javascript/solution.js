import { Queue } from "@datastructures-js/queue";

class DSU {
   constructor(nodeCounter) {
      this.rank = Array(nodeCounter).fill(1);
      this.parents = Array.from({ length: nodeCounter }, (_, node) => node);
      this.size = nodeCounter;
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


class Solution2 {
   /**
    * Time complexity: O(n2)
    *     n: adjacency matrix len
    * Auxiliary space complexity: O(n)
    * Tags: dfs, recursion, graph, dsu
    * DSU
    * @param {number[][]} connections
    * @return {number}
    */
   findCircleNum(connections) {
      const dsu = new DSU(connections.length);

      for (let row = 0; row < connections.length; row++) {
         for (let col = 0; col < connections.length; col++) {
            if (row > col && connections[row][col])
               dsu.union(row, col);
         }
      }
      return dsu.size
   };
}


class Solution3 {
   /**
    * Time complexity: O(n2)
    *     n: adjacency matrix len
    * Auxiliary space complexity: O(n)
    * Tags: dfs, recursion, graph, dsu
    * DFS
    * @param {number[][]} connections
    * @return {number}
    */
   findCircleNum(connections) {
      const adjs = new Map();
      for (let node = 0; node < connections.length; node++) {
         adjs.set(node, new Set());
      }
      for (let row = 0; row < connections.length; row++) {
         for (let col = 0; col < connections.length; col++) {
            if (row !== col && connections[row][col] === 1) {
               adjs.set(row, adjs.get(row).add(col));
               adjs.set(col, adjs.get(col).add(row));
            }
         }
      }

      const dfs = (node) => {
         if (visited.has(node))
            return

         visited.add(node);

         for (const adjNode of adjs.get(node)) {
            dfs(adjNode);
         }
      };

      let components = 0;
      const visited = new Set();
      for (let node = 0; node < connections.length; node++) {
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
    * Time complexity: O(n2)
    *     n: adjacency matrix len
    * Auxiliary space complexity: O(n)
    * Tags: bfs, dfs, graph, dsu
    * BFS
    * @param {number[][]} connections
    * @return {number}
    */
   findCircleNum(connections) {
      const adjs = new Map();
      for (let node = 0; node < connections.length; node++) {
         adjs.set(node, new Set());
      }
      for (let row = 0; row < connections.length; row++) {
         for (let col = 0; col < connections.length; col++) {
            if (row !== col && connections[row][col] === 1) {
               adjs.set(row, adjs.get(row).add(col));
               adjs.set(col, adjs.get(col).add(row));
            }
         }
      }

      const bfs = (node) => {
         const queue = new Queue([node]);
         
         while (!queue.isEmpty()) {
            const node = queue.dequeue();
            visited.add(node);
            for (const adjNode of adjs.get(node)) {
               if (!visited.has(adjNode))
                  queue.enqueue(adjNode);
            }
         }
      };

      let components = 0;
      const visited = new Set();
      for (let node = 0; node < connections.length; node++) {
         if (!visited.has(node)) {
            bfs(node)
            components++;
         }
      }
      return components
   };
}
const findCircleNum = new Solution().findCircleNum;


console.log(new Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
console.log(new Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)