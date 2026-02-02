class Solution {
   /**
    * Time complexity: O(n + m)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: list
    *     A: two pionters
    * @param {number[][]} nums1
    * @param {number[][]} nums2
    * @return {number[][]}
    */
   mergeArrays(nums1, nums2) {
      let index1 = 0;
      let index2 = 0;
      const res = [];

      while (
         index1 < nums1.length &&
         index2 < nums2.length
      ) {
         const [key1, val1] = nums1[index1];
         const [key2, val2] = nums2[index2];

         if (key1 === key2) {
            res.push([key1, val1 + val2]);
            index1++
            index2++;
         } else if (key1 < key2) {
            res.push([key1, val1]);
            index1++;
         } else {
            res.push([key2, val2]);
            index2++;
         }
      }
      while (index1 < nums1.length) {
         res.push(nums1[index1]);
         index1++;
      }
      while (index2 < nums2.length) {
         res.push(nums2[index2]);
         index2++;
      }
      return res
   };

   /**
    * Time complexity: O(n + m)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: list
    *     A: two pionters
    * @param {number[][]} nums1
    * @param {number[][]} nums2
    * @return {number[][]}
    */
   mergeArrays(nums1, nums2) {
      let index1 = 0;
      let index2 = 0;
      const res = [];

      while (
         index1 < nums1.length ||
         index2 < nums2.length
      ) {
         if (index1 === nums1.length) {
            res.push(nums2[index2]);
            index2++;
            continue
         } else if (index2 === nums2.length) {
            res.push(nums1[index1]);
            index1++;
            continue
         }

         const [key1, val1] = nums1[index1];
         const [key2, val2] = nums2[index2];

         if (key1 === key2) {
            res.push([key1, val1 + val2]);
            index1++
            index2++;
         } else if (key1 < key2) {
            res.push([key1, val1]);
            index1++;
         } else {
            res.push([key2, val2]);
            index2++;
         }
      }
      return res
   };
}


const mergeArrays = new Solution().mergeArrays;
console.log(new Solution().mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]).toString() === [[1, 6], [2, 3], [3, 2], [4, 6]].toString())
console.log(new Solution().mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]).toString() === [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]].toString())
