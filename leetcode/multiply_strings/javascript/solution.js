class Solution {
   /**
    * Time complexity: O(n2)
    *     n: number length
    * Auxiliary space complexity: O(n)
    * Tags: iteration
    * @param {string} number1
    * @param {string} number2
    * @return {string}
    */
   multiply(number1, number2) {
      if (number1 === '0' || number2 === '0')
         return '0'
      
      const number_list = Array(number1.length + number2.length).fill(0);

      for (let index1 = number1.length - 1; index1 > -1; index1--) {
         const digit1 = number1[index1];
         for (let index2 = number2.length - 1; index2 > -1; index2--) {
            const digit2 = number2[index2];
            number_list[(number1.length - index1 - 1) + (number2.length - index2 - 1)] += Number(digit1) * Number(digit2);
         }
      }
      
      let carry = 0;
      for (let index = 0; index < number_list.length; index++) {
         let number = number_list[index] + carry;
         carry = number / 10 | 0;
         number %= 10;
         number_list[index] = number;
      }

      while (number_list[number_list.length - 1] === 0)
         number_list.pop();
      
      return number_list.reverse().join('')
   };
}


const multiply = new Solution().multiply;
console.log(new Solution().multiply('2', '3') === '6')
console.log(new Solution().multiply('12', '34') === '408')
console.log(new Solution().multiply('123', '456') === '56088')
console.log(new Solution().multiply('0', '3') === '0')