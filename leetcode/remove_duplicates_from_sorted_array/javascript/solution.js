class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {number[]}
    * @return {number}
    */
   removeDuplicates(numbers) {
      let left = 0;

      for (let right = 0; right < numbers.length; right++) {
         if (numbers[left] === numbers[right]) {
            continue
         } else {
            left++;
            numbers[left] = numbers[right];
         }
      }
      return left + 1
   };
}
const removeDuplicates = new Solution().removeDuplicates;


console.log(new Solution().removeDuplicates([1, 1, 2]), 2)
console.log(new Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)