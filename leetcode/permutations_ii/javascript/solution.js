class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n!)
    * Tags: backtracking, hash set
    * @param {number[]} numbers
    * @return {number[][]}
    */
   permuteUnique(numbers) {
      numbers.sort((a, b) => a - b)
      const permutationList = [];
      dfs(0)
      return permutationList

      function dfs(left) {
         if (left === numbers.length - 1) {
            permutationList.push(numbers.slice());
            return
         }

         const uniqueLevelValue = new Set();
         for (let right = left; right < numbers.length; right++) {
            if (uniqueLevelValue.has(numbers[right]))
               continue
            else
               uniqueLevelValue.add(numbers[right]);

            [numbers[left], numbers[right]] = [numbers[right], numbers[left]];
            dfs(left + 1);
            [numbers[left], numbers[right]] = [numbers[right], numbers[left]];
         }
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n!)
    * Tags: backtracking, hash map
    * @param {number[]} numbers
    * @return {number[][]}
    */
   permuteUnique(numbers) {
      const permutation = [];
      const permutationList = [];
      const numberFrequency = new Map();
      for (const number of numbers) {
         numberFrequency.set(number, (numberFrequency.get(number) || 0) + 1);
      }

      dfs()
      return permutationList

      function dfs(left) {
         if (permutation.length === numbers.length) {
            permutationList.push(permutation.slice());
            return
         }
         for (const number of numberFrequency.keys()) {
            if (numberFrequency.get(number)) {
               permutation.push(number);
               numberFrequency.set(number, numberFrequency.get(number) - 1);
               dfs();
               permutation.pop();
               numberFrequency.set(number, numberFrequency.get(number) + 1);
            }
         }

      }
   };
}
class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n!)
    * Tags: backtracking, hash set
    * @param {number[]} numbers
    * @return {number[][]}
    */
   permuteUnique(numbers) {
      const permutationSet = new Set();
      dfs(0)
      return Array.from(permutationSet).map(JSON.parse)

      function dfs(left) {
         if (left === numbers.length - 1) {
            permutationSet.add(JSON.stringify(numbers));
            return
         }

         for (let right = left; right < numbers.length; right++) {
            [numbers[left], numbers[right]] = [numbers[right], numbers[left]];
            dfs(left + 1);
            [numbers[left], numbers[right]] = [numbers[right], numbers[left]];
            
         }
      }
   };
}


const permuteUnique = new Solution().permuteUnique;


console.log(new Solution().permuteUnique([1, 2]), [[1, 2], [2, 1]])
console.log(new Solution().permuteUnique([1, 2, 3]), [[1, 3, 2], [1, 2, 3], [2, 1, 3], [3, 2, 1], [3, 1, 2], [2, 3, 1]])
console.log(new Solution().permuteUnique([1]), [[1]])
console.log(new Solution().permuteUnique([1, 1, 2]), [[1, 2, 1], [2, 1, 1], [1, 1, 2]])
console.log(new Solution().permuteUnique([2, 2, 1, 1]), [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]])