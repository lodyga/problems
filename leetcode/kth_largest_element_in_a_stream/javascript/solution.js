// import { MinPriorityQueue } from '@datastructures-js/priority-queue';


/**
 * Time complexity:
 *     constructor: O(nlogn)
 *     add: O(log(k))
 *     n: stream size
 *     k: highest test scores size
 * Auxiliary space complexity: O(1)
 * Tags:
 *     DS: heap
 *     A: iteration
 */
class KthLargest {
   /**
    * @param {number} k
    * @param {number[]} stream
    */
   constructor(k, stream) {
      this.k = k;
      this.minHeap = new MinPriorityQueue();

      stream.forEach(element => {
         this.minHeap.enqueue(element)
      })

      while (this.minHeap.size() > k) {
         this.minHeap.dequeue();
      }
   }

   /**
    * @param {number} val
    * @return {number}
    */
   add(val) {
      this.minHeap.enqueue(val);

      while (this.minHeap.size() > this.k) {
         this.minHeap.dequeue();
      }

      return this.minHeap.front();
   }
}


/**
 * Time complexity:
 *     constructor: O(nlogn)
 *     add: O(klog(k))
 *     n: stream size
 *     k: highest test scores size
 * Auxiliary space complexity: O(n + k)
 * Tags:
 *     DS: list
 *     A: sorting
 */
class KthLargest {
   /**
    * @param {number} k
    * @param {number[]} stream
    */
   constructor(k, stream) {
      this.k = k;
      this.stream = stream.sort((a, b) => b - a).slice(0, this.k);
   };

   /** 
    * @param {number} val
    * @return {number}
    */
   add(val) {
      this.stream.push(val);
      this.stream.sort((a, b) => b - a);
      
      if (this.stream.length > this.k) {
         this.stream.pop();
      }
      
      return this.stream[this.stream.length - 1];
   }
}



const kthLargest = new KthLargest(3, [4, 5, 8, 2]);
console.log(kthLargest.add(3) === 4);
console.log(kthLargest.add(5) === 5);
console.log(kthLargest.add(10) === 5);
console.log(kthLargest.add(9) === 8);
console.log(kthLargest.add(4) === 8);
