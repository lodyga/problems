import { ListNode } from '../../../../JS/linked-list-utils.js'


/**
 * Represents a node in a singly-linked list.
 * class ListNode {
 *    constructor(val = null, next = null) {
 *       this.val = val;
 *       this.next = next;
 *    }
 * }
 */


class MyHashSet {
   /**
    * Time complexity:
    *     constructor: O(n)
    *     add: O(1)
    *     contains: O(1)
    *     remove: O(1)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: linked list, hash set
    *     A: iteration
    */
   constructor() {
      this.bucketSize = 10 ** 4;
      this.set = Array.from({ length: this.bucketSize }, () => new ListNode());
   };

   /**
    * @param {number} key 
    * @returns {number}
    */
   _getHashCode(key) {
      return key % this.bucketSize
   };

   /**
    * @param {number} key 
    * @returns {void}
    */
   add(key) {
      if (!this.contains(key)) {
         const index = this._getHashCode(key);
         const node = this.set[index];
         node.next = new ListNode(key, node.next);
      }
   };

   /**
    * @param {number} key 
    * @returns {boolean}
    */
   contains(key) {
      const index = this._getHashCode(key);
      let node = this.set[index];

      while (node.next) {
         if (node.next.val == key)
            return true
         node = node.next;
      }
      return false
   };

   /**
    * @param {number} key 
    * @returns {void}
    */
   remove(key) {
      const index = this._getHashCode(key);
      let node = this.set[index];

      while (node.next) {
         if (node.next.val == key) {
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

      if (operation === 'MyHashSet') {
         myHathSet = new MyHashSet(...argument);
         output.push(null);
      } else if (operation === 'add') {
         myHathSet.add(...argument);
         output.push(null);
      } else if (operation === 'remove') {
         myHathSet.remove(...argument);
         output.push(null);
      } else if (operation === 'contains') {
         output.push(myHathSet.contains(...argument));
      }
   };
   return output
}


// Example Input
const operationsList = [
   ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"],
   ["MyHashSet","contains","remove","add","add","contains","remove","contains","contains","add","add","add","add","remove","add","add","add","add","add","add","add","add","add","add","contains","add","contains","add","add","contains","add","add","remove","add","add","add","add","add","contains","add","add","add","remove","contains","add","contains","add","add","add","add","add","contains","remove","remove","add","remove","contains","add","remove","add","add","add","add","contains","contains","add","remove","remove","remove","remove","add","add","contains","add","add","remove","add","add","add","add","add","add","add","add","remove","add","remove","remove","add","remove","add","remove","add","add","add","remove","remove","remove","add","contains","add"]
]

const argumentsList = [
   [[],[1],[2],[1],[3],[2],[2],[2],[2]],
   [[],[72],[91],[48],[41],[96],[87],[48],[49],[84],[82],[24],[7],[56],[87],[81],[55],[19],[40],[68],[23],[80],[53],[76],[93],[95],[95],[67],[31],[80],[62],[73],[97],[33],[28],[62],[81],[57],[40],[11],[89],[28],[97],[86],[20],[5],[77],[52],[57],[88],[20],[48],[42],[86],[49],[62],[53],[43],[98],[32],[15],[42],[50],[19],[32],[67],[84],[60],[8],[85],[43],[59],[65],[40],[81],[55],[56],[54],[59],[78],[53],[0],[24],[7],[53],[33],[69],[86],[7],[1],[16],[58],[61],[34],[53],[84],[21],[58],[25],[45],[3]]
]

const expectedOutputList = [
   [null, null, null, true, false, null, true, null, false],
   [null,false,null,null,null,false,null,true,false,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,null,true,null,null,true,null,null,null,null,null,null,null,null,true,null,null,null,null,false,null,false,null,null,null,null,null,true,null,null,null,null,true,null,null,null,null,null,null,true,true,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,null]
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
const myHashSet = new MyHashSet();
myHashSet.add(1)  // set = [1]
myHashSet.add(2)  // set = [1, 2]
console.log(myHashSet.contains(1))  // return True
console.log(myHashSet.contains(3))  // return false, (not found)
myHashSet.add(2)  // set = [1, 2]
console.log(myHashSet.contains(2))  // return True
myHashSet.remove(2)  // set = [1]
console.log(myHashSet.contains(2))  // return false, (already removed)