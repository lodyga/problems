class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: brute-force
    * @param {number[]} gas
    * @param {number[]} cost
    * @return {number}
    */
   canCompleteCircuit(gas, cost) {
      if (gas.reduce((total, value) => total + value, 0) < cost.reduce((total, value) => total + value, 0)) {
         return - 1;
      }

      const N = gas.length;

      for (let start = 0; start < N; start++) {
         let tank = 0;

         for (let idx = start; idx < start + N; idx++) {
            tank += gas[idx % N] - cost[idx % N];

            if (tank < 0) {
               break;
            }
         }

         if (tank >= 0) {
            return start;
         }
      }

      return -1;
   }
}


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
         return - 1;
      }

      const N = gas.length;
      let start = 0;
      let tank = 0;

      for (let idx = 0; idx < 2 * N - 1; idx++) {
         tank += gas[idx % N] - cost[idx % N];

         if (tank < 0) {
            tank = 0;
            start = idx + 1;
            continue;
         }
         else if (idx - start === N - 1) {
            return idx + 1 - N;
         }
      }

      return -1;
   }
}


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
         return - 1;
      }

      let start = 0;
      let tank = 0;

      for (let idx = 0; idx < gas.length; idx++) {
         tank += gas[idx] - cost[idx];

         if (tank < 0) {
            tank = 0;
            start = idx + 1;
         }
      }

      return start;
   }
}


const canCompleteCircuit = new Solution().canCompleteCircuit;
console.log(new Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) === 3)
console.log(new Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) === -1)
console.log(new Solution().canCompleteCircuit([1, 2, 3, 4], [2, 2, 4, 1]) === 3)
console.log(new Solution().canCompleteCircuit([3, 1, 1], [1, 2, 2]) === 0)
