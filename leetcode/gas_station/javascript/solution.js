class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} gas
    * @param {number[]} cost
    * @return {number}
    */
   canCompleteCircuit(gas, cost) {
      if (gas.reduce((total, value) => total + value, 0) < cost.reduce((total, value) => total + value, 0)) {
         return - 1
      }
      let start = 0;
      let gasTank = 0;

      for (let index = 0; index < gas.length; index++) {
         gasTank += gas[index] - cost[index];
         if (gasTank < 0) {
            gasTank = 0;
            start = index + 1;
         }
      }
      return start
   };
}


const canCompleteCircuit = new Solution().canCompleteCircuit;
console.log(new Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) === 3)
console.log(new Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) === -1)
console.log(new Solution().canCompleteCircuit([1, 2, 3, 4],  [2, 2, 4, 1]) === 3)
console.log(new Solution().canCompleteCircuit([3, 1, 1],  [1, 2, 2]) === 0)
