class DoublyLinkedNode {
   constructor(key = null, val = null, next = null, prev = null) {
      this.key = key;
      this.val = val;
      this.next = next;
      this.prev = prev;
   }
}

class DoublyLinkedList {
   constructor() {
      this.first = new DoublyLinkedNode();
      this.last = new DoublyLinkedNode();
      this.first.next = this.last;
      this.last.prev = this.first;
   }

   remove(node) {
      const prev = node.prev;
      const next = node.next;
      prev.next = next;
      next.prev = prev;
      //del node
   }

   add(node) {
      const next = this.last;
      const prev = next.prev;
      node.prev = prev;
      node.next = next;
      prev.next = node;
      next.prev = node;
   }
}

/**
 * Time complexity: O(1)
 * Auxiliary space complexity: O(cap)
 *     O(capacity)
 * Tags:
        DS: doubly linked list, linked list, hash map
 * @param {number} capacity
 */
class LRUCache {
   constructor(capacity) {
      this.capacity = capacity;
      this.size = 0;
      // key to list node map
      this.cache = new Map();  // {1: list node, 2: list node}
      this.doublyLinkedList = new DoublyLinkedList();
   }

   _removeNode(node) {
      this.doublyLinkedList.remove(node);
      this.cache.delete(node.key);
   }

   _addNode(key, val) {
      const node = new DoublyLinkedNode(key, val);
      this.doublyLinkedList.add(node);
      this.cache.set(key, node);
   }

   _updateNode(node, key, val) {
      this._removeNode(node);
      this._addNode(key, val);
   }

   /**
    * @param {number} key
    * @param {number} val
    * @return {void}
    */
   put(key, val) {
      if (this.cache.has(key)) {
         const node = this.cache.get(key);
         this._updateNode(node, key, val);

      } else if (this.size === this.capacity) {
         const lruNode = this.doublyLinkedList.first.next;
         this._updateNode(lruNode, key, val);

      } else {
         this._addNode(key, val);
         this.size++;
      }
   }

   /**
    * @param {number} key
    * @return {number}
    */
   get(key) {
      if (!this.cache.has(key)) {
         return -1
      }

      const node = this.cache.get(key);
      const val = node.val;
      this._updateNode(node, key, val)
      return val;
   }
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let lruCache;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'LRUCache') {
         lruCache = new LRUCache(...argument);
         output.push(null);
      } else if (operation === 'put') {
         lruCache.put(...argument);
         output.push(null);
      } else if (operation === 'get') {
         output.push(lruCache.get(...argument));
      }
   };
   return output
}


// Example Input
const operationsList = [
   ['LRUCache', 'put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get'],
   ['LRUCache', 'put', 'put', 'put', 'put', 'put', 'get', 'put', 'get', 'get', 'put', 'get', 'put', 'put', 'put', 'get', 'put', 'get', 'get', 'get', 'get', 'put', 'put', 'get', 'get', 'get', 'put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get', 'put', 'put', 'put', 'get', 'put', 'get', 'get', 'put', 'put', 'get', 'put', 'put', 'put', 'put', 'get', 'put', 'put', 'get', 'put', 'put', 'get', 'put', 'put', 'put', 'put', 'put', 'get', 'put', 'put', 'get', 'put', 'get', 'get', 'get', 'put', 'get', 'get', 'put', 'put', 'put', 'put', 'get', 'put', 'put', 'put', 'put', 'get', 'get', 'get', 'put', 'put', 'put', 'get', 'put', 'put', 'put', 'get', 'put', 'put', 'put', 'get', 'get', 'get', 'put', 'put', 'put', 'put', 'get', 'put', 'put', 'put', 'put', 'put', 'put', 'put']
]

const argumentsList = [
   [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
   [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
]

const expectedOutputList = [
   [null, null, null, 1, null, -1, null, -1, 3, 4],
   [null, null, null, null, null, null, -1, null, 19, 17, null, -1, null, null, null, -1, null, -1, 5, -1, 12, null, null, 3, 5, 5, null, null, 1, null, -1, null, 30, 5, 30, null, null, null, -1, null, -1, 24, null, null, 18, null, null, null, null, -1, null, null, 18, null, null, -1, null, null, null, null, null, 18, null, null, -1, null, 4, 29, 30, null, 12, -1, null, null, null, null, 29, null, null, null, null, 17, 22, 18, null, null, null, -1, null, null, null, 20, null, null, null, -1, 18, 18, null, null, null, null, 20, null, null, null, null, null, null, null]
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


const lRUCache1 = new LRUCache(2)
lRUCache1.put(1, 1)  // cache is {1=1}
lRUCache1.put(2, 2)  // cache is {1=1, 2=2}
console.log(lRUCache1.get(1))  // return 1
lRUCache1.put(3, 3)  // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
console.log(lRUCache1.get(2))  // returns -1 (not found)
lRUCache1.put(4, 4)  // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
console.log(lRUCache1.get(1))  // return -1 (not found)
console.log(lRUCache1.get(3))  // return 3
console.log(lRUCache1.get(4))  // return 4

const lRUCache2 = new LRUCache(2)
console.log(lRUCache2.get(2))  // return -1
lRUCache2.put(2, 6)
console.log(lRUCache2.get(1))  // return -1
lRUCache2.put(1, 5)
lRUCache2.put(1, 2)
console.log(lRUCache2.get(1))  // return 2
console.log(lRUCache2.get(2))  // return 6

const lRUCache3 = new LRUCache(2)
lRUCache3.put(2, 1)
lRUCache3.put(1, 1)
lRUCache3.put(2, 3)
lRUCache3.put(4, 1)
console.log(lRUCache3.get(1))  // return -1
console.log(lRUCache3.get(2))  // return 3