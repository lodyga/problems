class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number} k
    * @return {number}
    */
   smallestRepunitDivByK(k) {
      if (
         k % 2 === 0 ||
         k % 5 === 0
      )
         return -1

      let num = 0;
      for (let index = 1; index <= k; index++) {
         num = (num * 10 + 1) % k;
         if (num % k === 0)
            return index
      }

      return -1
   };
}


const smallestRepunitDivByK = new Solution().smallestRepunitDivByK;
console.log(new Solution().smallestRepunitDivByK(1) === 1)
console.log(new Solution().smallestRepunitDivByK(2) === -1)
console.log(new Solution().smallestRepunitDivByK(3) === 3)
console.log(new Solution().smallestRepunitDivByK(7) === 6)
console.log(new Solution().smallestRepunitDivByK(149) === 148)
