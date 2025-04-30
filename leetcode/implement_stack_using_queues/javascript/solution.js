import { Queue } from '@datastructures-js/queue';

class MyStack {
   /**
    * Time complexity:
    *     push: O(1)
    *     pop: O(n)
    *     top: O(n)
    *     empty: O(1)
    * Auxiliary space complexity: O(n)
    * Tags: queue, stack
    * @param {}
    * @return {}
    */
   constructor() {
      this.queue = new Queue();
   }
   push(number) {
      this.queue.push(number);
   };

   pop() {
      for (let index = 0; index < this.queue.size() - 1; index++) {
         this.queue.push(this.queue.pop());
      }
      return this.queue.pop()
   };

   top() {
      for (let index = 0; index < this.queue.size() - 1; index++) {
         this.queue.push(this.queue.pop());
      }
      const topNumber = this.queue.pop();
      this.queue.push(topNumber);
      return topNumber
   };

   empty() {
      return this.queue.isEmpty()
   };
}


const myStack = new MyStack();
myStack.push(1);
myStack.push(2);
console.log(myStack.top())  // return 2
console.log(myStack.pop())  // return 2
console.log(myStack.empty())  // return false