class Solution {
   /**
    * Time complexity: O(n*sqrt(m))
    *     n: number count
    *     m: max number
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number} nums
    * @return {boolean}
    */
   primeSubOperation(nums) {
      const getPrime = (num) => {
         num = Math.max(2, num);

         while (true) {
            let isPrime = true;

            for (let divider = 2; divider < Math.floor(num ** 0.5) + 1; divider++) {
               if (num % divider === 0) {
                  isPrime = false;
                  break
               }
            }

            if (isPrime) {
               return num
            }

            num++;
         }
      }

      for (let index = nums.length - 2; index > -1; index--) {
         const num = nums[index];

         if (num < nums[index + 1]) {
            continue
         }

         const minDiff = num - nums[index + 1] + 1;
         const minPrime = getPrime(minDiff);

         if (minPrime >= num) {
            return false
         } else {
            nums[index] -= minPrime;
         }
      }

      return true
   };
}


const primeSubOperation = new Solution().primeSubOperation;
console.log(new Solution().primeSubOperation([6, 8, 11, 12]) === true)
console.log(new Solution().primeSubOperation([4, 9, 6, 10]) === true)
console.log(new Solution().primeSubOperation([5, 8, 3]) === false)
console.log(new Solution().primeSubOperation([2, 2]) === false)
console.log(new Solution().primeSubOperation([8, 19, 3, 4, 9]) === true)
console.log(new Solution().primeSubOperation([18, 12, 14, 6]) === false)
console.log(new Solution().primeSubOperation([4, 18, 10, 16, 3]) === false)
console.log(new Solution().primeSubOperation([16, 8, 4]) === false)
console.log(new Solution().primeSubOperation([6, 16, 2]) === false)
