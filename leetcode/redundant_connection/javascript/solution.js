class DSU {
   constructor(node_count) {
      this.rank = Array(node_count).fill(1);
      this.parents = Array.from({ length: node_count }, (_, node) => node);
   }

   find(node) {
      while (node != this.parents[node]) {
         this.parents[node] = this.parents[this.parents[node]];
         node = this.parents[node];
      }
      return node
   }

   union(u, v) {
      const pu = this.find(u);
      const pv = this.find(v);

      if (pu === pv) 
         return true
      else if (pu >= pv) {
         this.rank[pu] += this.rank[pv];
         this.parents[pv] = pu;
      } else {
         this.rank[pv] += this.rank[pu];
         this.parents[pu] = pv;
      }
      return false
   }
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: dfs, recursion, graph, dsu
    * DSU
    * @param {number[][]} edges
    * @return {number[]}
    */
   findRedundantConnection(edges) {
      const dsu = new DSU(edges.length);
      for (const [u, v] of edges) {
         if (dsu.union(u - 1, v - 1))
            return [u, v]
      }
   };
}
const findRedundantConnection = new Solution().findRedundantConnection;


console.log(new Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]), [2, 3])
console.log(new Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4])
console.log(new Solution().findRedundantConnection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]), [2, 5])