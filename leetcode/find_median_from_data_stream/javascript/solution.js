import { MaxPriorityQueue, MinPriorityQueue } from '@datastructures-js/priority-queue';


/**
 * Time complexity:
 *     addNum: O(logn)
 *     findMedian: O(1)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: heap
 *     A: iteration
 */
class MedianFinder {
   constructor() {
      this.leftHeap = new MaxPriorityQueue();
      this.rightHeap = new MinPriorityQueue();
   };

   /**
    * @param {number} num
    * @return {void}
    */
   addNum(num) {
      if ((this.leftHeap.size() + this.rightHeap.size()) % 2) {
         this.rightHeap.enqueue(num);
         const lownum = this.rightHeap.dequeue();
         this.leftHeap.enqueue(lownum);
      } else {
         this.leftHeap.enqueue(num);
         const highNumber = this.leftHeap.dequeue();
         this.rightHeap.enqueue(highNumber)
      }
   };

   /**
    * @return {number}
    */
   findMedian() {
      if ((this.leftHeap.size() + this.rightHeap.size()) % 2) {
         return this.rightHeap.front();
      } else {
         return (this.leftHeap.front() + this.rightHeap.front()) / 2
      }
   };
}




/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let medianFinder;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'MedianFinder') {
         medianFinder = new MedianFinder(...argument);
         output.push(null);
      } else if (operation === 'addNum') {
         medianFinder.addNum(...argument);
         output.push(null);
      } else if (operation === 'findMedian') {
         output.push(medianFinder.findMedian());
      }
   }
   return output
}


// Example Input
const operationsList = [
   ['MedianFinder', 'addNum', 'addNum', 'findMedian', 'addNum', 'findMedian'],
   ['MedianFinder', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian'],
   ['MedianFinder', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian']
]

const argumentsList = [
   [[], [1], [2], [], [3], []],
   [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0], [], [6], [], [3], [], [1], [], [0], [], [0], []],
   [[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []]
]

const expectedOutputList = [
   [null, null, null, 1.5, null, 2.0],
   [null, null, 6.00000, null, 8.00000, null, 6.00000, null, 6.00000, null, 6.00000, null, 5.50000, null, 6.00000, null, 5.50000, null, 5.00000, null, 4.00000, null, 3.00000],
   [null, null, -1.00000, null, -1.50000, null, -2.00000, null, -2.50000, null, -3.00000]
]


// Run tests
/**
 * Run a batch of MedianFinder tests and compare outputs with expected results.
 * If show_output is True, returns [(actual, expected), ...] instead of booleans.
 * @param {string[][]} operationsList 
 * @param {number[][][]} argumentsList 
 * @param {number[][]} expectedOutputList 
 * @returns {boolean}
 */
const runTests = (operationsList, argumentsList, expectedOutputList, showOutput) => {
   const output = [];

   for (let index = 0; index < operationsList.length; index++) {
      const operations = operationsList[index];
      const args = argumentsList[index];
      const expectedOutput = expectedOutputList[index];
      if (showOutput) {
         output.push([testInput(operations, args), expectedOutput])
      } else {
         output.push(JSON.stringify(testInput(operations, args)) === JSON.stringify(expectedOutput))
      }
   }
   return output
}
console.log(runTests(operationsList, argumentsList, expectedOutputList))


// Example 1
const medianFinder = new MedianFinder();
medianFinder.addNum(1);
medianFinder.addNum(2);
console.log(medianFinder.findMedian() === 1.5);
medianFinder.addNum(3);
console.log(medianFinder.findMedian() === 2);
