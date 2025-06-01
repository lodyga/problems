/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags: stack, monotonic stack
 * monotonically decreasing stack
 */
class StockSpanner {
   constructor() {
      this.pricesStack = [];
      this.index = 0;
   };

   next(price) {
      let span = 1;
      let prevIndex = this.index;

      while (
         this.pricesStack.length &&
         this.pricesStack[this.pricesStack.length - 1][1] <= price
      ) {
         [prevIndex, ] = this.pricesStack.pop();
         span = this.index - prevIndex + 1;
      }
      this.pricesStack.push([prevIndex, price]);
      this.index++;
      return span
   }
}


const stockSpanner = new StockSpanner();
console.log(stockSpanner.next(100));  // return 1
console.log(stockSpanner.next(80));  // return 1
console.log(stockSpanner.next(60));  // return 1
console.log(stockSpanner.next(70));  // return 2
console.log(stockSpanner.next(60));  // return 1
console.log(stockSpanner.next(75));  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
console.log(stockSpanner.next(85));  // return 6