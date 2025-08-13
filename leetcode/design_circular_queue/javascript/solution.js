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


const myCircularQueue = new MyCircularQueue(3)
console.log(myCircularQueue.enQueue(1))  // return true
console.log(myCircularQueue.enQueue(2))  // return true
console.log(myCircularQueue.enQueue(3))  // return true
console.log(myCircularQueue.enQueue(4))  // return false
console.log(myCircularQueue.Rear())  // return 3
console.log(myCircularQueue.isFull())  // return true
console.log(myCircularQueue.deQueue())  // return true
console.log(myCircularQueue.enQueue(4))  // return true
console.log(myCircularQueue.Rear())  // return 4