class MyQueue {
   /**
    * Time complexity: O(1)
    *     push: O(1)
    *     pop: O(1)
    *     peek: O(1)
    *     empty: O(1)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: stack, queue
    *     A: iteration
    */
   constructor() {
      this.stack = [];
      this.reversedStack = [];
   };

   /**
    * @return {void}
    */
   _reverseStack() {
      if (this.reversedStack.length === 0) {
         while (this.stack.length) {
            this.reversedStack.push(this.stack.pop());
         }
      }
   };

   /**
    * @param {number} number
    * @return {void}
    */
   push(number) {
      this.stack.push(number)
   };

   /**
    * @return {number}
    */
   pop() {
      this._reverseStack();
      return this.reversedStack.pop()
   };

   /**
    * @return {number}
    */
   peek() {
      this._reverseStack();
      return this.reversedStack[this.reversedStack.length - 1]
   };

   /**
    * @return {void}
    */
   empty() {
      return (
         this.stack.length === 0 &&
         this.reversedStack.length === 0
      )
   };
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let myQueue;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'MyQueue') {
         myQueue = new MyQueue(...argument);
         output.push(null);
      } else if (operation === 'push') {
         myQueue.push(...argument);
         output.push(null);
      } else if (operation === 'pop') {
         output.push(myQueue.pop(...argument));
      } else if (operation === 'peek') {
         output.push(myQueue.peek(...argument));
      } else if (operation === 'empty') {
         output.push(myQueue.empty(...argument));
      };
   };
   return output
}


// Example Input
const operationsList = [
   ['MyQueue','push','push','peek','pop','empty']
]

const argumentsList = [
   [[],[1],[2],[],[],[]]
]

const expectedOutputList = [
   [null,null,null,1,1,false]
]


// Run tests
/**
 * Run a batch of myStack tests and compare outputs with expected results.
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


const myQueue = new MyQueue()
myQueue.push(1)  // queue is: [1]
myQueue.push(2)  // queue is: [1, 2] (leftmost is front of the queue)
console.log(myQueue.peek())  // return 1
console.log(myQueue.pop())  // return 1, queue is [2]
console.log(myQueue.empty())  // return false