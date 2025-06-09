class ListNode {
   constructor(val = null, next = null) {
      this.val = val;
      this.next = next;
   }
}


/**
 * Time complexity:
 *     construct: O(1)
 *     addAtHead: O(1)
 *     addAtTail: O(n)
 *     addAtIndex: O(n)
 *     get: O(n)
 *     deleteAtIndex: O(n)
 * Auxiliary space complexity O(n): 
 * Tags: linked list
 * singly linked list
 */
class MyLinkedList {
   constructor() {
      this.anchor = new ListNode();
   }

   addAtHead(val) {
      const anchor = this.anchor;
      const newHead = new ListNode(val, anchor.next);
      anchor.next = newHead;
   };

   addAtTail(val) {
      let node = this.anchor;
      while (node.next) {
         node = node.next;
      }
      const newTail = new ListNode(val, null);
      node.next = newTail;
   };

   addAtIndex(index, val) {
      let node = this.anchor;
      while (index && node.next) {
         index--;
         node = node.next;
      }
      if (index === 0) {
         const newNode = new ListNode(val, node.next);
         node.next = newNode;
      }
   };

   get(index) {
      let node = this.anchor;
      while (index && node.next) {
         index--;
         node = node.next;
      }
      return (index === 0 && node.next) ? node.next.val : -1
   };

   deleteAtIndex(index) {
      let node = this.anchor;
      while (index && node.next) {
         index--;
         node = node.next;
      }
      if (index === 0 && node.next)
         node.next = node.next.next;
   };
}


const myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);  // linked list becomes 1 -> 2 -> 3
console.log(myLinkedList.get(1));  // return 2
myLinkedList.deleteAtIndex(1);  // now the linked list is 1 -> 3
console.log(myLinkedList.get(1));  // return 3








var ListNode = function (val = 0, next = null, prev = null) {
  this.val = val;
  this.next = next;
  this.prev = prev;
};

var MyLinkedList = function () {
  this.left = new ListNode();
  this.right = new ListNode();
  this.left.next = this.right;
  this.right.prev = this.left;
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function (val) {
  let next = this.left.next;
  let prev = this.left
  let node = new ListNode(val, next, prev);
  next.prev = node;
  prev.next = node;
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function (val) {
  let next = this.right;
  let prev = this.right.prev;
  let node = new ListNode(val, next, prev);
  next.prev = node;
  prev.next = node;
};

/** 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function (index) {
  let node = this.left.next;

  while (index && node != this.right) {
    node = node.next;
    index--;
  }

  if (index === 0 && node != this.right)
    return node.val
  else
    return -1
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function (index, val) {
  let next = this.left.next;

  while (index && next != this.right) {
    next = next.next;
    index--;
  }

  if (index === 0 && next) {
    let prev = next.prev;
    let node = new ListNode(val, next, prev);
    prev.next = node;
    next.prev = node;
  }
};
/** 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function (index) {
  let node = this.left.next;

  while (index && node.next != this.right) {
    node = node.next;
    index--;
  }

  if (index === 0 && node && node != this.right) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
  }
};
