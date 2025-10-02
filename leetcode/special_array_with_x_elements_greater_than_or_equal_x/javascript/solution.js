class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} numbers
    * @return {number}
    */
   specialArray(numbers) {
      let left = 1;
      let right = numbers.length;
      let specialNumber = -1;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const specialCount = numbers.filter(value => value >= middle).length;
         
         if (specialCount >= middle) {
            if (specialCount === middle)
               specialNumber = middle;
            left = middle + 1;
         } else
            right = middle - 1;
      }
      return specialNumber
   };
}


const specialArray = new Solution().specialArray;
console.log(new Solution().specialArray([3, 5]) === 2)
console.log(new Solution().specialArray([0, 0]) === -1)
console.log(new Solution().specialArray([0, 4, 3, 0, 4]) === 3)
console.log(new Solution().specialArray([3, 6, 7, 7, 0]) === -1)