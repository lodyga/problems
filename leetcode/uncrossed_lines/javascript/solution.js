class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * dp, top-down with memoization as hash map
    * @param {number[]} numbers1
    * @param {number[]} numbers2
    * @return {number}
    */
   maxUncrossedLines(numbers1, numbers2) {
      const memo = new Map();
      return dfs(0, 0);

      function dfs(index1, index2) {
         const index = `${index1},${index2}`;
         if (
            index1 === numbers1.length ||
            index2 === numbers2.length
         ) {
            return 0
         } else if (memo.has(index)) {
            return memo.get(index)
         }

         if (numbers1[index1] === numbers2[index2]) {
            memo.set(index, dfs(index1 + 1, index2 + 1) + 1);
         } else {
            memo.set(index,
               Math.max(
                  dfs(index1 + 1, index2),
                  dfs(index1, index2 + 1)
               )
            );
         }
         return memo.get(index)
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * dp, top-down with memoization as array
    * @param {number[]} numbers1
    * @param {number[]} numbers2
    * @return {number}
    */
   maxUncrossedLines(numbers1, numbers2) {
      const memo = Array.from({ length: numbers1.length }, () => Array(numbers2.length).fill(null));
      return dfs(0, 0);

      function dfs(index1, index2) {
         if (
            index1 === numbers1.length ||
            index2 === numbers2.length
         ) {
            return 0
         } else if (memo[index1][index2] !== null) {
            return memo[index1][index2]
         }

         if (numbers1[index1] === numbers2[index2]) {
            memo[index1][index2] = dfs(index1 + 1, index2 + 1) + 1;
         } else {
            memo[index1][index2] = Math.max(
               dfs(index1 + 1, index2),
               dfs(index1, index2 + 1)
            );
         }
         return memo[index1][index2]
      }
   };
}


class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags: brute-force, tle
    * @param {number[]} numbers1
    * @param {number[]} numbers2
    * @return {number}
    */
   maxUncrossedLines(numbers1, numbers2) {
      return dfs(0, 0);

      function dfs(index1, index2) {
         if (
            index1 === numbers1.length ||
            index2 === numbers2.length
         ) {
            return 0
         }

         let memo;
         if (numbers1[index1] === numbers2[index2]) {
            memo = dfs(index1 + 1, index2 + 1) + 1;
         } else {
            memo = Math.max(
               dfs(index1 + 1, index2),
               dfs(index1, index2 + 1)
            );
         }
         return memo
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * dp, bottom-up
    * @param {number[]} numbers1
    * @param {number[]} numbers2
    * @return {number}
    */
   maxUncrossedLines(numbers1, numbers2) {
      const cache = Array.from({ length: numbers1.length + 1}, () => Array(numbers2.length + 1).fill(0));

      for (let index1 = numbers1.length - 1; index1 >= 0; index1--) {
         for (let index2 = numbers2.length - 1; index2 >= 0; index2--) {
            if (numbers1[index1] === numbers2[index2]) {
               cache[index1][index2] = cache[index1 + 1][index2 + 1] + 1;
            } else {
               cache[index1][index2] = Math.max(
                  cache[index1 + 1][index2],
                  cache[index1][index2 + 1]
               );
            }
         }
      }
      return cache[0][0]
   };
}



console.log(new Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4]) === 2)
console.log(new Solution().maxUncrossedLines([1, 5, 6], [5, 6]) === 2)
console.log(new Solution().maxUncrossedLines([5, 6], [1, 5, 6]) === 2)
console.log(new Solution().maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) === 3)
console.log(new Solution().maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) === 2)
console.log(new Solution().maxUncrossedLines([4, 1, 2, 5, 1, 5, 3, 4, 1, 5], [3, 1, 1, 3, 2, 5, 2, 4, 1, 3, 2, 2, 5, 5, 3, 5, 5, 1, 2, 1]) === 7)
console.log(new Solution().maxUncrossedLines([5, 1, 2, 5, 1, 2, 2, 3, 1, 1, 1, 1, 1, 3, 1], [2, 5, 1, 3, 4, 5, 5, 2, 2, 4, 5, 2, 2, 3, 1, 4, 5, 3, 2, 4, 5, 2, 4, 4, 2, 2, 2, 1, 3, 1]) === 11)