class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    * @param {number} number
    * @return {}
    */
   maximum69Number(number) {
      const digitArray = Array.from(number.toString());
      
      for (let index = 0; index < digitArray.length; index++) {
         if (digitArray[index] === '6') {
            digitArray[index] = '9';
            return Number(digitArray.join(''))
         }
      }
      return number
   };
}
const maximum69Number = new Solution().maximum69Number;


console.log(new Solution().maximum69Number(9669) === 9969)
console.log(new Solution().maximum69Number(9996) === 9999)
console.log(new Solution().maximum69Number(9999) === 9999)