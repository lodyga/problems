class Solution {
   /**
    * Time complexity: O(log(min(n+m)))
    * Auxiliary space complexity: O(1)
    * Tags:
    *    A: binary search
    * @param {number[]} nums1
    * @param {number[]} nums2
    * @return {number}
    */
   findMedianSortedArrays(nums1, nums2) {
      const [a, b] = nums1.length <= nums2.length ? [nums1, nums2] : [nums2, nums1]
      const len = a.length + b.length;
      const half = len >> 1;
      let left = 0;
      let right = a.length - 1;

      while (true) {
         let midA = (left + right) >> 1;
         let midB = half - midA - 2;

         const aLeft = midA >= 0 ? a[midA] : -(10**6) - 1;
         const aRight = midA + 1 < a.length ? a[midA + 1] : 10**6 + 1;
         const bLeft = midB >= 0 ? b[midB] : -(10**6) - 1;
         const bRight = midB + 1 < b.length ? b[midB + 1] : 10**6 + 1;

         if (
            aLeft <= bRight &&
            bLeft <= aRight
         ) {
            if (len % 2) {
               return Math.min(aRight, bRight)
            } else {
               return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2
            }
         } else if (aLeft > bRight) {
            right = midA - 1;
         } else {
            left = midA + 1
         }
      }
   };
}


const findMedianSortedArrays = new Solution().findMedianSortedArrays;
console.log(new Solution().findMedianSortedArrays([1, 3], [2]) === 2)
console.log(new Solution().findMedianSortedArrays([1, 2], [3, 4]) === 2.5)
console.log(new Solution().findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5]) === 4)
console.log(new Solution().findMedianSortedArrays([], [5]) === 5)
console.log(new Solution().findMedianSortedArrays([5], []) === 5)
