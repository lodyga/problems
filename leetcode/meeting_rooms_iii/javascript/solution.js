class Solution {
   /**
    * Time complexity: O(mlogn)
    *     n: room count, m: meegins count
    * Auxiliary space complexity: O(m)
    * Tags: heap
    * @param {number} room_count
    * @param {number[][]} meetings
    * @return {number}
    */
   mostBooked(room_count, meetings) {
      
   };
}
console.log = new Solution().mostBooked;


print(Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]), 0)
print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]), 1)
print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]), 1)
print(Solution().mostBooked(3, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]]), 1)
print(Solution().mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]), 0)
print(Solution().mostBooked(2, [[10, 11], [2, 10], [1, 17], [9, 13], [18, 20]]), 1)