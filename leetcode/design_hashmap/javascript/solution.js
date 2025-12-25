class ListNode {
   constructor(key = null, val = null, next = null) {
      this.key = key;
      this.val = val;
      this.next = next;
   }
}


class MyHashMap {
   /**
    * Time complexity: 
    *     put: O(1)
    *     get: O(1)
    *     remove: O(1)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: linked list, hash map
    *     A: iteration
    * @param {}
    * @return {}
    */

   constructor() {
      this.bucketSize = 10 ** 4;
      this.map = Array.from({ length: this.bucketSize }, () => new ListNode());
   };

   /**
    * @param {number} key 
    * @returns {number}
    */
   _getHashCode(key) {
      return key % this.bucketSize;
   }

   /**
    * @param {number} key 
    * @param {number} val 
    * @returns {void}
    */
   put(key, val) {
      const index = this._getHashCode(key);
      let node = this.map[index];

      while (node.next) {
         if (node.next.key === key) {
            node.next.val = val;
            return
         }
         node = node.next;
      }
      node.next = new ListNode(key, val);
   };

   /**
    * @param {number} key 
    * @returns {number}
    */
   get(key) {
      const index = this._getHashCode(key);
      let node = this.map[index];

      while (node.next) {
         if (node.next.key === key) {
            return node.next.val
         }
         node = node.next;
      }
      return -1
   };

   /**
    * @param {number} key 
    * @returns {void}
    */
   remove(key) {
      const index = this._getHashCode(key);
      let node = this.map[index];

      while (node.next) {
         if (node.next.key === key) {
            node.next = node.next.next;
            return
         }
         node = node.next;
      }
   };
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let myHathSet;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'MyHashMap') {
         myHathSet = new MyHashMap(...argument);
         output.push(null);
      } else if (operation === 'put') {
         myHathSet.put(...argument);
         output.push(null);
      } else if (operation === 'remove') {
         myHathSet.remove(...argument);
         output.push(null);
      } else if (operation === 'get') {
         output.push(myHathSet.get(...argument));
      }
   };
   return output
}


// Example Input
const operationsList = [
   ["MyHashMap","put","put","get","get","put","get","remove","get"]
]

const argumentsList = [
   [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
]

const expectedOutputList = [
   [null,null,null,1,-1,null,1,null,-1]
]


// Run tests
/**
 * Run a batch of TimeMap tests and compare outputs with expected results.
 * If show_output is true, returns [(actual, expected), ...] instead of booleans.
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
const myHashMap = new MyHashMap()
myHashMap.put(1, 1)  // The map is now[[1, 1]]
myHashMap.put(2, 2)  // The map is now[[1, 1], [2, 2]]
console.log(myHashMap.get(1))  // return 1, The map is now[[1, 1], [2, 2]]
console.log(myHashMap.get(3))  // return -1(i.e., not found), The map is now[[1, 1], [2, 2]]
myHashMap.put(2, 1)  // The map is now[[1, 1], [2, 1]]
console.log(myHashMap.get(2))  // return 1, The map is now[[1, 1], [2, 1]]
myHashMap.remove(2)  // remove the mapping for 2, The map is now[[1, 1]]
console.log(myHashMap.get(2))  // return -1(i.e., not found), The map is now[[1, 1]]