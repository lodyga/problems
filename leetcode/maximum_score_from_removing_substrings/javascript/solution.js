class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: stack, string
    *     A: greedy, iteration
    * @param {string} text
    * @param {number} x
    * @param {number} y
    * @return {number}
    */
   maximumGain(text, x, y) {
      const [highSubstr, lowSubstr] = x >= y ? ['ab', 'ba'] : ['ba', 'ab'];
      const [highPts, lowPts] = x >= y ? [x, y] : [y, x];
      let score = 0;
      const highStack = [];

      for (const char of text) {
         if (
            highStack.length &&
            highStack[highStack.length - 1] === highSubstr[0] &&
            char === highSubstr[1]
         ) {
            highStack.pop();
            score += highPts;
         } else {
            highStack.push(char);
         }
      }

      const lowStack = [];

      for (const char of highStack) {
         if (
            lowStack.length &&
            lowStack[lowStack.length - 1] === lowSubstr[0] &&
            char === lowSubstr[1]
         ) {
            lowStack.pop();
            score += lowPts;
         } else {
            lowStack.push(char);
         }
      }

      return score
   };
}


const maximumGain = new Solution().maximumGain;
console.log(new Solution().maximumGain('aba', 4, 5) === 5)
console.log(new Solution().maximumGain('bab', 4, 5) === 5)
console.log(new Solution().maximumGain('cdbcbbaaabab', 4, 5) === 19)
console.log(new Solution().maximumGain('aabbaaxybbaabb', 5, 4) === 20)
console.log(new Solution().maximumGain('aabbrtababbabmaaaeaabeawmvaataabnaabbaaaybbbaabbabbbjpjaabbtabbxaaavsmmnblbbabaeuasvababjbbabbabbasxbbtgbrbbajeabbbfbarbagha', 8484, 4096) === 198644)
console.log(new Solution().maximumGain('babeaaabbafaaabbnaabuaaaaagabbaabbbbbmaaanaasaebbvlaaabbbaibabbbabaaabasbbryqraryobuabguabaabbmabgubabbaaraaaabapbaabsbbbbbbbbahabbbsanaajbabarbntbqagkbababbabbbbaabaybagababaabbzaaaaaaambwabbbaababmxqbbgbabbbabbbbbaakabaabzabbabfabjbobabaaaabbbaaaaaaaajbbbaqrabnarsaabbbaabaabavgbaaabtmcbbababbbubaaababaedbbtabbalkababiaaaabbaafabaabtvbbzayaaaakzbdafbasbaabbsbbarbebaaboyabbabnyamabbbfubaaebabaababbbbbqxajaaaamfabbabbbapbubaabbehbbnaandabmxbqcaaqbyaabbamafbaufaabblbbbbabbaabgbdbbnbaababaiauaybbtnbnaayasgafadbabblabbbaababbtsbabapbdaaasxxafakaaaaabrbbcabaahzbaaajbbbbbhaabbabbtbababbababaxabaaaipabbxbaagbaaabba', 7275, 9407) === 1220161)
