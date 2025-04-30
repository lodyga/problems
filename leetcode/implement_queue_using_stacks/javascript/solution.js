class MyQueue {
   /**
    * Time complexity: O(1)
    *     push: O(1)
    *     pop: O(1)
    *     peek: O(1)
    *     empty: O(1)
    * Auxiliary space complexity: O(n)
    * Tags: stack, queue
    */
   constructor() {
      this.stack = [];
      this.reversedStack = [];
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
      this.reverseStack();
      return this.reversedStack.pop()
   };

   /**
    * @return {number}
    */
   peek() {
      this.reverseStack();
      return this.reversedStack[this.reversedStack.length - 1]
   };

   /**
    * @return {void}
    */
   reverseStack() {
      if (this.reversedStack.length === 0) {
         while (this.stack.length) {
            this.reversedStack.push(this.stack.pop());
         }
      }
   }

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


const myQueue = new MyQueue()
myQueue.push(1)  // queue is: [1]
myQueue.push(2)  // queue is: [1, 2] (leftmost is front of the queue)
console.log(myQueue.peek())  // return 1
console.log(myQueue.pop())  // return 1, queue is [2]
console.log(myQueue.empty())  // return false