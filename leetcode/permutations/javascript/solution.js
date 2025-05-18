class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking
    * @param {number[]} numbers
    * @return {number[][]}
    */
   permute(numbers) {
      const permutationList = [];

      function dfs(start) {
         if (start === numbers.length) {
            permutationList.push(numbers.slice())
            return
         }
         for (let index = start; index < numbers.length; index++) {
            [numbers[start], numbers[index]] = [numbers[index], numbers[start]];
            dfs(start + 1);
            [numbers[start], numbers[index]] = [numbers[index], numbers[start]];
         }
      }
      dfs(0);
      return permutationList
   };
}


console.log(new Solution().permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
console.log(new Solution().permute([0, 1]), [[0, 1], [1, 0]])
console.log(new Solution().permute([1]), [[1]])