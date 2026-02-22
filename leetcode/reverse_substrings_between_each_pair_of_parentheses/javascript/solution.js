class Solution {
   /**
    * Time complexity: O(n2)
    *     O(n*m)
    *     n: text length
    *     m: parenthesis pairs count
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: stack
    * @param {string} text
    * @return {string}
    */
   reverseParentheses(text) {
      const stack = [];
      let res = '';

      for (const char of text) {
         if (char === '(') {
            stack.push(res);
            res = '';
         } else if (char === ')') {
            res = stack.pop() + res.split('').reverse('').join('');
         } else {
            res += char;
         }
      }

      return res
   };
}


const reverseParentheses = new Solution().reverseParentheses;
console.log(new Solution().reverseParentheses('yfgnxf') === 'yfgnxf')
console.log(new Solution().reverseParentheses('x(ab)z') === 'xbaz')
console.log(new Solution().reverseParentheses('(abcd)') === 'dcba')
console.log(new Solution().reverseParentheses('(u(love)i)') === 'iloveu')
console.log(new Solution().reverseParentheses('(ed(et(oc))el)') === 'leetcode')
console.log(new Solution().reverseParentheses('a(bcdefghijkl(mno)p)q') === 'apmnolkjihgfedcbq')
console.log(new Solution().reverseParentheses('ta()usw((((a))))') === 'tauswa')
console.log(new Solution().reverseParentheses('s()uteawj((eg))') === 'suteawjeg')
console.log(new Solution().reverseParentheses('sxmdll(q)eki(x)') === 'sxmdllqekix')
