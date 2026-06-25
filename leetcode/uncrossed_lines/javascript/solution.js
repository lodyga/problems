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
      const N1 = nums1.length;
      const N2 = nums2.length;
      // {(idx1, idx2): connection count}
      const memo = new Map();

      const dfs = (idx1, idx2) => {
         // const idx = `${idx1},${idx2}`;
         const idx = (BigInt(idx1) << 32n) | BigInt(idx2);
         if (idx1 === N1 || idx2 === N2) {
            return 0;
         }
         else if (memo.has(idx)) {
            return memo.get(idx);
         }

         let res = 0;

         if (nums1[idx1] === nums2[idx2]) {
            res = 1 + dfs(idx1 + 1, idx2 + 1);
         }
         else {
            res = Math.max(
               dfs(idx1 + 1, idx2),
               dfs(idx1, idx2 + 1)
            );
         }

         memo.set(idx, res);
         return res;
      }

      return dfs(0, 0);
   }
}


class Solution {
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
      const N1 = nums1.length;
      const N2 = nums2.length;
      // {(idx1, idx2): connection count}
      const memo = Array.from({ length: nums1.length }, () => Array(nums2.length).fill(-1));

      const dfs = (idx1, idx2) => {
         if (idx1 === N1 || idx2 === N2) {
            return 0;
         }
         else if (memo[idx1][idx2] !== -1) {
            return memo[idx1][idx2];
         }

         let res = 0;

         if (nums1[idx1] === nums2[idx2]) {
            res = 1 + dfs(idx1 + 1, idx2 + 1);
         } else {
            res = Math.max(
               dfs(idx1 + 1, idx2),
               dfs(idx1, idx2 + 1)
            );
         }

         memo[idx1][idx2] = res;
         return res;
      }

      return dfs(0, 0);
   };
}


class Solution {
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
      const N1 = nums1.length;
      const N2 = nums2.length;
      const cache = Array.from({ length: N1 + 1 }, () => Array(N2 + 1).fill(0));

      for (let idx1 = N1 - 1; idx1 > -1; idx1--) {
         for (let idx2 = N2 - 1; idx2 > -1; idx2--) {
            if (nums1[idx1] === nums2[idx2]) {
               cache[idx1][idx2] = 1 + cache[idx1 + 1][idx2 + 1];
            }
            else {
               cache[idx1][idx2] = Math.max(
                  cache[idx1 + 1][idx2],
                  cache[idx1][idx2 + 1]
               );
            }
         }
      }

      return cache[0][0];
   }
}


class Solution {
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
      const N1 = nums1.length;
      const N2 = nums2.length;
      let nextCache = Array(N2 + 1).fill(0);

      for (let idx1 = N1 - 1; idx1 > -1; idx1--) {
         const cache = Array(N2 + 1).fill(0);

         for (let idx2 = N2 - 1; idx2 > -1; idx2--) {
            if (nums1[idx1] === nums2[idx2]) {
               cache[idx2] = 1 + nextCache[idx2 + 1];
            } else {
               cache[idx2] = Math.max(
                  nextCache[idx2],
                  cache[idx2 + 1]
               );
            }
         }

         nextCache = cache;
      }

      return nextCache[0];
   }
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
