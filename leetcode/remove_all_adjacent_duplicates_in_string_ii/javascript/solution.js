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
      // [[letter, frequency], ]
      const stack = [];

      for (const letter of text) {
         if (
            stack.length &&
            stack[stack.length - 1][0] === letter
         ) {
            const [_, freq] = stack.pop();

            if (freq + 1 !== k) {
               stack.push([letter, freq + 1]);
            }
         } else {
            stack.push([letter, 1]);
         }
      }

      return stack
         .map(([letter, freq]) => letter.repeat(freq))
         .join('');
   }
}


const removeDuplicates = new Solution().removeDuplicates;
console.log(new Solution().removeDuplicates('abcd', 2) === 'abcd')
console.log(new Solution().removeDuplicates('deeedbbcccbdaa', 3) === 'aa')
console.log(new Solution().removeDuplicates('pbbcggttciiippooaais', 2) === 'ps')
