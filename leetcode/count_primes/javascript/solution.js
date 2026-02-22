class Solution {
   /**
    * Time complexity: O(n*sqrt(n))
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number} n
    * @return {number}
    */
   countPrimes(n) {
      const isPrime = (num) => {
         for (let divider = 2; divider < Math.floor(num ** 0.5) + 1; divider++) {
            if (num % divider === 0) {
               return false
            }
         }
         return true
      }

      if (n < 3) {
         return 0
      }

      let counter = 1

      for (let num = 3; num < n; num += 2) {
         counter += isPrime(num) ? 1 : 0;
      }

      return counter
   };

   /**
    * Time complexity: O(n*log(log n))
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     A: sieve of eratosthenes, primes
    * @param {number} n
    * @return {number}
    */
   countPrimes(n) {
      if (n < 3) {
         return 0
      } else if (n == 3) {
         return 1
      }

      const isPrime = Array(n + 1).fill(true);
      isPrime[0] = false;
      isPrime[1] = false;

      for (let num = 2; num < Math.floor(n ** 0.5) + 1; num++) {
         if (isPrime[num]) {
            for (let multi = num * 2; multi < n + 1; multi += num) {
               isPrime[multi] = false;
            }
         }
      }

      isPrime.pop()
      return isPrime.reduce((sum, num) => sum + num, 0)
   };
}


const countPrimes = new Solution().countPrimes;
console.log(new Solution().countPrimes(10) === 4)
console.log(new Solution().countPrimes(20) === 8)
console.log(new Solution().countPrimes(0) === 0)
console.log(new Solution().countPrimes(1) === 0)
console.log(new Solution().countPrimes(2) === 0)
console.log(new Solution().countPrimes(3) === 1)
console.log(new Solution().countPrimes(19) === 7)
console.log(new Solution().countPrimes(499979) === 41537)
