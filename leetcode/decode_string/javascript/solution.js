class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: stack, string
    *     A: iteration
    * @param {string} text
    * @return {string}
    */
   decodeString(text) {
      const stack = [];
      let word = "";
      let multiplier = 0;

      for (const char of text) {
         if (char >= 0 && char <= 9) {
            multiplier = multiplier * 10 + Number(char);
         } else if (char === '[') {
            stack.push(word);
            word = '';
            stack.push(multiplier);
            multiplier = 0;
         } else if (char === ']') {
            word = word.repeat(stack.pop());
            word = stack.pop() + word;
         } else {
            word += char;
         }
      }
      return word
   };
}


const decodeString = new Solution().decodeString;
console.log(new Solution().decodeString('3[a]2[bc]') === 'aaabcbc')
console.log(new Solution().decodeString('3[a2[c]]') === 'accaccacc')
console.log(new Solution().decodeString('2[abc]3[cd]ef') === 'abcabccdcdcdef')
console.log(new Solution().decodeString('10[leetcode]') === 'leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode')
console.log(new Solution().decodeString('3[z]2[2[y]pq4[2[jk]e1[f]]]ef') === 'zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef')
