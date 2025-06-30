/**
 * Time complexity: 
 *     O(1): push, pop
 * Auxiliary space complexity: O(n)
 * Tags: stack, hash map
 */
class FreqStack {
   constructor() {
      this.numberFrequency = new Map();
      this.frequencyBucket = new Map();
      this.maxFrequency = 0;
   };

   /** 
    * @param {number} number
    * @return {void}
    */
   push(number) {
      this.numberFrequency.set(number, (this.numberFrequency.get(number) || 0) + 1);
      const frequency = this.numberFrequency.get(number)
      this.maxFrequency = Math.max(this.maxFrequency, frequency);

      if (!this.frequencyBucket.has(frequency)) {
         this.frequencyBucket.set(frequency, []);
      }
      this.frequencyBucket.get(frequency).push(number);
   };

   /**
    * @return {number}
    */
   pop() {
      const number = this.frequencyBucket.get(this.maxFrequency).pop();
      this.numberFrequency.set(number, this.numberFrequency.get(number) - 1);

      if (this.frequencyBucket.get(this.maxFrequency).length === 0) {
         this.frequencyBucket.delete(this.maxFrequency);
         this.maxFrequency--;
      }
      return number
   };
}


const freqStack = new FreqStack();
freqStack.push(5);  // The stack is [5]
freqStack.push(7);  // The stack is [5,7]
freqStack.push(5);  // The stack is [5,7,5]
freqStack.push(7);  // The stack is [5,7,5,7]
freqStack.push(4);  // The stack is [5,7,5,7,4]
freqStack.push(5);  // The stack is [5,7,5,7,4,5]
console.log(freqStack.pop());  // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
console.log(freqStack.pop());  // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
console.log(freqStack.pop());  // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
console.log(freqStack.pop());  // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const test_input = function (operations, args) {
   const result = []

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'FreqStack') {
         const freqStack = new FreqStack();
         result.push(null);
      } else if (operation === 'push') {
         freqStack.push(...argument);
         result.push(null);
      } else if (operation === 'pop') {
         result.push(freqStack.pop());
      }
   }

   return result
}

// Example Input
const operations = ['FreqStack', 'push', 'push', 'push', 'push', 'push', 'push', 'pop', 'pop', 'pop', 'pop']
const args = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
const expected_output = [null, null, null, null, null, null, null, 5, 7, 5, 4]

// const operations = ['FreqStack','push','push','push','push','pop', 'pop', 'push', 'push', 'push', 'pop', 'pop', 'pop']
// const args = [[],[1], [1], [1], [2], [], [], [2], [2], [1], [], [], []]
// const expected_output = [null, null, null, null, null, 1, 1, null, null, null, 2, 1, 2]

// Run tests
const test_output = test_input(operations, args)
console.log(JSON.stringify(test_output) === JSON.stringify(expected_output))
// console.log(test_output)