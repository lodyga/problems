class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers
    * @param {number[]} numbers
    * @return {number[]}
    */
   rearrangeArray(numbers) {
      numbers.sort((a, b) => a - b);
      const rear = Array(numbers.length).fill(0);
      let middle = numbers.length >> 1;
      let left = 0;
      let right = middle;
      let index = 0

      while (right < numbers.length) {
         rear[index] = numbers[right];
         index++
         right++;

         if (left !== middle) {
            rear[index] = numbers[left];
            index++
            left++;
         }
      }
      return rear
   };
}
const rearrangeArray = new Solution().rearrangeArray;


console.log(new Solution().rearrangeArray([1, 2, 3, 4, 5]), [1, 5, 2, 4, 3])
console.log(new Solution().rearrangeArray([1, 2, 3, 4]), [1, 4, 2, 3])
console.log(new Solution().rearrangeArray([6, 2, 0, 9, 7]), [0, 9, 2, 7, 6])
console.log(new Solution().rearrangeArray([1, 3, 2]), [1, 3, 2])
console.log(new Solution().rearrangeArray([15, 7, 13, 6, 3, 11, 14, 1, 20]), [11, 1, 13, 3, 14, 6, 15, 7, 20])