class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: in-place method, two pointers
    * @param {number[]} numbers
    * @return {number[]}
    */
   sortArrayByParity(numbers) {
      let left = 0;
      
      for (let right = 0; right < numbers.length; right++) {
         const number = numbers[right];

         if (number % 2 === 0) {
            [numbers[left], numbers[right]] = [numbers[right], numbers[left]];
            left++;
         }
      }
      return numbers
   };
}
const sortArrayByParity = new Solution().sortArrayByParity;


console.log(new Solution().sortArrayByParity([3, 1, 2, 4]), [2, 4, 3, 1])
console.log(new Solution().sortArrayByParity([1, 2, 3, 4]), [2, 4, 3, 1])
console.log(new Solution().sortArrayByParity([0]), [0])