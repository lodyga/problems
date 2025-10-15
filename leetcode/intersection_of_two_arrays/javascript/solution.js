class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {number[]} numbers1
    * @param {number[]} numbers2
    * @return {number[]}
    */
   intersection(numbers1, numbers2) {
      const s1 = new Set(numbers1);
      const s2 = new Set(numbers2);
      return [...s1].filter(value => s2.has(value))
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {number[]} numbers1
    * @param {number[]} numbers2
    * @return {number[]}
    */
   intersection(numbers1, numbers2) {
      const numbers1Set = new Set(numbers1)
      const intersect = [];
      for (const number of numbers2) {
         if (numbers1Set.has(number)) {
            intersect.push(number)
            numbers1Set.delete(number);
         }
      }
      return intersect
   };
}


const intersection = new Solution().intersection;
console.log(new Solution().intersection([1, 2, 2, 1], [2, 2]), [2])
console.log(new Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])