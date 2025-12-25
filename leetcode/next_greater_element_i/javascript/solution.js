class Solution {
   /**
    * Time complexity: O(n+m)
    * Auxiliary space complexity: O(n+m)
    * Tags: 
    *     DS: monotonic decreasing stack, hash map
    *     A: iteration
    * @param {number[]} nums1
    * @param {number[]} nums2
    * @return {number[]}
    */
   nextGreaterElement(nums1, nums2) {
      // {num: next greater num, ...}
      const num2Next = new Map(nums2.map(num => [num, -1]));

      // Find the next greater number.
      const stack = [];  // decreasing stack
      for (const num of nums2) {
         while (stack.length && stack[stack.length - 1] < num)
            num2Next.set(stack.pop(), num);
         stack.push(num);
      }
      return nums1.map(num => num2Next.get(num))
   };
}


const nextGreaterElement = new Solution().nextGreaterElement;
console.log(JSON.stringify(new Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])) === JSON.stringify([-1, 3, -1]))
console.log(JSON.stringify(new Solution().nextGreaterElement([2, 4], [1, 2, 3, 4])) === JSON.stringify([3, -1]))
console.log(JSON.stringify(new Solution().nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7])) === JSON.stringify([7, 7, 7, 7, 7]))
