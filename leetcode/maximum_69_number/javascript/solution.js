class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: string
    *     A: iteration
    * @param {num} num
    * @return {}
    */
   maximum69Number(num) {
      const strNum = Array.from(num.toString());

      for (let idx = 0; idx < strNum.length; idx++) {
         if (strNum[idx] === '6') {
            strNum[idx] = '9';
            break;
         }
      }

      return Number(strNum.join(''));
   }
}


const maximum69Number = new Solution().maximum69Number;
console.log(new Solution().maximum69Number(9669) === 9969)
console.log(new Solution().maximum69Number(9996) === 9999)
console.log(new Solution().maximum69Number(9999) === 9999)
