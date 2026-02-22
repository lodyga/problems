class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: sorting
    * @param {string[]} timePoints
    * @return {number}
    */
   findMinDifference(timePoints) {
      const times = timePoints.map(([h1, h2, , m1, m2]) =>
         [Number(h1) * 10 + Number(h2), Number(m1) * 10 + Number(m2)]);
      times.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
      const [h0, m0] = times[0];
      times.push([24 + h0, m0]);
      let res = 24 * 60;

      for (let index = 0; index < times.length - 1; index++) {
         const [h1, m1] = times[index];
         const [h2, m2] = times[index + 1];
         res = Math.min(res, (h2 - h1) * 60 + (m2 - m1));

         if (res === 0) {
            return 0
         }
      }
      return res
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: sorting
    * @param {string[]} timePoints
    * @return {number}
    */
   findMinDifference(timePoints) {
      const times = timePoints.map(([h1, h2, , m1, m2]) =>
         (Number(h1) * 10 + Number(h2)) * 60 + Number(m1) * 10 + Number(m2));
      times.sort((a, b) => a - b);
      times.push(times[0] + 24 * 60);
      let res = 24 * 60;

      for (let index = 0; index < times.length - 1; index++) {
         res = Math.min(res, times[index + 1] - times[index]);

         if (res === 0) {
            return 0
         }
      }
      return res
   };
}


const findMinDifference = new Solution().findMinDifference;
console.log(new Solution().findMinDifference(['23:59', '00:00']) === 1)
console.log(new Solution().findMinDifference(['00:00', '23:59', '00:00']) === 0)
console.log(new Solution().findMinDifference(['02:39', '10:26', '21:43']) === 296)
console.log(new Solution().findMinDifference(['00:01', '01:59']) === 118)
