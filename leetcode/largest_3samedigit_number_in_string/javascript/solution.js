class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: strging
    *     A: iteration
    * @param {string} num
    * @return {string}
    */
   largestGoodInteger(num) {
      let res = '';

      for (let idx = 0; idx < num.length - 2; idx++) {
         if ((
            num[idx] === num[idx + 1]
            && num[idx + 1] === num[idx + 2]
         ) && (
               res === ''
               || num[idx] > res[0]
            )
         ) {
            res = num[idx].repeat(3);
         }
      }

      return res;
   }
}


const largestGoodInteger = new Solution().largestGoodInteger;
console.log(new Solution().largestGoodInteger('6777133339') === '777')
console.log(new Solution().largestGoodInteger('2300019') === '000')
console.log(new Solution().largestGoodInteger('42352338') === '')
console.log(new Solution().largestGoodInteger('333666') === '666')
console.log(new Solution().largestGoodInteger('7678222622241118390785777474281834906756431393782326744172075725179542796491876218340') === '777')
