class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: string
    *     A: greedy
    * @param {num} num
    * @return {}
    */
   maximum69Number(num) {
      const digitNum = Array.from(num.toString());

      for (let index = 0; index < digitNum.length; index++) {
         if (digitNum[index] === '6') {
            digitNum[index] = '9';
            break
         }
      }
      return Number(digitNum.join(''))
   };
}


const maximum69Number = new Solution().maximum69Number;
console.log(new Solution().maximum69Number(9669) === 9969)
console.log(new Solution().maximum69Number(9996) === 9999)
console.log(new Solution().maximum69Number(9999) === 9999)
