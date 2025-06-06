class Solution {
   /**
    * Time complexity: O(2^n)
    *     O(2^numbers)
    * Auxiliary space complexity: O(n)
    * Tags: backtracking
    * @param {number} n
    * @param {number} k
    * @return {number[][]}
    */
   combine(n, k) {
      const combination = [];
      const combinationList = [];
      const numbers = Array.from({length:n}, (n, k) => k + 1);
      dfs(0)
      return combinationList

      function dfs(index) {
         if (combination.length === k) {
            combinationList.push(combination.slice());
            return
         } else if (index === n)
            return
         
         combination.push(numbers[index]);
         dfs(index + 1);
         combination.pop();
         dfs(index + 1);
      }
   };
}
const combine = new Solution().combine;


console.log(new Solution().combine(1, 1), [[1]])
console.log(new Solution().combine(2, 2), [[1, 2]])
console.log(new Solution().combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])