class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: prefix sum
    * @param {string} boxes
    * @return {number}
    */
   minOperations(boxes) {
      const N = boxes.length;
      const nums = boxes.split('').map((val) => val === "1" ? 1 : 0);
      const prefix = [0];
      const suffix = [0];
      let balls = 0;

      for (let index = 1; index < N; index++) {
         balls += nums[index - 1];
         prefix.push(prefix[prefix.length - 1] + balls);
      }

      balls = 0;

      for (let index = N - 2; index > -1; index--) {
         balls += nums[index + 1];
         suffix.push(suffix[suffix.length - 1] + balls);
      }

      return suffix.reverse().map((val, index) => val + prefix[index]);
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: prefix sum
    * @param {string} boxes
    * @return {number}
    */
   minOperations(boxes) {
      const N = boxes.length;
      const prefix = [0];
      let suffix = 0;
      let balls = 0;

      for (let index = 1; index < N; index++) {
         balls += boxes[index - 1] == '1' ? 1 : 0;
         prefix.push(prefix[prefix.length - 1] + balls);
      }

      balls = 0;

      for (let index = N - 2; index > -1; index--) {
         balls += boxes[index + 1] == '1' ? 1 : 0;
         suffix += balls;
         prefix[index] += suffix;
      }

      return prefix
   };
}


const minOperations = new Solution().minOperations;
console.log(new Solution().minOperations("110").toString() === [1, 1, 3].toString())
console.log(new Solution().minOperations("001011").toString() === [11, 8, 5, 4, 3, 4].toString())
