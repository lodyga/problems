class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {number[][]} numbers1
    * @param {number[][]} numbers2
    * @return {number[][]}
    */
   mergeArrays(numbers1, numbers2) {
      let index1 = 0;
      let index2 = 0;
      const mergedArrays = [];

      while (
         index1 < numbers1.length &&
         index2 < numbers2.length
      ) {
         if (numbers1[index1][0] < numbers2[index2][0]) {
            mergedArrays.push(numbers1[index1]);
            index1++;
         } else if (numbers2[index2][0] < numbers1[index1][0]) {
            mergedArrays.push(numbers2[index2]);
            index2++;
         } else {
            mergedArrays.push([numbers1[index1][0], numbers1[index1][1] + numbers2[index2][1]]);
            index1++
            index2++;
         }
      }
      while (index1 < numbers1.length) {
         mergedArrays.push(numbers1[index1]);
         index1++;
      }
      while (index2 < numbers2.length) {
         mergedArrays.push(numbers2[index2]);
         index2++;
      }
      return mergedArrays
   };
}


const mergeArrays = new Solution().mergeArrays;
console.log(new Solution().mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]), [[1, 6], [2, 3], [3, 2], [4, 6]])
console.log(new Solution().mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]), [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]])