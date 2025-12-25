class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: hash map
    *     A: top-down
    * @param {number[]} nums1
    * @param {number[]} nums2
    * @return {number}
    */
   maxUncrossedLines(nums1, nums2) {
      // {(index1, index2): connection count}
      const memo = new Map();

      const dfs = (index1, index2) => {
         const index = `${index1},${index2}`;
         if (
            index1 === nums1.length ||
            index2 === nums2.length
         ) {
            return 0
         } else if (memo.has(index)) {
            return memo.get(index)
         }

         let res = 0;
         if (nums1[index1] === nums2[index2]) {
            res = 1 + dfs(index1 + 1, index2 + 1);
         } else {
            res = dfs(index1 + 1, index2);
            res = Math.max(res, dfs(index1, index2 + 1));
         }

         memo.set(index, res);
         return res
      }
      return dfs(0, 0);
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} nums1
    * @param {number[]} nums2
    * @return {number}
    */
   maxUncrossedLines(nums1, nums2) {
      // {(index1, index2): connection count}
      const memo = Array.from({ length: nums1.length }, () => Array(nums2.length).fill(-1));

      const dfs = (index1, index2) => {
         if (
            index1 === nums1.length ||
            index2 === nums2.length
         ) {
            return 0
         } else if (memo[index1][index2] !== -1) {
            return memo[index1][index2]
         }

         let res = 0;
         if (nums1[index1] === nums2[index2]) {
            res = 1 + dfs(index1 + 1, index2 + 1);
         } else {
            res = dfs(index1 + 1, index2);
            res = Math.max(res, dfs(index1, index2 + 1));
         }

         memo[index1][index2] = res;
         return res
      }
      return dfs(0, 0);
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} nums1
    * @param {number[]} nums2
    * @return {number}
    */
   maxUncrossedLines(nums1, nums2) {
      const cache = Array.from({ length: nums1.length + 1 }, () => Array(nums2.length + 1).fill(0));

      for (let index1 = nums1.length - 1; index1 > -1; index1--) {
         for (let index2 = nums2.length - 1; index2 > -1; index2--) {
            if (nums1[index1] === nums2[index2]) {
               cache[index1][index2] = 1 + cache[index1 + 1][index2 + 1];
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

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} nums1
    * @param {number[]} nums2
    * @return {number}
    */
   maxUncrossedLines(nums1, nums2) {
      let nextCache =  Array(nums2.length + 1).fill(0);

      for (let index1 = nums1.length - 1; index1 > -1; index1--) {
         const cache =  Array(nums2.length + 1).fill(0);

         for (let index2 = nums2.length - 1; index2 > -1; index2--) {
            if (nums1[index1] === nums2[index2]) {
               cache[index2] = 1 + nextCache[index2 + 1];
            } else {
               cache[index2] = Math.max(
                  nextCache[index2],
                  cache[index2 + 1]
               );
            }
         }
         nextCache = cache;
      }
      return nextCache[0]
   };
}


const maxUncrossedLines = new Solution().maxUncrossedLines;
console.log(new Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4]) === 2)
console.log(new Solution().maxUncrossedLines([1, 5, 6], [5, 6]) === 2)
console.log(new Solution().maxUncrossedLines([5, 6], [1, 5, 6]) === 2)
console.log(new Solution().maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) === 3)
console.log(new Solution().maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) === 2)
console.log(new Solution().maxUncrossedLines([4, 1, 2, 5, 1, 5, 3, 4, 1, 5], [3, 1, 1, 3, 2, 5, 2, 4, 1, 3, 2, 2, 5, 5, 3, 5, 5, 1, 2, 1]) === 7)
console.log(new Solution().maxUncrossedLines([1, 2, 4, 1, 4, 4, 3, 5, 5, 1, 4, 4, 4, 1, 4, 3, 4, 2, 4, 2], [2, 4, 1, 1, 3, 5, 2, 1, 5, 1, 2, 3, 3, 2, 1, 4, 1, 2, 5, 5]) === 11)
console.log(new Solution().maxUncrossedLines([5, 1, 2, 5, 1, 2, 2, 3, 1, 1, 1, 1, 1, 3, 1], [2, 5, 1, 3, 4, 5, 5, 2, 2, 4, 5, 2, 2, 3, 1, 4, 5, 3, 2, 4, 5, 2, 4, 4, 2, 2, 2, 1, 3, 1]) === 11)
