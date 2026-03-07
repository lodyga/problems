class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: iteration
    * @param {number[]} nums1
    * @param {number[]} nums2
    * @return {number[][]}
    */
   findDifference(nums1, nums2) {
      const num1Set = new Set(nums1);
      const num2Set = new Set(nums2);

      const distinctA = [...num1Set].filter(val => !num2Set.has(val));
      const distinctB = [...num2Set].filter(val => !num1Set.has(val));

      return [distinctA, distinctB]
   };
}


const findDifference = new Solution().findDifference;
console.log(new Solution().findDifference([1, 2, 3], [2, 4, 6]).toString() === [[1, 3], [4, 6]].toString())
console.log(new Solution().findDifference([1, 2, 3, 3], [1, 1, 2, 2]).toString() === [[3], []].toString())
