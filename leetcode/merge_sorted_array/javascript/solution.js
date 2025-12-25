class Solution {
   /**
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
      let index1 = m - 1;
      let index2 = n - 1;
      let index = m + n - 1;

      while (
         index1 > -1 ||
         index2 > -1
      ) {
         const num1 = index1 > - 1 ? nums1[index1] : nums2[0] - 1;
         const num2 = index2 > - 1 ? nums2[index2] : nums1[0] - 1;

         if (num1 > num2) {
            nums1[index] = num1;
            index1--;
         } else {
            nums1[index] = num2;
            index2 -= 1;
         }
         index -= 1;
      };
      return nums1
   };
}


const merge = new Solution().merge;
console.log(JSON.stringify(new Solution().merge([1], 1, [], 0)) === JSON.stringify([1]))
console.log(JSON.stringify(new Solution().merge([0], 0, [1], 1)) === JSON.stringify([1]))
console.log(JSON.stringify(new Solution().merge([2, 0], 1, [1], 1)) === JSON.stringify([1, 2]))
console.log(JSON.stringify(new Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)) === JSON.stringify([1, 2, 2, 3, 5, 6]))
console.log(JSON.stringify(new Solution().merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)) === JSON.stringify([-1, 0, 0, 1, 2, 2, 3, 3, 3]))
console.log(JSON.stringify(new Solution().merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)) === JSON.stringify([1, 2, 3, 4, 5, 6]))
