class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers, three pointers, one pass
    * @param {number[]} numbers
    * @return {number[]}
    */
   sortColors(numbers) {
      let left = 0;
      let right = numbers.length - 1;
      let index = 0;

      while (index <= right) {
         if (numbers[index] === 0) {
            [numbers[index], numbers[left]] = [numbers[left], numbers[index]];
            left++;
         }
         else if (numbers[index] === 2) {
            [numbers[index], numbers[right]] = [numbers[right], numbers[index]];
            right--;
            index--;
         }
         index++;
      }
      return numbers
   };
}


console.log(new Solution().sortColors([2, 0, 1]), [0, 1, 2])
console.log(new Solution().sortColors([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])