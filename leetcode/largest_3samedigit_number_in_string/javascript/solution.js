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
      let triplet = '';

      for (let index = 0; index < num.length - 2; index++) {
         if (
            num[index] === num[index + 1] &&
            num[index + 1] === num[index + 2]
         ) {
            if (
               triplet === '' ||
               (triplet && num[index] > triplet[0])
            ) 
               triplet = num[index].repeat(3);
         }
      }
      return triplet
   };
}


const largestGoodInteger = new Solution().largestGoodInteger;
console.log(new Solution().largestGoodInteger('6777133339') === '777')
console.log(new Solution().largestGoodInteger('2300019') === '000')
console.log(new Solution().largestGoodInteger('42352338') === '')
console.log(new Solution().largestGoodInteger('333666') === '666')
console.log(new Solution().largestGoodInteger('7678222622241118390785777474281834906756431393782326744172075725179542796491876218340') === '777')
