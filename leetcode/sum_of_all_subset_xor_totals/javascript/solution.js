class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking
    * @param {number[]} numbers
    * @return {number}
    */
   subsetXORSum(numbers) {
      const subset = [];
      const xoredList = []

      function dfs(index) {
         if (index === numbers.length) {
            xoredList.push(getXorSum())
            return
         }

         subset.push(numbers[index]);
         dfs(index + 1)
         subset.pop();
         dfs(index + 1)
      }
      dfs(0)
      return xoredList.reduce((sum, number) => sum + number)

      function getXorSum() {
         return subset.reduce((xorSum, number) => xorSum ^ number, 0)
      }
   };
}
const subsetXORSum = new Solution().subsetXORSum;


console.log(new Solution().subsetXORSum([1, 3]), 6)
console.log(new Solution().subsetXORSum([5, 1, 6]), 28)
console.log(new Solution().subsetXORSum([3, 4, 5, 6, 7, 8]), 480)