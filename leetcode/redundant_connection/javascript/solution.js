class DSU {
   constructor(N) {
      this.size = Array(N).fill(1);
      this.parent = Array.from({ length: N }, (_, node) => node);
   }

   find(node) {
      while (node != this.parent[node]) {
         this.parent[node] = this.parent[this.parent[node]];
         node = this.parent[node];
      }
      return node
   }

   union(u, v) {
      const pu = this.find(u);
      const pv = this.find(v);

      if (pu === pv) 
         return true
      else if (pu >= pv) {
         this.size[pu] += this.size[pv];
         this.parent[pv] = pu;
      } else {
         this.size[pv] += this.size[pu];
         this.parent[pu] = pv;
      }
   }
}


class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: DSU, cycle detection
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
console.log(new Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]).toString() === [2, 3].toString())
console.log(new Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]).toString() === [1, 4].toString())
console.log(new Solution().findRedundantConnection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]).toString() === [2, 5].toString())
