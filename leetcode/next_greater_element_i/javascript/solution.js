class Solution {
   /**
    * Time complexity: O(n)
    *     m: numbers_1 length
    *     n: numbers_2 length (n >= m)
    * Auxiliary space complexity: O(n)
    * Tags: stack, monotonic stack, monotonic decreasing stack
    * @param {number[]} numbers1
    * @param {number[]} numbers2
    * @return {number[]}
    */
   nextGreaterElement(numbers1, numbers2) {
      const nextGreater = Array(numbers2.length).fill(-1);
      const stack = [];
      
      for (let index = 0; index < numbers2.length; index++) {
         const number = numbers2[index];
         
         while (
            stack.length && 
            number > stack[stack.length - 1][1]
         ) {
            const [prev_index, _] = stack.pop()
            nextGreater[prev_index] = number;
         } 
         stack.push([index, number])
      }
      
      const nextGreaterMap = Array(numbers1.length)
      const numbers2Map = new Map(numbers2.map((value, index) => [value, index]))
      
      for (let index = 0; index < numbers1.length; index++) {
         const number = numbers1[index];
         nextGreaterMap[index] = nextGreater[numbers2Map.get(number)]
      }
      
      return nextGreaterMap
   };
}
const nextGreaterElement = new Solution().nextGreaterElement;


console.log(new Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
console.log(new Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]), [3, -1])
console.log(new Solution().nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]), [7, 7, 7, 7, 7])