class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, array
    *     A: DFS
    *     Model: graph
    * @param {number[][]} roads
    * @param {number} seats
    * @return {}
    */
   minimumFuelCost(roads, seats) {
      if (roads.length === 0) {
         return 0
      }
      
      const adjs = new Map();
      let fuel = 0;

      for (const [u, v] of roads) {
         if (!adjs.has(u))
            adjs.set(u, []);
         if (!adjs.has(v))
            adjs.set(v, []);
         
         adjs.get(u).push(v);
         adjs.get(v).push(u);
      }
         
      const dfs = (node, prevNode) => {
         let totalPassengers = 1;

         for (const nextNode of adjs.get(node)) {
            if (nextNode !== prevNode) {
               const passengers = dfs(nextNode, node);
               fuel += Math.ceil(passengers / seats);
               totalPassengers += passengers;
            }
         }

         return totalPassengers
      };

      dfs(0, -1)
      return fuel
   };
}


const minimumFuelCost = new Solution().minimumFuelCost;
console.log(new Solution().minimumFuelCost([[0, 1]], 1) === 1)
console.log(new Solution().minimumFuelCost([[0, 1], [0, 2]], 1) === 2)
console.log(new Solution().minimumFuelCost([[0, 1], [1, 2]], 1) === 3)
console.log(new Solution().minimumFuelCost([[0, 1], [1, 2]], 2) === 2)
console.log(new Solution().minimumFuelCost([[0, 1], [0, 2], [2, 3]], 2) === 3)
console.log(new Solution().minimumFuelCost([[0, 1], [1, 2], [2, 3]], 1) === 6)
console.log(new Solution().minimumFuelCost([[0, 3], [0, 1], [1, 2]], 1) === 4)
console.log(new Solution().minimumFuelCost([[0, 1], [0, 2], [1, 3], [1, 4]], 5) === 4)
console.log(new Solution().minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5) === 3)
console.log(new Solution().minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2) === 7)
console.log(new Solution().minimumFuelCost([], 1) === 0)
