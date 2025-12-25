/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: monotonic decreasing stack
 *     A: iteration
 */
class StockSpanner {
   constructor() {
      // monotonic decreasing stack
      // [(price, span), ...]
      this.prices = [];
   };

   next(price) {
      const prices = this.prices;
      let span = 1;

      while (
         prices.length &&
         prices[this.prices.length - 1][0] <= price
      ) {
         const [_, prevSpan] = prices.pop();
         span += prevSpan;
      }
      prices.push([price, span]);
      return span
   };
}


/** 
 * @param {string[]} operations
 * @param {number[][]} args
 * @return {number[][]}
 */
const testInput = (operations, args) => {
   const output = []
   let stockSpanner;

   for (let index = 0; index < operations.length; index++) {
      const operation = operations[index];
      const argument = args[index];

      if (operation === 'StockSpanner') {
         stockSpanner = new StockSpanner(...argument);
         output.push(null);
      } else if (operation === 'next') {
         output.push(stockSpanner.next(...argument));
      }
   };
   return output
}


// Example Input
const operationsList = [
   ['StockSpanner', 'next', 'next', 'next', 'next', 'next', 'next', 'next']
]

const argumentsList = [
   [[], [100], [80], [60], [70], [60], [75], [85]]
]

const expectedOutputList = [
   [null, 1, 1, 1, 2, 1, 4, 6]
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


const stockSpanner = new StockSpanner();
console.log(stockSpanner.next(100));  // return 1
console.log(stockSpanner.next(80));  // return 1
console.log(stockSpanner.next(60));  // return 1
console.log(stockSpanner.next(70));  // return 2
console.log(stockSpanner.next(60));  // return 1
console.log(stockSpanner.next(75));  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
console.log(stockSpanner.next(85));  // return 6