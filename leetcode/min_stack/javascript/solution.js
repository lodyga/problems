/**
 * Time complexity: O(1)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: stack
 * In the class-based approach, the object defined using the class keyword and the methods directly within the class body.
 */
class MinStack {
   constructor() {
      this.stack = [];
      this.minStack = [];
   }

   /**
    * @param {number} val
    * @return {void}
    */
   push(val) {
      this.stack.push(val);
      const minStack = this.minStack
      if (minStack.length)
         minStack.push(Math.min(minStack[minStack.length - 1], val));
      else
         minStack.push(val);
   }

   /**
    * @return {void}
    */
   pop() {
      this.stack.pop();
      this.minStack.pop();
   }

   /**
    * @returns {number}
    */
   top() {
      return this.stack[this.stack.length - 1]
   }

   /**
    * @returns {number}
    */
   getMin() {
      return this.minStack[this.minStack.length - 1]
   }
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (cls, operations, args) => {
   const res = []

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === cls.name) {
         const instance = new TimeMap(...argument);
         res.push(null);
         continue
      } 

      const method = getattr(instance, operation);
        const result = method(...argument);
        res.push(result);

   return res
}


// Example Input
const operationsList = [
   ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
]

const argumentsList = [
   [[], [-2], [0], [-3], [], [], [], []],
]

const expectedOutputList = [
   [None, None, None, None, -3, None, 0, -2]
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
const runTests = (cls, operationsList, argumentsList, expectedOutputList, showOutput) => {
   const res = [];

   for (let index = 0; index < operationsList.length; index++) {
      const operations = operationsList[index];
      const args = argumentsList[index];
      const expectedOutput = expectedOutputList[index];
      
      if (showOutput) {
         res.push([testInput(cls, operations, args), expectedOutput])
      } else {
         res.push(JSON.stringify(testInput(cls, operations, args)) === JSON.stringify(expectedOutput))
      }
   }
   return res
}
console.log(runTests(MinStack, operationsList, argumentsList, expectedOutputList))


// Example 1
const minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
console.log(minStack.getMin() === -3);
minStack.pop();
console.log(minStack.top() === 0);
console.log(minStack.getMin() === -2);



// class as a function, methods are attached directly
const MinStack2 = function () {
   this.stack = [];
   this.stackMin = [];

   this.push = function (val) {
      this.stack.push(val);
      val = Math.min(val, this.stackMin[this.stackMin.length - 1] ?? val)
      this.stackMin.push(val)
   };

   this.pop = function () {
      this.stack.pop();
      this.stackMin.pop();
   };

   this.top = function () {
      return this.stack[this.stack.length - 1]
   };

   this.getMin = function () {
      return this.stackMin[this.stackMin.length - 1]
   };
};


// adding methods with prototype
const MinStack3 = function () {
   this.stack = [];
   this.stackMin = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
   this.stack.push(val);
   val = Math.min(val, this.stackMin[this.stackMin.length - 1] ?? val)
   this.stackMin.push(val)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
   this.stack.pop();
   this.stackMin.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
   return this.stack[this.stack.length - 1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
   return this.stackMin[this.stackMin.length - 1]
};


