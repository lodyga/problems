class MountainArray {
   constructor(nums) {
      this.nums = nums;
   };

   /**
    * @param {number} index
    * @return {number}
    */
   get(index) {
      return this.nums[index]
   };

   /**
    * @return {number}
    */
   length() {
      return this.nums.length
   };
}


class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    A: binary search
    * @param {number} target
    * @param {MountainArray} mountainArr
    * @return {number}
    */
   findInMountainArray(target, mountainArr) {
      const len = mountainArr.length();
      let left = 1;
      let right = len - 2;
      let peak;

      // find the peak
      while (left <= right) {
         const midd = (left + right) >> 1;
         const midHeight = mountainArr.get(midd);
         const leftHeight = mountainArr.get(midd - 1);
         const rightHeight = mountainArr.get(midd + 1);

         if (
            leftHeight < midHeight &&
            midHeight > rightHeight
         ) {
            peak = midd;
            break
         } else if (
            midHeight < rightHeight
         ) {
            left = midd + 1;
            peak = left;
         } else {
            right = midd - 1;
            peak = right;
         }
      }

      // search the left portion
      left = 0;
      right = peak;
      while (left <= right) {
         const midd = (left + right) >> 1;
         const midHeight = mountainArr.get(midd);

         if (target === midHeight) {
            return midd
         } else if (target < midHeight) {
            right = midd - 1;
         } else {
            left = midd + 1;
         }
      }

      // search the right portion
      left = peak + 1;
      right = len - 1;
      while (left <= right) {
         const midd = (left + right) >> 1;
         const midHeight = mountainArr.get(midd);

         if (target === midHeight) {
            return midd
         } else if (target > midHeight) {
            right = midd - 1;
         } else {
            left = midd + 1;
         }
      }

      return -1
   }
}


const findInMountainArray = new Solution().findInMountainArray;
console.log(new Solution().findInMountainArray(3, new MountainArray([1, 2, 3, 4, 5, 3, 1])) === 2)
console.log(new Solution().findInMountainArray(3, new MountainArray([0, 1, 2, 4, 2, 1])) === -1)
