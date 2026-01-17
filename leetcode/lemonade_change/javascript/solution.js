class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: greedy
    * @param {number[]} bills
    * @return {boolean}
    */
   lemonadeChange(bills) {
      // bill deposit frequency: 5, 10
      const change = [0, 0];
      for (const bill of bills) {
         if (bill === 5) {
            change[0]++;
         } else if (bill === 10) {
            if (change[0] === 0)
               return false
            else {
               change[0]--;
               change[1]++;
            }
         } else {
            if (change[0] && change[1]) {
               change[0]--;
               change[1]--;
            } else if (change[0] >= 3) {
               change[0] -= 3;
            } else
               return false
         }
      }
      return true
   };
}


const lemonadeChange = new Solution().lemonadeChange;
console.log(new Solution().lemonadeChange([5, 5, 5, 10, 20]) === true)
console.log(new Solution().lemonadeChange([5, 5, 10, 10, 20]) === false)
console.log(new Solution().lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]) === true)
console.log(new Solution().lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]) === false)
