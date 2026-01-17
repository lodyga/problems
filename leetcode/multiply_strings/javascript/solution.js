class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: string
    *     A: iteration
    * @param {string} text1
    * @param {string} text2
    * @return {string}
    */
   multiply(text1, text2) {
      if (text1 === '0' || text2 === '0')
         return '0'
      
      const num_list = Array(text1.length + text2.length).fill(0);

      for (let index1 = text1.length - 1; index1 > -1; index1--) {
         const digit1 = text1[index1];
         for (let index2 = text2.length - 1; index2 > -1; index2--) {
            const digit2 = text2[index2];
            num_list[(text1.length - index1 - 1) + (text2.length - index2 - 1)] += Number(digit1) * Number(digit2);
         }
      }
      
      let carry = 0;
      for (let index = 0; index < num_list.length; index++) {
         let num = num_list[index] + carry;
         carry = Math.floor(num / 10);
         num %= 10;
         num_list[index] = num;
      }

      while (num_list[num_list.length - 1] === 0)
         num_list.pop();
      
      return num_list.reverse().join('')
   };
}


const multiply = new Solution().multiply;
console.log(new Solution().multiply('2', '3') === '6')
console.log(new Solution().multiply('12', '34') === '408')
console.log(new Solution().multiply('123', '456') === '56088')
console.log(new Solution().multiply('0', '3') === '0')
