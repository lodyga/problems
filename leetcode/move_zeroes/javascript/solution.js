class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers, in-place method
    * @param {number[]} numbers
    * @return {number[]}
    */
   moveZeroes(numbers) {
      let left = 0;

      for (let right = 0; right < numbers.length; right++) {
         const number = numbers[right];
         if (number !== 0) {
            [numbers[left], numbers[right]] = [numbers[right], numbers[left]];
            left++;
         }
      }
      return numbers
   };
}


console.log(new Solution().moveZeroes([0]), [0])
console.log(new Solution().moveZeroes([1]), [1])
console.log(new Solution().moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])