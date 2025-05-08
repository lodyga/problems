class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: hash map
    * @param {number[]} bills
    * @return {boolean}
    */
   lemonadeChange(bills) {
      const moneyCounter = new Map([
         [5, 0],
         [10, 0],
         [20, 0]
      ]);

      for (const bill of bills) {
         if (bill === 5) {
            moneyCounter.set(5, moneyCounter.get(5) + 1);
         } else if (bill === 10) {
            if (moneyCounter.get(5) === 0) {
               return false
            } else {
               moneyCounter.set(5, moneyCounter.get(5) - 1);
               moneyCounter.set(10, moneyCounter.get(10) + 1);
            }
         } else if (bill === 20) {
            if (
               moneyCounter.get(5) > 0 &&
               moneyCounter.get(10) > 0
            ) {
               moneyCounter.set(5, moneyCounter.get(5) - 1);
               moneyCounter.set(10, moneyCounter.get(10) - 1);
            } else if (moneyCounter.get(5) > 2) {
               moneyCounter.set(5, moneyCounter.get(5) - 3);
            } else {
               return false
            }
            moneyCounter.set(20, moneyCounter.get(20) + 1);
         }
      }
      return true
   };
}


console.log(new Solution().lemonadeChange([5, 5, 5, 10, 20]), true)
console.log(new Solution().lemonadeChange([5, 5, 10, 10, 20]), false)
console.log(new Solution().lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]), true)
console.log(new Solution().lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]), false)