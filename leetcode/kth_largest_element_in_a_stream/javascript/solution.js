import { MinPriorityQueue } from '@datastructures-js/priority-queue';


/**
 * @param {number} k
 * @param {number[]} numbers
 */
class KthLargest {
   /**
    * Time complexity: O(m*logk)
    *     m: number of `add` calls
    *     k: the number of highest test scores
    * Auxiliary space complexity: O(k)
    * Tags: heap
    * @param {number} k
    * @param {number[]} numbers
    */
   constructor(k, numbers) {
      this.k = k;
      this.minHeap = new MinPriorityQueue();

      for (const number of numbers)
         this.minHeap.enqueue(number);

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


import { MinHeap } from '@datastructures-js/heap';


class KthLargest {
   /**
    * Time complexity: O(m*logk)
    *     m: number of `add` calls
    *     k: the number of highest test scores
    * Auxiliary space complexity: O(k)
    * Tags: heap
    * @param {number} k
    * @param {number[]} numbers
    */
   constructor(k, numbers) {
      this.k = k;
      this.numbersHeap = MinHeap.heapify(numbers)
      while (this.numbersHeap.size() > this.k)
         this.numbersHeap.pop();
   };

   add(val) {
      this.numbersHeap.push(val);
      this.numbersHeap.pop();
      return this.numbersHeap.top()
   };
}


/**
 * Time complexity: O(m*nlogn)
 *     m: number of `add` calls
 *     n: `numbers` size
 * Auxiliary space complexity: O(n + m)
 * Tags: sorting
 */
class KthLargest {
   /**
    * @param {number} k
    * @param {number[]} numbers
    */
   constructor(k, numbers) {
      this.k = k;
      this.numbers = numbers.sort((a, b) => b - a).slice(0, this.k);
   };

   /** 
    * @param {number} val
    * @return {number}
    */
   add(val) {
      this.numbers.push(val);
      this.numbers.sort((a, b) => b - a);
      this.numbers.pop();
      return this.numbers[this.numbers.length - 1]
   };
}



const kthLargest = new KthLargest(3, [4, 5, 8, 2]);
console.log(kthLargest.add(3) === 4);
console.log(kthLargest.add(5) === 5);
console.log(kthLargest.add(10) === 5);
console.log(kthLargest.add(9) === 8);
console.log(kthLargest.add(4) === 8);