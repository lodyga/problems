import { Queue } from '@datastructures-js/queue';


/**
 * Time complexity:
 *     push: O(1)
 *     pop: O(n)
 *     top: O(n)
 *     empty: O(1)
 * Auxiliary space complexity: O(n)
 * Tags: 
 *     DS: queue, stack
 *     A: iteration
 */
class MyStack {
   constructor() {
      this.queue = new Queue();
   }
   push(number) {
      this.queue.push(number);
   };

   pop() {
      const queue = this.queue;
      for (let index = 0; index < queue.size() - 1; index++) {
         queue.push(queue.pop());
      }
      return queue.pop()
   };

   top() {
      const queue = this.queue;
      for (let index = 0; index < queue.size() - 1; index++)
         queue.push(queue.pop());
      const num = queue.pop();
      queue.push(num);
      return num
   };

   empty() {
      return this.queue.isEmpty()
   };
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let myStack;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'MyStack') {
         myStack = new MyStack();
         output.push(null);
      } else if (operation === 'push') {
         myStack.push(...argument);
         output.push(null);
      } else if (operation === 'pop') {
         output.push(myStack.pop(...argument));
      } else if (operation === 'top') {
         output.push(myStack.top(...argument));
      } else if (operation === 'empty') {
         output.push(myStack.empty(...argument));
      };
   };
   return output
}


// Example Input
const operationsList = [
   ['MyStack', 'push', 'push', 'top', 'pop', 'empty']
]

const argumentsList = [
   [[], [1], [2], [], [], []]
]

const expectedOutputList = [
   [null, null, null, 2, 2, false]
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


const myStack = new MyStack();
myStack.push(1);
myStack.push(2);
console.log(myStack.top())  // return 2
console.log(myStack.pop())  // return 2
console.log(myStack.empty())  // return false