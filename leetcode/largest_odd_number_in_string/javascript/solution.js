class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {string} num
    * @return {string}
    */
   largestOddNumber(num) {
      for (let index = num.length - 1; index > -1; index--) {
         let digit = num[index];
         if ('13579'.includes(digit))
            return num.slice(0, index + 1)
      }
      return ''
   };
}


const largestOddNumber = new Solution().largestOddNumber;
console.log(new Solution().largestOddNumber('52') === '5')
console.log(new Solution().largestOddNumber('4206') === '')
console.log(new Solution().largestOddNumber('35427') === '35427')
