class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags: Iterative DFS with Backtracking
    * Smallest → Largest
    * @param {number[]} numbers
    * @return {number[][]}
    */
   subsetsWithDup(numbers) {
      const subset = [];
      const subsetList = [];

      function dfs(start) {
         subsetList.push(subset.slice());
         
         for (let index = start; index < numbers.length; index++) {
            if (
               index > start &&
               numbers[index] === numbers[index - 1]
            ) continue
            subset.push(numbers[index]);
            dfs(index + 1);
            subset.pop();
         }
      }

      dfs(0)
      return subsetList
   };
}


class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking
    * Largest → Smallest
    * @param {number[]} numbers
    * @return {number[][]}
    */
   subsetsWithDup(numbers) {
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
         if (
            index + 1 < numbers.length && 
            numbers[index] === numbers[index + 1]
         ) {
            index++;
         }
         dfs(index + 1);
      }
      dfs(0);
      return subsetList
   };
}


console.log(new Solution().subsetsWithDup([0]), [[], [0]])
console.log(new Solution().subsetsWithDup([5, 5]), [[], [5], [5, 5]])
console.log(new Solution().subsetsWithDup([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
console.log(new Solution().subsetsWithDup([4, 4, 4, 1, 4]), [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])