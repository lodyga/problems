class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: greedy, sorting
    * @param {} costs
    * @return {}
    */
   twoCitySchedCost(costs) {
      costs.sort((a, b) => (a[0] - a[1]) - (b[0] - b[1]));
      const half = parseInt(costs.length / 2);
      let res = 0;

      for (let index = 0; index < half; index++) {
         res += costs[index][0];
      }
      
      for (let index = half; index < costs.length; index++) {
         res += costs[index][1];
      }

      return res
   };
}


const twoCitySchedCost = new Solution().twoCitySchedCost;
console.log(new Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]) === 110)
console.log(new Solution().twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]) === 1859)
console.log(new Solution().twoCitySchedCost([[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]) === 3086)
