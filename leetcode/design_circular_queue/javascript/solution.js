class ListNode {
   constructor(val = null, next = null) {
      this.val = val;
      this.next = next;
   }
}


/**
 * Time complexity: O(1)
 * Auxiliary space complexity: O(n)
 * Tags: linked list, queue
 */
class MyCircularQueue {
   constructor(k) {
      this.size = 0
      this.sizeLimit = k
      this.anchor = new ListNode()
      this.lastNode = this.anchor
   };

   enQueue(value) {
      if (this.isFull()) {
         return false
      }
      this.size++;
      this.lastNode.next = new ListNode(value)
      this.lastNode = this.lastNode.next
      return true
   };

   deQueue() {
      if (this.isEmpty()) {
         return false
      }
      this.size--
      this.anchor.next = this.anchor.next.next
      if (this.isEmpty()) {
         this.lastNode = this.anchor
      }
      return true
   }

   Front() {
      if (this.isEmpty()) {
         return -1
      }
      return this.anchor.next.val
   };

   Rear() {
      if (this.isEmpty()) {
         return -1
      }
      return this.lastNode.val
   };

   isEmpty() {
      return this.size === 0
   };

   isFull() {
      return this.size === this.sizeLimit
   };
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let myCircularQueue;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'MyCircularQueue') {
         myCircularQueue = new MyCircularQueue(...argument);
         output.push(null);
      } else if (operation === 'enQueue') {
         output.push(myCircularQueue.enQueue(...argument));
      } else if (operation === 'deQueue') {
         output.push(myCircularQueue.deQueue(...argument));
      } else if (operation === 'Front') {
         output.push(myCircularQueue.Front(...argument));
      } else if (operation === 'Front') {
         output.push(myCircularQueue.Front(...argument));
      } else if (operation === 'isEmpty') {
         output.push(myCircularQueue.isEmpty(...argument));
      } else if (operation === 'isFull') {
         output.push(myCircularQueue.isFull(...argument));
      }
   };
   return output
}


// Example Input
const operationsList = [
   ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"],
   ["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"],
   ["MyCircularQueue","enQueue","deQueue","enQueue","enQueue","deQueue","isFull","isFull","Front","deQueue","enQueue","Front","enQueue","enQueue","Rear","Rear","deQueue","enQueue","enQueue","Rear","Rear","Front","Rear","Rear","deQueue","enQueue","Rear","deQueue","Rear","Rear","Front","Front","enQueue","enQueue","Front","enQueue","enQueue","enQueue","Front","isEmpty","enQueue","Rear","enQueue","Front","enQueue","enQueue","Front","enQueue","deQueue","deQueue","enQueue","deQueue","Front","enQueue","Rear","isEmpty","Front","enQueue","Front","deQueue","enQueue","enQueue","deQueue","deQueue","Front","Front","deQueue","isEmpty","enQueue","Rear","Front","enQueue","isEmpty","Front","Front","enQueue","enQueue","enQueue","Rear","Front","Front","enQueue","isEmpty","deQueue","enQueue","enQueue","Rear","deQueue","Rear","Front","enQueue","deQueue","Rear","Front","Rear","deQueue","Rear","Rear","enQueue","enQueue","Rear","enQueue"]
]

const argumentsList = [
   [[3],[1],[2],[3],[4],[],[],[],[4],[]],
   [[6],[6],[],[],[],[5],[],[],[],[],[],[]],
   [[81],[69],[],[92],[12],[],[],[],[],[],[28],[],[13],[45],[],[],[],[24],[27],[],[],[],[],[],[],[88],[],[],[],[],[],[],[53],[39],[],[28],[66],[17],[],[],[47],[],[87],[],[92],[94],[],[59],[],[],[99],[],[],[84],[],[],[],[52],[],[],[86],[30],[],[],[],[],[],[],[45],[],[],[83],[],[],[],[22],[77],[23],[],[],[],[14],[],[],[90],[57],[],[],[],[],[34],[],[],[],[],[],[],[],[49],[59],[],[71]]
]

const expectedOutputList = [
   [null, true, true, true, false, 3, true, true, true, 4],
   [null, true, 6, 6, true, true, 5, true, -1, false, false, false],
   [null, true, true, true, true, true, false, false, 12, true, true, 28, true, true, 45, 45, true, true, true, 27, 27, 13, 27, 27, true, true, 88, true, 88, 88, 24, 24, true, true, 24, true, true, true, 24, false, true, 47, true, 24, true, true, 24, true, true, true, true, true, 53, true, 84, false, 53, true, 53, true, true, true, true, true, 66, 66, true, false, true, 45, 17, true, false, 17, 17, true, true, true, 23, 17, 17, true, false, true, true, true, 57, true, 57, 87, true, true, 34, 92, 34, true, 34, 34, true, true, 59, true]
]


// Run tests
/**
 * Run a batch of TimeMap tests and compare outputs with expected results.
 * If show_output is true, returns [(actual, expected), ...] instead of booleans.
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
const myCircularQueue = new MyCircularQueue(3)
console.log(myCircularQueue.enQueue(1) === true)
console.log(myCircularQueue.enQueue(2) === true)
console.log(myCircularQueue.enQueue(3) === true)
console.log(myCircularQueue.enQueue(4) === false)
console.log(myCircularQueue.Rear() === 3)
console.log(myCircularQueue.isFull() === true)
console.log(myCircularQueue.deQueue() === true)
console.log(myCircularQueue.enQueue(4) === true)
console.log(myCircularQueue.Rear() === 4)
