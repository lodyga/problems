import { MinPriorityQueue } from '@datastructures-js/priority-queue';


/**
 * Time complexity: O(n*logk)
 *     n: number of `add` calls
 *     k: the number of highest test scores
 * Auxiliary space complexity: O(1)
 * Tags: 
 *     DS: heap
 *     A: heap, in-place method
 */
class KthLargest {
    /**
     * @param {number} k
     * @param {number[]} nums
     */
   constructor(k, nums) {
      this.k = k;
      this.minHeap = new MinPriorityQueue();

      for (const num of nums)
         this.minHeap.enqueue(num);

      while (this.minHeap.size() > k)
         this.minHeap.dequeue();
   }
   /**
    * @param {number} val
    * @return {number}
    */
   add(val) {
      this.minHeap.enqueue(val);

      while (this.minHeap.size() > this.k)
         this.minHeap.dequeue();

      return this.minHeap.front()
   }
}


/**
 * Time complexity: O(m*nlogn)
 *     m: number of `add` calls
 *     n: `numbers` size
 * Auxiliary space complexity: O(n + m)
 * Tags:
 *     DS: list
 *     A: sorting
 */
class KthLargest2 {
   /**
    * @param {number} k
    * @param {number[]} nums
    */
   constructor(k, nums) {
      this.k = k;
      this.nums = nums.sort((a, b) => b - a).slice(0, this.k);
   };

   /** 
    * @param {number} val
    * @return {number}
    */
   add(val) {
      this.nums.push(val);
      this.nums.sort((a, b) => b - a);
      this.nums.pop();
      return this.nums[this.nums.length - 1]
   };
}



const kthLargest = new KthLargest(3, [4, 5, 8, 2]);
console.log(kthLargest.add(3) === 4);
console.log(kthLargest.add(5) === 5);
console.log(kthLargest.add(10) === 5);
console.log(kthLargest.add(9) === 8);
console.log(kthLargest.add(4) === 8);