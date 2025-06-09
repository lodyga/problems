class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * @param {string} text
    * @param {number} k
    * @return {string}
    */
   removeDuplicates(text, k) {
      const stack = [];  // [[letter, frequency], ]

      for (const letter of text) {
         if (
            stack.length &&
            stack[stack.length - 1][0] === letter
         ) {
            stack[stack.length - 1][1]++;
            if (stack[stack.length - 1][1] === k)
               stack.pop();
         } else {
            stack.push([letter, 1]);
         }
      }
      return stack
         .map(([letter, frequency]) => letter.repeat(frequency))
         .join('')
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: stack
    * @param {string} text
    * @param {number} k
    * @return {string}
    */
   removeDuplicates(text, k) {
      const stack = [];  // [[letter, frequency], ]

      for (const letter of text) {
         if (
            stack.length &&
            stack[stack.length - 1][0] === letter &&
            stack[stack.length - 1][1] === k - 1
         ) {
            for (let i = k; i > 1; i--) {
               stack.pop();
            }
         } else if (
            stack.length &&
            stack[stack.length - 1][0] === letter
         ) {
            stack.push([letter, stack[stack.length - 1][1] + 1]);
         } else {
            stack.push([letter, 1]);
         }
      }
      return stack
         .map(([letter, _]) => letter)
         .join('')
   };
}
const removeDuplicates = new Solution().removeDuplicates;


console.log(new Solution().removeDuplicates('abcd', 2) === 'abcd')
console.log(new Solution().removeDuplicates('deeedbbcccbdaa', 3) === 'aa')
console.log(new Solution().removeDuplicates('pbbcggttciiippooaais', 2) === 'ps')