class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} number
    * @return {string}
    */
   largestGoodInteger(number) {
      let triplet = '';

      for (let index = 0; index < number.length - 2; index++) {
         if (
            number[index] === number[index + 1] &&
            number[index + 1] === number[index + 2]
         ) {
            triplet = Math.max(triplet, number.slice(index, index + 3));
            index += 2;
         }
      }
      return triplet === 0 ? '000' : triplet.toString()
   };
}
const largestGoodInteger = new Solution().largestGoodInteger;


console.log(new Solution().largestGoodInteger('6777133339'), '777')
console.log(new Solution().largestGoodInteger('2300019'), '000')
console.log(new Solution().largestGoodInteger('42352338'), '')
console.log(new Solution().largestGoodInteger('7678222622241118390785777474281834906756431393782326744172075725179542796491876218340'), '777')
console.log(new Solution().largestGoodInteger('333666'), '666')