/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: list
 *     A: interval, iteration
 * @param {number} start
 * @param {number} end
 * @return {boolean}
 */
class MyCalendarTwo {
   constructor() {
      // [[event start, event end], ]
      this.calendar1 = [];
      this.calendar2 = [];
   }

   book(start, end) {
      // one book
      const calendar1 = this.calendar1;
      // two books
      const calendar2 = this.calendar2;

      for (const [bookStart, bookEnd] of calendar2) {
         if (
            start < bookEnd &&
            end > bookStart
         )
            return false
      }

      for (const [bookStart, bookEnd] of calendar1) {
         if (
            start < bookEnd &&
            end > bookStart
         ) {
            const newStart = Math.max(start, bookStart);
            const newEnd = Math.min(end, bookEnd);
            calendar2.push([newStart, newEnd]);
         }
      }

      calendar1.push([start, end]);
      return true
   };
}


const myCalendarTwo = new MyCalendarTwo();
console.log(myCalendarTwo.book(10, 20) === true)
console.log(myCalendarTwo.book(50, 60) === true)
console.log(myCalendarTwo.book(10, 40) === true)
console.log(myCalendarTwo.book(5, 15) === false)
console.log(myCalendarTwo.book(5, 10) === true)
console.log(myCalendarTwo.book(25, 55) === true)
