class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking
    * @param {number[]} numbers
    * @return {number[][]}
    */
   subsets(numbers) {
      const subset = [];
      const subsetList = [];

      function dfs(index) {
         if (index === numbers.length) {
            subsetList.push(subset.slice());
            return
         }
         subset.push(numbers[index]);
         dfs(index + 1);
         subset.pop();
         dfs(index + 1);
      }
      
      dfs(0);
      return subsetList
   };
}
const subsets = new Solution().subsets;


class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags: Iterative DFS with Backtracking
    * @param {number[]} numbers
    * @return {number[][]}
    */
   subsets(numbers) {
      const subset = [];
      const subsetList = [];

      function dfs(start) {
         subsetList.push(subset.slice());
         for (let index = start; index < numbers.length; index++) {
            subset.push(numbers[index]);
            dfs(index + 1);
            subset.pop();
         }
      }
      dfs(0);
      return subsetList
   };
}


console.log(new Solution().subsets([0]), [[], [0]])
console.log(new Solution().subsets([1, 2]), [[], [1], [2], [1, 2]])
console.log(new Solution().subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])