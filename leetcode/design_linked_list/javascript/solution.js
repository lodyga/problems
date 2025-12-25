class ListNode {
   constructor(val = null, next = null) {
      this.val = val;
      this.next = next;
   }
}


/**
 * Time complexity:
 *     constructor: O(1)
 *     get: O(n)
 *     addAtHead: O(1)
 *     addAtTail: O(n)
 *     addAtIndex: O(n)
 *     deleteAtIndex: O(n)
 * Auxiliary space complexity O(n): 
 * Tags: 
 *     DS: linked list, singly linked list
 */
class MyLinkedList {
   constructor() {
      this.anchor = new ListNode();
   }

   get(index) {
      let node = this.anchor.next;
      while (index && node) {
         node = node.next;
         index--;
      }
      return (index === 0 && node) ? node.val : -1
   };

   addAtHead(val) {
      this.anchor.next = new ListNode(val, this.anchor.next);
   };

   addAtTail(val) {
      let node = this.anchor;
      while (node.next) {
         node = node.next;
      }
      node.next = new ListNode(val, null);
   };

   addAtIndex(index, val) {
      let node = this.anchor;
      while (index && node.next) {
         node = node.next;
         index--;
      }
      if (index === 0)
         node.next = new ListNode(val, node.next);
   };


   deleteAtIndex(index) {
      let node = this.anchor;
      while (index && node.next) {
         node = node.next;
         index--;
      }
      if (index === 0 && node.next)
         node.next = node.next.next;
   };
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let myLinkedList;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'MyLinkedList') {
         myLinkedList = new MyLinkedList(...argument);
         output.push(null);
      } else if (operation === 'addAtHead') {
         myLinkedList.addAtHead(...argument);
         output.push(null);
      } else if (operation === 'addAtTail') {
         myLinkedList.addAtTail(...argument);
         output.push(null);
      } else if (operation === 'addAtIndex') {
         myLinkedList.addAtIndex(...argument);
         output.push(null);
      } else if (operation === 'deleteAtIndex') {
         myLinkedList.deleteAtIndex(...argument);
         output.push(null);
      } else if (operation === 'get') {
         output.push(myLinkedList.get(...argument));
      }
   };
   return output
}


// Example Input
const operationsList = [
   ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
    ["MyLinkedList","deleteAtIndex"], 
    ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"], 
    ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"],
    ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
]

const argumentsList = [
   [[], [1], [3], [1, 2], [1], [1], [1]], 
    [[],[0]], 
    [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]], 
    [[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]], 
    [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
]

const expectedOutputList = [
   [null, null, null, null, 2, null, 3], 
    [null, null], 
    [null, null, null, null, null, null, null, null, null, 2, null, null], 
    [null,null,null,null,2,null,3,-1,null,null,3,null,-1],
    [null,null,null,null,null,null,null,null,4,null,null,null]
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
const myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);  // linked list becomes 1 -> 2 -> 3
console.log(myLinkedList.get(1));  // return 2
myLinkedList.deleteAtIndex(1);  // now the linked list is 1 -> 3
console.log(myLinkedList.get(1));  // return 3


class DoublyListNode {
   constructor(val = null, next = null, prev = null) {
      this.val = val;
      this.next = next;
      this.prev = prev;
   }
}

class MyLinkedList2 {
   constructor() {
      this.left = new DoublyListNode();
      this.right = new DoublyListNode();
      this.left.next = this.right;
      this.right.prev = this.left;
   }
   /**
    * @param {number} val
    * @return {void}
    */
   addAtHead(val) {
      let next = this.left.next;
      let prev = this.left;
      let node = new DoublyListNode(val, next, prev);
      next.prev = node;
      prev.next = node;
   }
   /**
    * @param {number} val
    * @return {void}
    */
   addAtTail(val) {
      let next = this.right;
      let prev = this.right.prev;
      let node = new DoublyListNode(val, next, prev);
      next.prev = node;
      prev.next = node;
   }
   /**
    * @param {number} index
    * @return {number}
    */
   get(index) {
      let node = this.left.next;

      while (index && node != this.right) {
         node = node.next;
         index--;
      }

      if (index === 0 && node != this.right)
         return node.val;

      else
         return -1;
   }
   /**
    * @param {number} index
    * @param {number} val
    * @return {void}
    */
   addAtIndex(index, val) {
      let next = this.left.next;

      while (index && next != this.right) {
         next = next.next;
         index--;
      }

      if (index === 0 && next) {
         let prev = next.prev;
         let node = new DoublyListNode(val, next, prev);
         prev.next = node;
         next.prev = node;
      }
   }
   /**
    * @param {number} index
    * @return {void}
    */
   deleteAtIndex(index) {
      let node = this.left.next;

      while (index && node.next != this.right) {
         node = node.next;
         index--;
      }

      if (index === 0 && node && node != this.right) {
         node.prev.next = node.next;
         node.next.prev = node.prev;
      }
   }
}




