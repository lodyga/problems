class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set, list
    *     A: build-in function
    * @param {number[]} nums1
    * @param {number[]} nums2
    * @return {number[]}
    */
   intersection(nums1, nums2) {
      const s1 = new Set(nums1);
      const s2 = new Set(nums2);
      return [...s1].filter(num => s2.has(num))
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set, list
    * @param {number[]} nums1
    * @param {number[]} nums2
    * @return {number[]}
    */
   intersection(nums1, nums2) {
      const num1Set = new Set(nums1);
      const res = [];

      for (const num of nums2) {
         if (num1Set.has(num)) {
            res.push(num);
            num1Set.delete(num);
         }
      }
      return res
   };
}


const intersection = new Solution().intersection;
console.log(new Solution().intersection([1, 2, 2, 1], [2, 2]).sort().toString() === [2].sort().toString())
console.log(new Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]).sort().toString() === [4, 9].sort().toString())
