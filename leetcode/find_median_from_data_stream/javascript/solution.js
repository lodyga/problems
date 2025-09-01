import { MaxPriorityQueue, MinPriorityQueue } from '@datastructures-js/priority-queue';


/**
 * Time complexity:
 *     addNum: O(logn)
 *     findMedian: O(1)
 * Auxiliary space complexity: O(n)
 * Tags: heap
 */
class MedianFinder {
   constructor() {
      // max heap
      this.lowHeap = new MaxPriorityQueue();
      // min heap
      this.highHeap = new MinPriorityQueue();
      this.index = 0;
   };

   /**
    * @param {number} number
    * @return {void}
    */
   addNum(number) {
      if (this.index % 2) {
         this.highHeap.enqueue(number);
         const lowNumber = this.highHeap.dequeue();
         this.lowHeap.enqueue(lowNumber);
      } else {
         this.lowHeap.enqueue(number);
         const highNumber = this.lowHeap.dequeue();
         this.highHeap.enqueue(highNumber)
      }
      this.index++;
   };

   /**
    * @return {number}
    */
   findMedian() {
      if (this.index % 2) {
         return this.highHeap.front();
      } else {
         return (this.lowHeap.front() + this.highHeap.front()) / 2
      }
   };
}


// const medianFinder = new MedianFinder();
// medianFinder.addNum(1);    // arr = [1]
// medianFinder.addNum(2);    // arr = [1, 2]
// console.log(medianFinder.findMedian()); // return 1.5 (i.e., (1 + 2) / 2)
// medianFinder.addNum(3);    // arr[1, 2, 3]
// console.log(medianFinder.findMedian()); // return 2.0


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
         medianFinder = new MedianFinder();
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
// const operations = ['MedianFinder', 'addNum', 'addNum', 'findMedian', 'addNum', 'findMedian']
// const args = [[], [1], [2], [], [3], []]
// const expected_output = [null, null, null, 1.5, null, 2.0]

// Run tests
//const test_output = testInput(operations, args)
//console.log(JSON.stringify(test_output) === JSON.stringify(expected_output))
//console.log(test_output)


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