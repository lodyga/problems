class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @return {boolean}
    */
   validPartition(numbers) {
      const cache = [true, true, true, true];

      for (let index = numbers.length - 1; index >= 0; index--) {
         cache.pop();
         cache.unshift(false);

         if (!cache[0] && index + 1 < numbers.length) {
            if (numbers[index] === numbers[index + 1]) {
               cache[0] = cache[2];
            }
         }

         if (!cache[0] && index + 2 < numbers.length) {
            if (
               numbers[index] === numbers[index + 1] &&
               numbers[index + 1] === numbers[index + 2]
            ) {
               cache[0] = cache[3];
            }
         }

         if (!cache[0] && index + 2 < numbers.length) {
            if (
               numbers[index] + 2 === numbers[index + 1] + 1 &&
               numbers[index + 1] + 1 === numbers[index + 2]
            ) {
               cache[0] = cache[3];
            }
         }
      }
      return cache[0]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @return {boolean}
    */
   validPartition(numbers) {
      const cache = Array(numbers.length + 1).fill(false);
      cache[cache.length - 1] = true;

      for (let index = numbers.length - 1; index >= 0; index--) {

         if (!cache[index] && index + 1 < numbers.length) {
            if (numbers[index] === numbers[index + 1]) {
               cache[index] = cache[index + 2];
            }
         }

         if (!cache[index] && index + 2 < numbers.length) {
            if (
               numbers[index] === numbers[index + 1] &&
               numbers[index + 1] === numbers[index + 2]
            ) {
               cache[index] = cache[index + 3];
            }
         }

         if (!cache[index] && index + 2 < numbers.length) {
            if (
               numbers[index] + 2 === numbers[index + 1] + 1 &&
               numbers[index + 1] + 1 === numbers[index + 2]
            ) {
               cache[index] = cache[index + 3];
            }
         }
      }
      return cache[0]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down witm memoization as hash map
    * @param {number[]} numbers
    * @return {boolean}
    */
   validPartition(numbers) {
      const memo = new Map([[numbers.length, true]]);
      return dfs(0)

      function dfs(index) {
         if (memo.has(index)) {
            return memo.get(index)
         }

         memo.set(index, false);

         if (!memo.get(index) && index + 1 < numbers.length) {
            if (numbers[index] === numbers[index + 1]) {
               memo.set(index, dfs(index + 2));
            }
         }

         if (!memo.get(index) && index + 2 < numbers.length) {
            if (
               numbers[index] === numbers[index + 1] && 
               numbers[index + 1] === numbers[index + 2]
            ) {
               memo.set(index, dfs(index + 3));
            }
         }

         if (!memo.get(index) && index + 2 < numbers.length) {
            if (
               numbers[index] + 2 === numbers[index + 1] + 1 && 
               numbers[index + 1] + 1 === numbers[index + 2]
            ) {
               memo.set(index, dfs(index + 3));
            }
         }
         return memo.get(index)
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down witm memoization as array
    * @param {number[]} numbers
    * @return {boolean}
    */
   validPartition(numbers) {
      const memo = Array(numbers.length + 1).fill(null);
      memo[memo.length - 1] = true;
      return dfs(0)

      function dfs(index) {
         if (memo[index]) {
            return memo[index]
         } else if (memo[index] === false) {
            return false
         }

         if (!memo[index] && index + 1 < numbers.length) {
            if (numbers[index] === numbers[index + 1]) {
               memo[index] = dfs(index + 2);
            }
         }

         if (!memo[index] && index + 2 < numbers.length) {
            if (
               numbers[index] === numbers[index + 1] && 
               numbers[index + 1] === numbers[index + 2]
            ) {
               memo[index] = dfs(index + 3);
            }
         }

         if (!memo[index] && index + 2 < numbers.length) {
            if (
               numbers[index] + 2 === numbers[index + 1] + 1 && 
               numbers[index + 1] + 1 === numbers[index + 2]
            ) {
               memo[index] = dfs(index + 3);
            }
         }
         return memo[index] ? memo[index] : false
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: brute-force, tle
    * @param {number[]} numbers
    * @return {boolean}
    */
   validPartition(numbers) {
      return dfs(0)

      function dfs(index) {
         if (index >= numbers.length) {
            return index === numbers.length
         }
         let memo = false;

         if (!memo && index + 1 < numbers.length) {
            if (numbers[index] === numbers[index + 1]) {
               memo = dfs(index + 2);
            }
         }

         if (!memo && index + 2 < numbers.length) {
            if (
               numbers[index] === numbers[index + 1] && 
               numbers[index + 1] === numbers[index + 2]
            ) {
               memo = dfs(index + 3);
            }
         }

         if (!memo && index + 2 < numbers.length) {
            if (
               numbers[index] + 2 === numbers[index + 1] + 1 && 
               numbers[index + 1] + 1 === numbers[index + 2]
            ) {
               memo = dfs(index + 3);
            }
         }
         return memo
      }
   };
}
const validPartition = new Solution().validPartition;


console.log(new Solution().validPartition([4, 4, 4, 5, 6]) === true)
console.log(new Solution().validPartition([1, 1, 1, 2]) === false)
console.log(new Solution().validPartition([993335, 993336, 993337, 993338, 993339, 993340, 993341]) === false)
console.log(new Solution().validPartition([803201, 803201, 803201, 803201, 803202, 803203]) === true)
console.log(new Solution().validPartition([67149, 67149, 67149, 67149, 67149, 136768, 136768, 136768, 136768, 136768, 136768, 136768, 136769, 136770, 136771, 136772, 136773, 136774, 136775, 136776, 136777, 136778, 136779, 136780, 136781, 136782, 136783, 136784]) === false)