class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *    DS: stack
    *    A: iteration
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
            const [_, frequency] = stack.pop();
            if (frequency + 1 < k)
               stack.push([letter, frequency + 1]);
         } else {
            stack.push([letter, 1]);
         }
      }
      return stack
         .map(([letter, frequency]) => letter.repeat(frequency))
         .join('')
   };
}


const removeDuplicates = new Solution().removeDuplicates;
console.log(new Solution().removeDuplicates('abcd', 2) === 'abcd')
console.log(new Solution().removeDuplicates('deeedbbcccbdaa', 3) === 'aa')
console.log(new Solution().removeDuplicates('pbbcggttciiippooaais', 2) === 'ps')
