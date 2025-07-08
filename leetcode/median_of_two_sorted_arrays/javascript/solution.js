class Solution {
   /**
    * Time complexity: O(log(min(n+m)))
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} numbers1
    * @param {number[]} numbers2
    * @return {number}
    */
   findMedianSortedArrays(numbers1, numbers2) {
      const [a, b] = numbers1.length <= numbers2.length ? [numbers1, numbers2] : [numbers2, numbers1]
      const len = a.length + b.length;
      const half = len >> 1;
      let left = 0;
      let right = a.length - 1;

      while (true) {
         let middleA = (left + right) >> 1;
         let middleB = half - middleA - 2;

         const aLeft = middleA >= 0 ? a[middleA] : -Infinity;
         const aRight = middleA + 1 < a.length ? a[middleA + 1] : Infinity;
         const bLeft = middleB >= 0 ? b[middleB] : -Infinity;
         const bRight = middleB + 1 < b.length ? b[middleB + 1] : Infinity;

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
            right = middleA - 1;
         } else {
            left = middleA + 1
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