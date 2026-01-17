/**
 * Time complexity: 
 *     O(1): push, pop
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: hash map
 *     A: iteration
 */
class FreqStack {
   constructor() {
      this.valFreq = new Map();  // {value: frequency, ...}
      this.freqBucket = new Map();  // {frequency1: [value1, value2], ...}
      this.maxFreq = 0;
   };

   /** 
    * @param {number} val
    * @return {void}
    */
   push(val) {
      this.valFreq.set(val, (this.valFreq.get(val) || 0) + 1);

      const freq = this.valFreq.get(val);
      if (!this.freqBucket.has(freq)) {
         this.freqBucket.set(freq, []);
         this.maxFreq = freq;
      }
      this.freqBucket.get(freq).push(val);
   };

   /**
    * @return {number}
    */
   pop() {
      const freq = this.maxFreq;
      const val = this.freqBucket.get(freq).pop();
      this.valFreq.set(val, this.valFreq.get(val) - 1);

      if (this.freqBucket.get(this.maxFreq).length === 0) {
         this.freqBucket.delete(this.maxFreq);
         this.maxFreq--;
      }
      return val
   };
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let freqStack;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'FreqStack') {
         freqStack = new FreqStack(...argument);
         output.push(null);
      } else if (operation === 'push') {
         freqStack.push(...argument);
         output.push(null);
      } else if (operation === 'pop') {
         output.push(freqStack.pop(...argument));
      }
   };
   return output
}


// Example Input
const operationsList = [
   ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
   ["FreqStack", "push", "push", "push", "push", "pop", "pop", "push", "push", "push", "pop", "pop", "pop"],
]

const argumentsList = [
   [[], [5], [7], [5], [7], [4], [5], [], [], [], []],
   [[], [1], [1], [1], [2], [], [], [2], [2], [1], [], [], []],
]

const expectedOutputList = [
   [null, null, null, null, null, null, null, 5, 7, 5, 4],
   [null, null, null, null, null, 1, 1, null, null, null, 2, 1, 2],
]


// Run tests
/**
 * Run a batch of TimeMap tests and compare outputs with expected results.
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
const freqStack = new FreqStack();
freqStack.push(5);
freqStack.push(7);
freqStack.push(5);
freqStack.push(7);
freqStack.push(4);
freqStack.push(5);
console.log(freqStack.pop() === 5);
console.log(freqStack.pop() === 7);
console.log(freqStack.pop() === 5);
console.log(freqStack.pop() === 4);
