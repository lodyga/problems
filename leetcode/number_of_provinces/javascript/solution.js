import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(n2)
    *     n: adjacency matrix side
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array (graph)
    *     A: multi-source DFS
    * @param {number[][]} isConnected
    * @return {number}
    */
   findCircleNum(isConnected) {
      const N = isConnected.length
      let components = 0;
      const visited = Array(N).fill(false);

      const dfs = (node) => {
         if (visited[node])
            return 0

         visited[node] = true;

         for (let index = 0; index < N; index++) {
            if (
               index !== node &&
               isConnected[node][index]
            )
               dfs(index)
         }
         return 1
      }

      for (let node = 0; node < N; node++)
         components += dfs(node);

      return components
   };

   /**
    * Time complexity: O(n2)
    *     n: adjacency matrix side
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array (graph)
    *     A: multi-source BFS
    * @param {number[][]} isConnected
    * @return {number}
    */
   findCircleNum(isConnected) {
      const N = isConnected.length
      let components = 0;
      const visited = Array(N).fill(false);

      const bfs = (node) => {
         if (visited[node])
            return 0

         const queue = new Queue([node]);

         while (queue.size()) {
            const node = queue.dequeue();
            visited[node] = true;

            for (let index = 0; index < N; index++) {
               if (
                  index !== node &&
                  isConnected[node][index] &&
                  !visited[index]
               )
                  queue.enqueue(index)
            }
         }
         return 1
      }

      for (let node = 0; node < N; node++)
         components += bfs(node)

      return components
   };

   /**
    * Time complexity: O(n2)
    *     n: adjacency matrix side
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array (graph)
    *     A: DSU
    * @param {number[][]} isConnected
    * @return {number}
    */
   findCircleNum(isConnected) {
      const dsu = new DSU(isConnected.length);

      for (let row = 0; row < isConnected.length; row++) {
         for (let col = 0; col < isConnected.length; col++) {
            if (row > col && isConnected[row][col])
               dsu.union(row, col);
         }
      }
      return dsu.components
   };
}


class DSU {
   constructor(N) {
      this.size = Array(N).fill(1);
      this.parent = Array.from({ length: N }, (_, node) => node);
      this.components = N;
   }

   find(node) {
      while (node !== this.parent[node]) {
         this.parent[node] = this.parent[this.parent[node]];
         node = this.parent[node];
      }
      return node
   }

   union(u, v) {
      const pu = this.find(u);
      const pv = this.find(v);

      if (pu === pv)
         return
      else if (this.size[pu] >= this.size[pv]) {
         this.size[pu] += this.size[pv];
         this.parent[pv] = pu;
      } else {
         this.size[pv] += this.size[pu];
         this.parent[pu] = pv;
      }
      this.components -= 1
   }
}


const findCircleNum = new Solution().findCircleNum;
console.log(new Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) === 2)
console.log(new Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) === 3)
console.log(new Solution().findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) === 1)
