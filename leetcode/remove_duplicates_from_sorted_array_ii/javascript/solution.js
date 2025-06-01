class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {number[]} numbers
    * @return {number}
    */
   removeDuplicates(numbers) {
      let left = 1;

      for (let right = 2; right < numbers.length; right++) {
         if (numbers[left - 1] < numbers[right]) {
            left++;
            numbers[left] = numbers[right]
         }
      }

      return left + 1
   };
}


console.log(new Solution().removeDuplicates([1, 1, 1, 2, 2, 3]) == 5)
console.log(new Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) === 7)