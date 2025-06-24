class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {number[][]} questions
    * @return {number}
    */
   mostPoints(questions) {
      const memo = new Map();
      return dfs(0)

      function dfs(index) {
         if (index >= questions.length) {
            return 0
         } else if (memo.has(index)) {
            return memo.get(index)
         }

         const [points, brainpower] = questions[index];

         memo.set(index,
            Math.max(
               dfs(index + 1),
               points + dfs(index + brainpower + 1)
            )
         );

         return memo.get(index)
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as array
    * @param {number[][]} questions
    * @return {number}
    */
   mostPoints(questions) {
      const memo = Array(questions.length).fill(null);
      return dfs(0)

      function dfs(index) {
         if (index >= questions.length) {
            return 0
         } else if (memo[index] !== null) {
            return memo[index]
         }

         const [points, brainpower] = questions[index];

         memo[index] = Math.max(
            dfs(index + 1),
            points + dfs(index + brainpower + 1)
         );

         return memo[index] 
      }
   };
}


class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags: brute-force, tle
    * @param {number[][]} questions
    * @return {number}
    */
   mostPoints(questions) {
      return dfs(0)

      function dfs(index) {
         if (index >= questions.length) {
            return 0
         }

         const [points, brainpower] = questions[index];

         const memo = Math.max(
            dfs(index + 1),
            points + dfs(index + brainpower + 1)
         );

         return memo 
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up with tabulation as array
    * @param {number[][]} questions
    * @return {number}
    */
   mostPoints(questions) {
      const cache = Array(questions.length + 1).fill(0);

      for (let index = questions.length - 1; index >= 0; index--) {
         const [points, brainpower] = questions[index];
         const skip = index + brainpower + 1;

         if (skip < questions.length) {
            cache[index] = Math.max(cache[index + 1], points + cache[skip])
         } else {
            cache[index] = Math.max(cache[index + 1], points + 0)
         }
      }
      return cache[0]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up with tabulation as hash map
    * @param {number[][]} questions
    * @return {number}
    */
   mostPoints(questions) {
      const cache = new Map([[questions.length, 0]]);

      for (let index = questions.length - 1; index >= 0; index--) {
         const [points, brainpower] = questions[index];
         const skip = index + brainpower + 1;
         const cumulated_points = points + (skip < questions.length ? cache.get(skip) : 0);

         cache.set(
            index,
            Math.max(cache.get(index + 1), cumulated_points)
         );

      }
      return cache.get(0)
   };
}


console.log(new Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) === 5)
console.log(new Solution().mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) === 7)
console.log(new Solution().mostPoints([[72, 5], [36, 5], [95, 5], [50, 1], [62, 1], [14, 3], [72, 5], [86, 2], [43, 3], [51, 3], [14, 1], [91, 5], [47, 4], [72, 4], [63, 5], [40, 3], [68, 1], [8, 3], [84, 5], [7, 5], [40, 1], [35, 3], [66, 2], [39, 5], [40, 1], [92, 3], [67, 5], [34, 3], [84, 4], [75, 5], [6, 1], [71, 3], [77, 3], [25, 3], [53, 3], [32, 3], [88, 5], [18, 2], [21, 3], [78, 2], [69, 5], [45, 4], [94, 2], [70, 1], [85, 2], [7, 2], [68, 4], [71, 4], [57, 2], [12, 5], [53, 5], [51, 3], [46, 1], [28, 3]]) === 845)