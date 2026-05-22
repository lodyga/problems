class Solution {
   /**
    * Do not return anything, modify nums1 in-place instead.
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: two pointers, in-place method
    * @param {number[]} nums1
    * @param {number} m
    * @param {number[]} nums2
    * @param {number} n
    * @return {number[]}
    */
   merge(nums1, m, nums2, n) {
      let idx1 = m - 1;
      let idx2 = n - 1;
      let idx = m + n - 1;

      while (idx1 > -1 || idx2 > -1) {
         const num1 = idx1 > - 1 ? nums1[idx1] : nums2[0] - 1;
         const num2 = idx2 > - 1 ? nums2[idx2] : nums1[0] - 1;

         if (num1 > num2) {
            nums1[idx] = num1;
            idx1--;
         } else {
            nums1[idx] = num2;
            idx2 -= 1;
         }

         idx--;
      }
      
      return nums1
   }
}


const merge = new Solution().merge;
console.log(JSON.stringify(new Solution().merge([1], 1, [], 0)) === JSON.stringify([1]))
console.log(JSON.stringify(new Solution().merge([0], 0, [1], 1)) === JSON.stringify([1]))
console.log(JSON.stringify(new Solution().merge([2, 0], 1, [1], 1)) === JSON.stringify([1, 2]))
console.log(JSON.stringify(new Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)) === JSON.stringify([1, 2, 2, 3, 5, 6]))
console.log(JSON.stringify(new Solution().merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)) === JSON.stringify([-1, 0, 0, 1, 2, 2, 3, 3, 3]))
console.log(JSON.stringify(new Solution().merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)) === JSON.stringify([1, 2, 3, 4, 5, 6]))
