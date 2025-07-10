class MountainArray {
   constructor(numbers) {
      this.numbers = numbers;
   };

   /**
    * @param {number} index
    * @return {number}
    */
   get(index) {
      return this.numbers[index]
   };

   /**
    * @return {number}
e    */
   length() {
      return this.numbers.length
   };
}


class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number} target
    * @param {MountainArray} mountainArr
    * @return {number}
    */
   findInMountainArray(target, mountainArr) {
      const len = mountainArr.length();
      let left = 1;
      let right = len - 2;
      let peak;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleNumber = mountainArr.get(middle);
         const leftNumber = mountainArr.get(middle - 1);
         const rightNumber = mountainArr.get(middle + 1);

         if (
            leftNumber < middleNumber &&
            middleNumber < rightNumber
         ) {
            left = middle + 1;
         } else if (
            leftNumber > middleNumber &&
            middleNumber > rightNumber
         ) {
            right = middle - 1
         } else {
            peak = middle;
            break
         }
      }

      left = 0;
      right = peak;
      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleNumber = mountainArr.get(middle);

         if (target === middleNumber) {
            return middle
         } else if (target < middleNumber) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }

      left = peak + 1;
      right = len - 1;
      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleNumber = mountainArr.get(middle);

         if (target === middleNumber) {
            return middle
         } else if (target > middleNumber) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }

      return -1
   }
}
const findInMountainArray = new Solution().findInMountainArray;


console.log(new Solution().findInMountainArray(3, new MountainArray([1, 2, 3, 4, 5, 3, 1])) == 2)
console.log(new Solution().findInMountainArray(3, new MountainArray([0, 1, 2, 4, 2, 1])) == -1)