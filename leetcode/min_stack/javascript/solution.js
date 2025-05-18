/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags: stack
 * In the class-based approach, the object defined using the class keyword and the methods directly within the class body.
 */
class MinStack {
   constructor() {
      this.stack = [];
      this.stackMin = [];
   };

   /**
    * @param {number} val
    * @return {void}
    */
   push(val) {
      this.stack.push(val);
      const minVal = Math.min(val, this.stackMin[this.stackMin.length - 1] || val);
      this.stackMin.push(minVal);
   };

   /**
    * @return {void}
    */
   pop() {
      this.stack.pop();
      this.stackMin.pop();
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
      return this.stackMin[this.stackMin.length - 1]
   }
}


const minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
console.log(minStack.getMin());  // return -3
minStack.pop();
console.log(minStack.top());  // return 0
console.log(minStack.getMin());  // return -2


// adding methods with prototype
var MinStack = function () {
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


// class as a function, methods are attached directly
var MinStack = function () {
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