class ListNode {
   constructor(val = [null, null], next = null) {
      this.val = val;  // [timestamp, value]
      this.next = next;
   }
}


/**
 * Time complexity: 
 *    set(): O(1)
 *    get(): O(n)
 *    n: `values assigned to a key` count
 * Auxiliary space complexity: O(n*m)
 *     m: key count
 * Tags:
 *     DS: linked list, hash map
 *     A: iteration
 */
class TimeMap2 {
   constructor() {
      this.store = new Map();
   };

   /** 
    * @param {string} key 
    * @param {string} value 
    * @param {number} timestamp
    * @return {void}
    */
   set(key, value, timestamp) {
      const store = this.store;
      if (!store.has(key))
         store.set(key, new ListNode([0, ""]));

      const head = store.get(key);
      const node = new ListNode([timestamp, value], head);
      store.set(key, node);

   };

   /** 
    * @param {string} key 
    * @param {number} timestamp
    * @return {string}
    */
   get(key, timestamp) {
      const store = this.store;
      if (!this.store.get(key))
         return ''

      let node = store.get(key);
      while (timestamp < node.val[0])
         node = node.next

      return node.val[1]
   };
}


/**
 * Time complexity: 
 *    set(): O(1)
 *    get(): O(logn)
 *    n: `values assigned to a key` count
 * Auxiliary space complexity: O(n*m)
 *     m: key count
 * Tags:
 *     DS: list, hash map
 *     A: binary search
 */
class TimeMap {
   constructor() {
      this.store = new Map();
   };

   /** 
    * @param {string} key 
    * @param {string} value 
    * @param {number} timestamp
    * @return {void}
    */
   set(key, value, timestamp) {
      const store = this.store;
      if (!store.has(key))
         store.set(key, [[0, ""]]);

      store.get(key).push([timestamp, value]);
   };

   /** 
    * @param {string} key 
    * @param {number} timestamp
    * @return {string}
    */
   get(key, timestamp) {
      const store = this.store;
      if (!store.has(key))
         return ""

      const keyVals = store.get(key);
      let left = 0;
      let right = keyVals.length - 1;
      let res = keyVals[right][1];

      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleVal = keyVals[middle]

         if (timestamp === middleVal[0]) {
            return middleVal[1]
         } else if (timestamp > middleVal[0]) {
            res = middleVal[1];
            left = middle + 1;
         } else {
            right = middle - 1;
         }
      }
      return res
   };
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let timeMap;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'TimeMap') {
         timeMap = new TimeMap(...argument);
         output.push(null);
      } else if (operation === 'set') {
         timeMap.set(...argument);
         output.push(null);
      } else if (operation === 'get') {
         output.push(timeMap.get(...argument));
      }
   };
   return output
}


// Example Input
const operationsList = [
   ['TimeMap','set','get','get','set','get','get'],
   ['TimeMap','set','set','get','get','get','get','get'],
   ['TimeMap','set','set','get','set','get','get']
]

const argumentsList = [
   [[],['foo','bar',1],['foo',1],['foo',3],['foo','bar2',4],['foo',4],['foo',5]],
   [[],['love','high',10],['love','low',20],['love',5],['love',10],['love',15],['love',20],['love',25]],
   [[],['a','bar',1],['x','b',3],['b',3],['foo','bar2',4],['foo',4],['foo',5]]
]

const expectedOutputList = [
   [null,null,'bar','bar',null,'bar2','bar2'],
   [null,null,null,'','high','high','low','low'],
   [null,null,null,'',null,'bar2','bar2']
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
const timeMap = new TimeMap();
timeMap.set('foo', 'bar', 1);  // store the key 'foo' and value 'bar' along with timestamp = 1.
console.log(timeMap.get('foo', 1));  // return 'bar'
console.log(timeMap.get('foo', 3));  // return 'bar', since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is 'bar'.
timeMap.set('foo', 'bar2', 4);  // store the key 'foo' and value 'bar2' along with timestamp = 4.
console.log(timeMap.get('foo', 4));  // return 'bar2'
console.log(timeMap.get('foo', 5));  // return 'bar2'

// Example 2
const timeMap2 = new TimeMap();
timeMap2.set('love', 'high', 10);
timeMap2.set('love', 'low', 20);
console.log(timeMap2.get('love', 5));  // return ''
console.log(timeMap2.get('love', 10));  // return high
console.log(timeMap2.get('love', 15));  // return high
console.log(timeMap2.get('love', 20));  // return low
console.log(timeMap2.get('love', 25));  // return low

// Example 3
const timeMap3 = new TimeMap();
timeMap3.set('a', 'bar', 1);
timeMap3.set('x', 'b', 3);
console.log(timeMap3.get('b', 3));  // return ''
timeMap3.set('foo', 'bar2', 4);
console.log(timeMap3.get('foo', 4));  // return 'bar2'
console.log(timeMap3.get('foo', 5));  // return 'bar2'